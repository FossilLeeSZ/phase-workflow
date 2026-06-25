from __future__ import annotations

import argparse
import json
import os
import signal
import socket
import subprocess
import sys
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.phase_mcp_guidance import default_guidance_paths
from scripts.phase_mcp_read_core import list_allowed_files
from scripts.phase_mcp_server import PhaseWorkflowMCPServer


PROJECT_CONFIG_PATH = Path(".phase-workflow") / "mcp" / "project.json"
SERVER_LOCK_NAME = "server.lock"
SERVER_READY_NAME = "server.ready.json"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_ENDPOINT_PATH = "/mcp"
REGISTRY_SCHEMA_VERSION = 1
PROJECT_SCHEMA_VERSION = 1
DEFAULT_ALLOWED_CANDIDATES = (
    "AGENTS.md",
    "TODO.md",
    ".codex/skills/phase-workflow/SKILL.md",
    ".codex/skills/phase-workflow/references/phase_policy.md",
    "SKILL.md",
    "PLAN.md",
    "DECISIONS.md",
    "CURRENT_STATE.md",
    "HANDOFF.md",
    "docs/handoff.md",
    "references/phase_policy.md",
    "references/change_request_policy.md",
    "references/handoff_protocol.md",
    "references/verification_policy.md",
)


class LifecycleError(RuntimeError):
    """Raised when MCP lifecycle management must fail closed."""


def configure_project(
    project_root: Path | str,
    *,
    registry_path: Path | str | None = None,
    project_id: str | None = None,
    workspace_id: str | None = None,
    display_name: str | None = None,
    allowed_files: list[str] | tuple[str, ...] | None = None,
) -> dict[str, Any]:
    root = Path(project_root).resolve()
    if not root.is_dir():
        raise LifecycleError(f"project root does not exist: {root}")

    config_path = root / PROJECT_CONFIG_PATH
    existing_config = _read_json(config_path, default=None)
    if existing_config is not None and not isinstance(existing_config, dict):
        raise LifecycleError("project MCP config must be a JSON object")

    stable_project_id = _select_project_id(existing_config, project_id)
    normalized_allowed = _select_allowed_files(root, existing_config, allowed_files)
    project_config = {
        "schema_version": PROJECT_SCHEMA_VERSION,
        "project_id": stable_project_id,
        "display_name": display_name or _existing_value(existing_config, "display_name") or root.name,
        "allowed_files": normalized_allowed,
    }
    _write_json(config_path, project_config)

    resolved_registry_path = _resolve_registry_path(registry_path)
    registry = _load_registry(resolved_registry_path)
    workspace = _find_workspace_by_root(
        registry,
        stable_project_id,
        root,
    )

    if workspace is None:
        workspace = {
            "project_id": stable_project_id,
            "workspace_id": workspace_id or f"workspace-{uuid.uuid4().hex}",
            "workspace_root": str(root),
            "host": DEFAULT_HOST,
            "port": None,
            "endpoint": None,
            "pid": None,
            "lock_path": str(_lock_path(root)),
            "status": "stopped",
        }
        registry["workspaces"].append(workspace)
    else:
        workspace["project_id"] = stable_project_id
        workspace["workspace_root"] = str(root)
        workspace["workspace_id"] = workspace_id or workspace["workspace_id"]
        workspace.setdefault("host", DEFAULT_HOST)
        workspace.setdefault("port", None)
        workspace.setdefault("endpoint", None)
        workspace.setdefault("pid", None)
        workspace.setdefault("lock_path", str(_lock_path(root)))
        workspace.setdefault("status", "stopped")

    _save_registry(resolved_registry_path, registry)

    return _public_workspace_status(workspace)


def start_project(
    project_id: str,
    *,
    workspace_id: str | None = None,
    registry_path: Path | str | None = None,
    host: str = DEFAULT_HOST,
    port: int = 0,
    python_executable: str | None = None,
) -> dict[str, Any]:
    if host != DEFAULT_HOST:
        raise LifecycleError("MCP lifecycle start only supports loopback host 127.0.0.1")

    resolved_registry_path = _resolve_registry_path(registry_path)
    registry = _load_registry(resolved_registry_path)
    workspace = _resolve_workspace(registry, project_id, workspace_id)

    if _workspace_is_running(workspace):
        raise LifecycleError("MCP companion is already running for this workspace")

    root = Path(workspace["workspace_root"]).resolve()
    project_config = _load_project_config(root)
    if project_config["project_id"] != project_id:
        raise LifecycleError("project config project_id mismatch")

    selected_port = _select_port(host, port)
    endpoint = f"http://{host}:{selected_port}{DEFAULT_ENDPOINT_PATH}"
    lock_path = _lock_path(root)
    ready_path = root / ".phase-workflow" / "mcp" / SERVER_READY_NAME
    ready_path.parent.mkdir(parents=True, exist_ok=True)
    _remove_file(ready_path)

    command = [
        python_executable or sys.executable,
        str(Path(__file__).resolve()),
        "serve",
        "--project-root",
        str(root),
        "--project-id",
        project_id,
        "--workspace-id",
        workspace["workspace_id"],
        "--host",
        host,
        "--port",
        str(selected_port),
        "--ready-file",
        str(ready_path),
    ]
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    process = subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creationflags,
    )

    ready = _wait_for_ready_file(ready_path, process)
    workspace.update(
        {
            "host": host,
            "port": ready["port"],
            "endpoint": endpoint,
            "pid": ready["pid"],
            "lock_path": str(lock_path),
            "status": "running",
        }
    )
    _write_json(lock_path, _public_workspace_status(workspace))
    _save_registry(resolved_registry_path, registry)

    return _public_workspace_status(workspace)


def status_project(
    project_id: str,
    *,
    workspace_id: str | None = None,
    registry_path: Path | str | None = None,
) -> dict[str, Any]:
    resolved_registry_path = _resolve_registry_path(registry_path)
    registry = _load_registry(resolved_registry_path)
    workspace = _resolve_workspace(registry, project_id, workspace_id)
    _refresh_workspace_status(workspace)
    _save_registry(resolved_registry_path, registry)
    return _public_workspace_status(workspace)


def stop_project(
    project_id: str,
    *,
    workspace_id: str | None = None,
    registry_path: Path | str | None = None,
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    resolved_registry_path = _resolve_registry_path(registry_path)
    registry = _load_registry(resolved_registry_path)
    workspace = _resolve_workspace(registry, project_id, workspace_id)

    pid = workspace.get("pid")
    if pid is not None and _pid_is_running(pid):
        _terminate_pid(pid)

        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline and _pid_is_running(pid):
            time.sleep(0.05)

        if _pid_is_running(pid):
            raise LifecycleError("MCP companion did not stop before timeout")

    _clear_workspace_process(workspace)
    _remove_file(Path(workspace["lock_path"]))
    _remove_file(Path(workspace["workspace_root"]) / ".phase-workflow" / "mcp" / SERVER_READY_NAME)
    _save_registry(resolved_registry_path, registry)

    return _public_workspace_status(workspace)


def serve_project(
    project_root: Path | str,
    *,
    project_id: str,
    workspace_id: str,
    host: str,
    port: int,
    ready_file: Path | str | None = None,
):
    if host != DEFAULT_HOST:
        raise LifecycleError("MCP server must bind to 127.0.0.1")

    root = Path(project_root).resolve()
    project_config = _load_project_config(root)
    if project_config["project_id"] != project_id:
        raise LifecycleError("project config project_id mismatch")

    server = PhaseWorkflowMCPServer(
        root,
        project_config["allowed_files"],
        project_id=project_id,
        workspace_id=workspace_id,
        guidance_paths=default_guidance_paths(root, project_config["allowed_files"]),
    )
    httpd = _build_http_server(server, host, port)
    actual_port = httpd.server_address[1]
    endpoint = f"http://{host}:{actual_port}{DEFAULT_ENDPOINT_PATH}"

    if ready_file is not None:
        _write_json(
            Path(ready_file),
            {
                "pid": os.getpid(),
                "host": host,
                "port": actual_port,
                "endpoint": endpoint,
            },
        )

    httpd.serve_forever()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="phase-workflow read-only MCP lifecycle")
    subparsers = parser.add_subparsers(dest="command", required=True)

    configure_parser = subparsers.add_parser("configure")
    configure_parser.add_argument("--project-root", default=".")
    configure_parser.add_argument("--registry-path")
    configure_parser.add_argument("--project-id")
    configure_parser.add_argument("--workspace-id")
    configure_parser.add_argument("--display-name")
    configure_parser.add_argument("--allowed-file", action="append", dest="allowed_files")

    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("project_id")
    start_parser.add_argument("--workspace-id")
    start_parser.add_argument("--registry-path")
    start_parser.add_argument("--port", type=int, default=0)

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("project_id")
    status_parser.add_argument("--workspace-id")
    status_parser.add_argument("--registry-path")

    stop_parser = subparsers.add_parser("stop")
    stop_parser.add_argument("project_id")
    stop_parser.add_argument("--workspace-id")
    stop_parser.add_argument("--registry-path")

    serve_parser = subparsers.add_parser("serve")
    serve_parser.add_argument("--project-root", required=True)
    serve_parser.add_argument("--project-id", required=True)
    serve_parser.add_argument("--workspace-id", required=True)
    serve_parser.add_argument("--host", default=DEFAULT_HOST)
    serve_parser.add_argument("--port", type=int, required=True)
    serve_parser.add_argument("--ready-file")

    args = parser.parse_args(argv)

    try:
        if args.command == "configure":
            result = configure_project(
                args.project_root,
                registry_path=args.registry_path,
                project_id=args.project_id,
                workspace_id=args.workspace_id,
                display_name=args.display_name,
                allowed_files=args.allowed_files,
            )
        elif args.command == "start":
            result = start_project(
                args.project_id,
                workspace_id=args.workspace_id,
                registry_path=args.registry_path,
                port=args.port,
            )
        elif args.command == "status":
            result = status_project(
                args.project_id,
                workspace_id=args.workspace_id,
                registry_path=args.registry_path,
            )
        elif args.command == "stop":
            result = stop_project(
                args.project_id,
                workspace_id=args.workspace_id,
                registry_path=args.registry_path,
            )
        else:
            serve_project(
                args.project_root,
                project_id=args.project_id,
                workspace_id=args.workspace_id,
                host=args.host,
                port=args.port,
                ready_file=args.ready_file,
            )
            return 0
    except LifecycleError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


def _build_http_server(
    server: PhaseWorkflowMCPServer,
    host: str,
    port: int,
) -> ThreadingHTTPServer:
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            if self.path != DEFAULT_ENDPOINT_PATH:
                self.send_error(404)
                return

            origin = self.headers.get("Origin")
            if origin and not _allowed_origin(origin):
                self.send_error(403)
                return

            try:
                content_length = int(self.headers.get("Content-Length", "0"))
                raw_body = self.rfile.read(content_length)
                request = json.loads(raw_body.decode("utf-8"))
                response = server.handle_json_rpc_request(request)
                response_body = json.dumps(response, ensure_ascii=False, sort_keys=True).encode(
                    "utf-8"
                )
            except Exception as exc:  # pragma: no cover - defensive HTTP boundary
                response_body = json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {"code": -32603, "message": str(exc)},
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body)

        def do_GET(self):
            self.send_error(405)

        def log_message(self, format, *args):
            return

    return ThreadingHTTPServer((host, port), Handler)


def _select_project_id(existing_config: dict[str, Any] | None, project_id: str | None) -> str:
    selected = project_id or _existing_value(existing_config, "project_id") or f"project-{uuid.uuid4().hex}"
    if not isinstance(selected, str) or not selected.strip():
        raise LifecycleError("project_id is required")
    return selected


def _select_allowed_files(
    root: Path,
    existing_config: dict[str, Any] | None,
    allowed_files: list[str] | tuple[str, ...] | None,
) -> list[str]:
    selected = allowed_files
    if selected is None and existing_config is not None:
        existing_allowed = existing_config.get("allowed_files")
        if isinstance(existing_allowed, list):
            selected = existing_allowed
    if selected is None:
        selected = [path for path in DEFAULT_ALLOWED_CANDIDATES if (root / path).is_file()]

    return list_allowed_files(selected)


def _existing_value(existing_config: dict[str, Any] | None, key: str):
    if existing_config is None:
        return None
    return existing_config.get(key)


def _resolve_registry_path(registry_path: Path | str | None) -> Path:
    if registry_path is None:
        return Path.home() / ".phase-workflow" / "mcp" / "registry.json"
    return Path(registry_path).expanduser().resolve()


def _load_registry(registry_path: Path) -> dict[str, Any]:
    registry = _read_json(
        registry_path,
        default={"schema_version": REGISTRY_SCHEMA_VERSION, "workspaces": []},
    )
    if not isinstance(registry, dict):
        raise LifecycleError("local MCP registry must be a JSON object")
    registry.setdefault("schema_version", REGISTRY_SCHEMA_VERSION)
    registry.setdefault("workspaces", [])
    if not isinstance(registry["workspaces"], list):
        raise LifecycleError("local MCP registry workspaces must be a list")
    return registry


def _save_registry(registry_path: Path, registry: dict[str, Any]):
    registry["workspaces"] = sorted(
        registry["workspaces"],
        key=lambda item: (item.get("project_id", ""), item.get("workspace_root", "")),
    )
    _write_json(registry_path, registry)


def _load_project_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / PROJECT_CONFIG_PATH
    config = _read_json(config_path, default=None)
    if not isinstance(config, dict):
        raise LifecycleError("project MCP config is missing or invalid")
    if config.get("schema_version") != PROJECT_SCHEMA_VERSION:
        raise LifecycleError("unsupported project MCP config schema_version")
    if not isinstance(config.get("project_id"), str) or not config["project_id"].strip():
        raise LifecycleError("project MCP config project_id is missing")
    if not isinstance(config.get("allowed_files"), list):
        raise LifecycleError("project MCP config allowed_files is missing")
    return config


def _find_workspace_by_root(
    registry: dict[str, Any],
    project_id: str,
    project_root: Path,
) -> dict[str, Any] | None:
    root_text = str(project_root)
    for workspace in registry["workspaces"]:
        if workspace.get("project_id") == project_id and workspace.get("workspace_root") == root_text:
            return workspace
    return None


def _resolve_workspace(
    registry: dict[str, Any],
    project_id: str,
    workspace_id: str | None,
) -> dict[str, Any]:
    if not isinstance(project_id, str) or not project_id.strip():
        raise LifecycleError("project_id is required")

    matches = [
        workspace
        for workspace in registry["workspaces"]
        if workspace.get("project_id") == project_id
    ]
    if not matches:
        raise LifecycleError(f"unknown project_id: {project_id}")

    if workspace_id is None:
        if len(matches) > 1:
            raise LifecycleError("ambiguous project_id; workspace_id is required")
        return matches[0]

    for workspace in matches:
        if workspace.get("workspace_id") == workspace_id:
            return workspace

    raise LifecycleError("workspace_id mismatch")


def _refresh_workspace_status(workspace: dict[str, Any]):
    if _workspace_is_running(workspace):
        workspace["status"] = "running"
        return

    _clear_workspace_process(workspace)


def _workspace_is_running(workspace: dict[str, Any]) -> bool:
    pid = workspace.get("pid")
    return pid is not None and _pid_is_running(pid)


def _clear_workspace_process(workspace: dict[str, Any]):
    workspace["status"] = "stopped"
    workspace["pid"] = None
    workspace["endpoint"] = None
    workspace["port"] = None
    workspace["host"] = DEFAULT_HOST


def _pid_is_running(pid: Any) -> bool:
    try:
        value = int(pid)
    except (TypeError, ValueError):
        return False

    if value <= 0:
        return False

    if os.name == "nt":
        return _windows_pid_is_running(value)

    try:
        os.kill(value, 0)
    except OSError:
        return False
    return True


def _windows_pid_is_running(pid: int) -> bool:
    import ctypes
    from ctypes import wintypes

    process_query_limited_information = 0x1000
    still_active = 259

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    handle = kernel32.OpenProcess(
        process_query_limited_information,
        False,
        wintypes.DWORD(pid),
    )
    if not handle:
        return False

    try:
        exit_code = wintypes.DWORD()
        if not kernel32.GetExitCodeProcess(handle, ctypes.byref(exit_code)):
            return False
        return exit_code.value == still_active
    finally:
        kernel32.CloseHandle(handle)


def _terminate_pid(pid: Any):
    value = int(pid)
    if os.name == "nt":
        _windows_terminate_pid(value)
        return

    try:
        os.kill(value, signal.SIGTERM)
    except OSError:
        pass


def _windows_terminate_pid(pid: int):
    import ctypes
    from ctypes import wintypes

    process_terminate = 0x0001

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    handle = kernel32.OpenProcess(process_terminate, False, wintypes.DWORD(pid))
    if not handle:
        return

    try:
        kernel32.TerminateProcess(handle, 1)
    finally:
        kernel32.CloseHandle(handle)


def _select_port(host: str, port: int) -> int:
    if port < 0 or port > 65535:
        raise LifecycleError("port must be between 0 and 65535")
    if port == 0:
        return _choose_free_port(host)
    _assert_port_available(host, port)
    return port


def _choose_free_port(host: str) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind((host, 0))
        return int(probe.getsockname()[1])


def _assert_port_available(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        try:
            probe.bind((host, port))
        except OSError as exc:
            raise LifecycleError(f"port conflict on {host}:{port}") from exc


def _wait_for_ready_file(ready_path: Path, process: subprocess.Popen, timeout_seconds: float = 5.0):
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        if ready_path.is_file():
            ready = _read_json(ready_path, default=None)
            if isinstance(ready, dict):
                return ready
        if process.poll() is not None:
            raise LifecycleError("MCP companion process exited before it became ready")
        time.sleep(0.05)

    try:
        process.terminate()
    except OSError:
        pass
    raise LifecycleError("MCP companion did not become ready before timeout")


def _public_workspace_status(workspace: dict[str, Any]) -> dict[str, Any]:
    return {
        "project_id": workspace["project_id"],
        "workspace_id": workspace["workspace_id"],
        "workspace_root": workspace["workspace_root"],
        "host": workspace.get("host"),
        "port": workspace.get("port"),
        "endpoint": workspace.get("endpoint"),
        "pid": workspace.get("pid"),
        "lock_path": workspace.get("lock_path"),
        "status": workspace.get("status"),
    }


def _lock_path(project_root: Path) -> Path:
    return project_root / ".phase-workflow" / "mcp" / SERVER_LOCK_NAME


def _read_json(path: Path, *, default: Any):
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict[str, Any]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _remove_file(path: Path):
    try:
        path.unlink()
    except FileNotFoundError:
        return


def _allowed_origin(origin: str) -> bool:
    return origin.startswith("http://127.0.0.1") or origin.startswith("http://localhost")


if __name__ == "__main__":
    raise SystemExit(main())

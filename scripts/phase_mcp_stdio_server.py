from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO


if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.phase_mcp_guidance import default_guidance_paths
from scripts.phase_mcp_server import PhaseWorkflowMCPServer, serve_stdio


PROJECT_CONFIG_PATH = Path(".phase-workflow") / "mcp" / "project.json"
PROJECT_SCHEMA_VERSION = 1


class StdioServerError(RuntimeError):
    """Raised when the stdio MCP server must fail closed."""


def build_stdio_server(
    project_root: Path | str,
    *,
    project_id: str,
    workspace_id: str,
) -> PhaseWorkflowMCPServer:
    root = Path(project_root).resolve()
    project_config = _load_project_config(root)
    if project_config["project_id"] != project_id:
        raise StdioServerError("project config project_id mismatch")

    return PhaseWorkflowMCPServer(
        root,
        project_config["allowed_files"],
        project_id=project_id,
        workspace_id=workspace_id,
        guidance_paths=default_guidance_paths(root, project_config["allowed_files"]),
    )


def run_stdio_server(
    project_root: Path | str,
    *,
    project_id: str,
    workspace_id: str,
    input_stream: TextIO,
    output_stream: TextIO,
):
    server = build_stdio_server(
        project_root,
        project_id=project_id,
        workspace_id=workspace_id,
    )
    serve_stdio(server, input_stream, output_stream)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="phase-workflow read-only MCP stdio server")
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--workspace-id", required=True)
    args = parser.parse_args(argv)

    try:
        run_stdio_server(
            args.project_root,
            project_id=args.project_id,
            workspace_id=args.workspace_id,
            input_stream=sys.stdin,
            output_stream=sys.stdout,
        )
    except StdioServerError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    return 0


def _load_project_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / PROJECT_CONFIG_PATH
    if not config_path.is_file():
        raise StdioServerError("project MCP config is missing")

    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise StdioServerError("project MCP config must be a JSON object")
    if config.get("schema_version") != PROJECT_SCHEMA_VERSION:
        raise StdioServerError("unsupported project MCP config schema_version")
    if not isinstance(config.get("project_id"), str) or not config["project_id"].strip():
        raise StdioServerError("project MCP config project_id is missing")
    if not isinstance(config.get("allowed_files"), list) or any(
        not isinstance(path, str) or not path.strip()
        for path in config.get("allowed_files", [])
    ):
        raise StdioServerError("project MCP config allowed_files is missing")

    return config


if __name__ == "__main__":
    raise SystemExit(main())

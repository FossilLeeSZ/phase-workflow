from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, TextIO

from scripts.phase_mcp_read_core import (
    MCPReadError,
    get_default_snapshot,
    list_allowed_files,
    read_allowed_file,
    read_scoped_section,
)


PROTOCOL_VERSION = "2025-06-18"
SERVER_NAME = "phase-workflow-mcp"
SERVER_VERSION = "0.17.4"

TOOL_NAMES = (
    "get_default_snapshot",
    "list_allowed_files",
    "read_allowed_file",
    "read_scoped_section",
)

READ_ONLY_ANNOTATIONS = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}


class MCPServerError(RuntimeError):
    """Raised when the local MCP server boundary rejects a request."""


class PhaseWorkflowMCPServer:
    def __init__(
        self,
        project_root: Path | str,
        allowed_files: Iterable[Path | str],
        *,
        project_id: str,
        workspace_id: str | None = None,
        guidance_paths: Iterable[Path | str] | None = None,
        compact_state_paths: Iterable[Path | str] | None = None,
    ):
        self.project_root = Path(project_root).resolve()
        self.allowed_files = tuple(str(path) for path in allowed_files)
        self.project_id = _require_non_empty_string("project_id", project_id)
        self.workspace_id = workspace_id
        self.guidance_paths = tuple(str(path) for path in guidance_paths or ())
        self.compact_state_paths = (
            tuple(str(path) for path in compact_state_paths)
            if compact_state_paths is not None
            else None
        )

        if self.workspace_id is not None:
            _require_non_empty_string("workspace_id", self.workspace_id)

    def list_tools(self) -> list[dict[str, Any]]:
        return [_tool_schema(name, self.workspace_id is not None) for name in TOOL_NAMES]

    def call_tool(self, name: str, arguments: Mapping[str, Any] | None = None):
        if name not in TOOL_NAMES:
            raise MCPServerError(f"Unknown MCP tool: {name}")

        args = _coerce_arguments(arguments)
        self._validate_identity(args)

        if name == "get_default_snapshot":
            payload = get_default_snapshot(
                self.project_root,
                self.allowed_files,
                guidance_paths=self.guidance_paths,
                compact_state_paths=self.compact_state_paths,
            )
        elif name == "list_allowed_files":
            payload = {
                "kind": "allowed_files",
                "allowed_files": list_allowed_files(self.allowed_files),
                "source_refs": ["mcp_config.allowed_files"],
            }
        elif name == "read_allowed_file":
            payload = {
                "kind": "allowed_file",
                **read_allowed_file(
                    self.project_root,
                    _require_argument(args, "path"),
                    self.allowed_files,
                ),
            }
        else:
            payload = {
                "kind": "scoped_section",
                **read_scoped_section(
                    self.project_root,
                    _require_argument(args, "path"),
                    _require_argument(args, "heading"),
                    self.allowed_files,
                ),
            }

        return _tool_result(self._attach_identity(payload))

    def handle_json_rpc_request(self, request: Mapping[str, Any]):
        request_id = request.get("id") if isinstance(request, Mapping) else None

        try:
            if not isinstance(request, Mapping):
                raise MCPServerError("JSON-RPC request must be an object")

            method = request.get("method")
            params = request.get("params") or {}
            if params is None:
                params = {}
            if not isinstance(params, Mapping):
                raise MCPServerError("JSON-RPC params must be an object")

            if method == "initialize":
                return _json_rpc_result(
                    request_id,
                    {
                        "protocolVersion": PROTOCOL_VERSION,
                        "serverInfo": {
                            "name": SERVER_NAME,
                            "version": SERVER_VERSION,
                        },
                        "capabilities": {"tools": {"listChanged": False}},
                    },
                )

            if method == "tools/list":
                return _json_rpc_result(request_id, {"tools": self.list_tools()})

            if method == "tools/call":
                tool_name = params.get("name")
                if not isinstance(tool_name, str) or not tool_name.strip():
                    raise MCPServerError("tool name is required")
                return _json_rpc_result(
                    request_id,
                    self.call_tool(tool_name, params.get("arguments") or {}),
                )

            raise MCPServerError(f"Unsupported JSON-RPC method: {method}")
        except (MCPReadError, MCPServerError, TypeError, ValueError) as exc:
            return _json_rpc_error(request_id, -32602, str(exc))

    def _validate_identity(self, arguments: Mapping[str, Any]):
        project_id = _require_argument(arguments, "project_id")
        if project_id != self.project_id:
            raise MCPServerError("project_id mismatch")

        if self.workspace_id is None:
            return

        workspace_id = _require_argument(arguments, "workspace_id")
        if workspace_id != self.workspace_id:
            raise MCPServerError("workspace_id mismatch")

    def _attach_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        result = {
            "project_id": self.project_id,
            **payload,
        }
        if self.workspace_id is not None:
            result["workspace_id"] = self.workspace_id
        return result


def serve_stdio(
    server: PhaseWorkflowMCPServer,
    input_stream: TextIO,
    output_stream: TextIO,
):
    for line in input_stream:
        if not line.strip():
            continue

        try:
            request = json.loads(line)
        except json.JSONDecodeError as exc:
            response = _json_rpc_error(None, -32700, f"Parse error: {exc.msg}")
        else:
            response = server.handle_json_rpc_request(request)

        output_stream.write(json.dumps(response, ensure_ascii=False, sort_keys=True))
        output_stream.write("\n")
        output_stream.flush()


def _tool_schema(name: str, workspace_id_required: bool) -> dict[str, Any]:
    schema = copy.deepcopy(_BASE_TOOL_SCHEMAS[name])
    required = ["project_id", *schema["inputSchema"].get("required", [])]
    if workspace_id_required:
        required.insert(1, "workspace_id")

    schema["inputSchema"]["required"] = required
    schema["annotations"] = copy.deepcopy(READ_ONLY_ANNOTATIONS)
    return schema


def _tool_result(payload: dict[str, Any]) -> dict[str, Any]:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return {
        "content": [{"type": "text", "text": text}],
        "structuredContent": payload,
        "isError": False,
    }


def _json_rpc_result(request_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result,
    }


def _json_rpc_error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


def _coerce_arguments(arguments: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if arguments is None:
        return {}
    if not isinstance(arguments, Mapping):
        raise MCPServerError("tool arguments must be an object")
    return arguments


def _require_argument(arguments: Mapping[str, Any], name: str) -> str:
    value = arguments.get(name)
    if not isinstance(value, str) or not value.strip():
        raise MCPServerError(f"{name} is required")
    return value


def _require_non_empty_string(name: str, value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise MCPServerError(f"{name} is required")
    return value


_IDENTITY_PROPERTIES = {
    "project_id": {
        "type": "string",
        "description": "Stable project identity selected during MCP project configuration.",
    },
    "workspace_id": {
        "type": "string",
        "description": "Machine-local checkout identity when multiple workspaces may exist.",
    },
}


_BASE_TOOL_SCHEMAS = {
    "get_default_snapshot": {
        "name": "get_default_snapshot",
        "title": "Get Default Snapshot",
        "description": "Read the bounded default planning snapshot for ChatGPT/MCP planning.",
        "inputSchema": {
            "type": "object",
            "properties": copy.deepcopy(_IDENTITY_PROPERTIES),
            "additionalProperties": False,
        },
    },
    "list_allowed_files": {
        "name": "list_allowed_files",
        "title": "List Allowed Files",
        "description": "List project-relative files that this MCP server may read.",
        "inputSchema": {
            "type": "object",
            "properties": copy.deepcopy(_IDENTITY_PROPERTIES),
            "additionalProperties": False,
        },
    },
    "read_allowed_file": {
        "name": "read_allowed_file",
        "title": "Read Allowed File",
        "description": "Read one allowlisted project file by project-relative path.",
        "inputSchema": {
            "type": "object",
            "properties": {
                **copy.deepcopy(_IDENTITY_PROPERTIES),
                "path": {
                    "type": "string",
                    "description": "Project-relative allowlisted file path.",
                },
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    "read_scoped_section": {
        "name": "read_scoped_section",
        "title": "Read Scoped Section",
        "description": "Read one named Markdown section from an allowlisted project file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                **copy.deepcopy(_IDENTITY_PROPERTIES),
                "path": {
                    "type": "string",
                    "description": "Project-relative allowlisted Markdown file path.",
                },
                "heading": {
                    "type": "string",
                    "description": "Exact Markdown heading line, such as ## Phase 17.4.",
                },
            },
            "required": ["path", "heading"],
            "additionalProperties": False,
        },
    },
}

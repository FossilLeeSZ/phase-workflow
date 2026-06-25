from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping


CHATGPT_MCP_MODE = "ChatGPT/MCP planning with Codex execution"
REQUIRED_HANDOFF_FIELDS = (
    "phase_workflow_handoff: 1",
    "project_id",
    "workspace_id",
    "mode",
    "source_refs",
    "snapshot_id",
    "requested_action",
    "stop_condition",
)


class SetupOutputError(RuntimeError):
    """Raised when ChatGPT setup output cannot be produced safely."""


def build_setup_card(
    project_config: Mapping[str, Any],
    workspace_status: Mapping[str, Any],
    *,
    tunnel_id: str | None = None,
    tunnel_profile_name: str | None = None,
    tunnel_target_type: str = "stdio",
    python_command: str = "python",
    stdio_server_script: str | None = None,
) -> dict[str, Any]:
    validated = _validate_inputs(project_config, workspace_status)
    allowed_files = validated["allowed_files"]
    allowed_files_summary = _allowed_files_summary(allowed_files)
    secure_tunnel_profile = _build_secure_tunnel_profile(
        validated,
        allowed_files_summary=allowed_files_summary,
        tunnel_id=tunnel_id,
        tunnel_profile_name=tunnel_profile_name,
        tunnel_target_type=tunnel_target_type,
        python_command=python_command,
        stdio_server_script=stdio_server_script,
    )

    return {
        "kind": "chatgpt_mcp_setup_card",
        "schema_version": 1,
        "connector_transport": "local read-only MCP endpoint over loopback HTTP",
        "endpoint": validated["endpoint"],
        "project_id": validated["project_id"],
        "workspace_id": validated["workspace_id"],
        "display_name": validated["display_name"],
        "workspace_root": validated["workspace_root"],
        "allowed_files": allowed_files,
        "allowed_files_summary": allowed_files_summary,
        "connection_options": [
            {
                "name": "openai_secure_mcp_tunnel",
                "recommended_for": "ChatGPT web or other supported OpenAI surfaces when available.",
                "transport_boundary": "OpenAI Secure MCP Tunnel keeps the MCP server private and uses outbound tunnel-client connectivity.",
                "profile_name": secure_tunnel_profile["profile_name"],
                "tunnel_id": secure_tunnel_profile["tunnel_id"],
                "target_type": secure_tunnel_profile["target_type"],
            },
            {
                "name": "local_loopback_http",
                "recommended_for": "same-machine local development and existing companion smoke tests.",
                "endpoint": validated["endpoint"],
            },
        ],
        "secure_tunnel_profile": secure_tunnel_profile,
        "lifecycle_guidance": _build_lifecycle_guidance(
            validated,
            secure_tunnel_profile,
        ),
        "diagnostics_guidance": _build_diagnostics_guidance(
            validated,
            secure_tunnel_profile,
        ),
        "chatgpt_side_steps": [
            "In ChatGPT connector settings, use the Tunnel connection option when Secure Tunnel is available.",
            "Select an available tunnel or paste the tunnel_id from this card or OpenAI Platform tunnel settings.",
            "Use the project_id and workspace_id from this card to confirm the intended local project.",
            "Send the starter ChatGPT planning prompt in that ChatGPT conversation.",
            "After ChatGPT plans through MCP, copy its short handoff back into Codex.",
        ],
        "codex_boundary": [
            "Direct Codex conversation remains Codex-only.",
            "MCP is only for ChatGPT-side planning reads.",
            "The setup card is connector guidance and does not authorize execution.",
            "Codex still validates local files, phase gates, authorization branch, and stop condition before execution.",
        ],
    }


def build_starter_prompt(
    project_config: Mapping[str, Any],
    workspace_status: Mapping[str, Any],
    *,
    requested_action: str = "Plan the next phase and return a draft start gate preview plus Codex handoff.",
    stop_condition: str = (
        "Return a planning-only draft start gate preview and short Codex handoff only; "
        "do not execute."
    ),
) -> str:
    validated = _validate_inputs(project_config, workspace_status)

    return "\n".join(
        [
            "Use the local read-only MCP companion for this project.",
            "",
            f"endpoint: {validated['endpoint']}",
            f"project_id: {validated['project_id']}",
            f"workspace_id: {validated['workspace_id']}",
            f"mode: {CHATGPT_MCP_MODE}",
            "",
            "Read the bounded default snapshot first.",
            "Use on-demand reads only for concrete planning needs, and name the file, heading, or section for each read.",
            "Record source refs for every MCP read you use.",
            "",
            "Do not execute commands.",
            "Do not call Codex.",
            "Do not run `codex exec`.",
            "Do not start Codex or the local companion.",
            "Do not include full project history or full file contents.",
            "",
            "Return a planning-only draft start gate preview after MCP-assisted planning.",
            "The draft preview is non-authoritative and not Codex execution authorization.",
            "Codex must still show the authoritative start gate after local revalidation and wait for separate Codex-side execution confirmation before any mutation.",
            "The draft preview should include these fields when they are present in MCP planning context:",
            "draft_start_gate_preview: 1",
            "status: planning-only; non-authoritative; not Codex execution authorization",
            "current_phase:",
            "goal:",
            "non_goals:",
            "split_decision:",
            "verification_loop:",
            "confirmation_status:",
            "source_refs:",
            "snapshot_id:",
            "",
            "Then return the short Codex handoff.",
            "The handoff must include these header fields:",
            "phase_workflow_handoff: 1",
            f"project_id: {validated['project_id']}",
            f"workspace_id: {validated['workspace_id']}",
            f"mode: {CHATGPT_MCP_MODE}",
            "source_refs:",
            "snapshot_id:",
            f"requested_action: {requested_action}",
            f"stop_condition: {stop_condition}",
        ]
    )


def build_chatgpt_setup_output(
    project_config: Mapping[str, Any],
    workspace_status: Mapping[str, Any],
    *,
    requested_action: str = "Plan the next phase and return a draft start gate preview plus Codex handoff.",
    stop_condition: str = (
        "Return a planning-only draft start gate preview and short Codex handoff only; "
        "do not execute."
    ),
    tunnel_id: str | None = None,
    tunnel_profile_name: str | None = None,
    tunnel_target_type: str = "stdio",
    python_command: str = "python",
    stdio_server_script: str | None = None,
) -> dict[str, Any]:
    setup_card = build_setup_card(
        project_config,
        workspace_status,
        tunnel_id=tunnel_id,
        tunnel_profile_name=tunnel_profile_name,
        tunnel_target_type=tunnel_target_type,
        python_command=python_command,
        stdio_server_script=stdio_server_script,
    )
    starter_prompt = build_starter_prompt(
        project_config,
        workspace_status,
        requested_action=requested_action,
        stop_condition=stop_condition,
    )

    return {
        "kind": "chatgpt_mcp_setup_output",
        "schema_version": 1,
        "setup_card": setup_card,
        "starter_chatgpt_planning_prompt": starter_prompt,
        "final_handoff_owner": "ChatGPT after MCP-assisted planning",
        "codex_execution_boundary": [
            "This output is ChatGPT setup guidance, not a final Codex handoff.",
            "Codex execution still requires a valid header-based handoff and local revalidation.",
            "Direct Codex conversation remains Codex-only unless a valid ChatGPT/MCP handoff header is pasted back.",
        ],
    }


def _validate_inputs(
    project_config: Mapping[str, Any],
    workspace_status: Mapping[str, Any],
) -> dict[str, Any]:
    project_id = _required_text(project_config, "project_id")
    status_project_id = _required_text(workspace_status, "project_id")
    if project_id != status_project_id:
        raise SetupOutputError("project_id mismatch between project config and workspace status")

    status = _required_text(workspace_status, "status")
    if status != "running":
        raise SetupOutputError("workspace status must be running before ChatGPT setup output")

    workspace_id = _required_text(workspace_status, "workspace_id")
    endpoint = _required_text(workspace_status, "endpoint")
    workspace_root = _required_text(workspace_status, "workspace_root")
    display_name = project_config.get("display_name") or project_id
    if not isinstance(display_name, str) or not display_name.strip():
        display_name = project_id

    allowed_files = project_config.get("allowed_files")
    if not isinstance(allowed_files, list) or any(
        not isinstance(path, str) or not path.strip() for path in allowed_files
    ):
        raise SetupOutputError("allowed_files must be a list of project-relative paths")

    return {
        "project_id": project_id,
        "workspace_id": workspace_id,
        "endpoint": endpoint,
        "workspace_root": workspace_root,
        "display_name": display_name,
        "allowed_files": list(allowed_files),
    }


def _required_text(mapping: Mapping[str, Any], key: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise SetupOutputError(f"{key} is required")
    return value


def _build_secure_tunnel_profile(
    validated: Mapping[str, Any],
    *,
    allowed_files_summary: str,
    tunnel_id: str | None,
    tunnel_profile_name: str | None,
    tunnel_target_type: str,
    python_command: str,
    stdio_server_script: str | None,
) -> dict[str, Any]:
    target_type = _validate_tunnel_target_type(tunnel_target_type)
    profile_name = (
        _clean_optional_text(tunnel_profile_name)
        or _default_tunnel_profile_name(
            validated["project_id"],
            validated["workspace_id"],
        )
    )
    tunnel_identifier = (
        _clean_optional_text(tunnel_id)
        or "<tunnel_id from OpenAI Platform tunnel settings>"
    )
    stdio_target = (
        _build_stdio_target(
            validated,
            python_command=python_command,
            stdio_server_script=stdio_server_script,
        )
        if target_type == "stdio"
        else None
    )
    http_target = _build_http_target(validated) if target_type == "http" else None

    return {
        "connection_type": "OpenAI Secure MCP Tunnel",
        "tunnel_id": tunnel_identifier,
        "profile_name": profile_name,
        "project_id": validated["project_id"],
        "workspace_id": validated["workspace_id"],
        "allowed_files_summary": allowed_files_summary,
        "target_type": target_type,
        "target_description": _tunnel_target_description(target_type),
        "stdio_target": stdio_target,
        "http_target": http_target,
        "tunnel_client_commands": _build_tunnel_client_commands(
            profile_name,
            tunnel_identifier,
            target_type=target_type,
            stdio_target=stdio_target,
            http_target=http_target,
        ),
        "chatgpt_connector_guidance": [
            "In ChatGPT connector settings, choose the Tunnel connection option for the MCP connector.",
            "Select the visible tunnel or paste the tunnel_id when the target workspace supports it.",
            "Confirm the selected connector is for this project_id and workspace_id before planning.",
            "After ChatGPT uses MCP for planning, copy ChatGPT's short handoff back into Codex.",
        ],
        "tunnel_client_profile_guidance": [
            "Create or update the named tunnel-client profile outside project files.",
            "Keep tunnel-client running while ChatGPT discovers tools or performs MCP planning reads.",
            "Use the stdio target for the built-in read-only MCP server when available; use HTTP only for an already running local companion.",
        ],
        "secret_boundary": [
            "API keys and tunnel runtime keys are user-provided runtime secrets.",
            "Secret values must not be written to project config, local registry, handoff prompts, README examples, or tests.",
            "This setup output may name required secret categories but must not print or persist secret values.",
        ],
    }


def _build_lifecycle_guidance(
    validated: Mapping[str, Any],
    secure_tunnel_profile: Mapping[str, Any],
) -> dict[str, Any]:
    tunnel_commands = secure_tunnel_profile["tunnel_client_commands"]

    return {
        "local_companion": {
            "owner": "Codex after explicit user confirmation",
            "commands": ["configure", "start", "status", "stop"],
            "script": "scripts/phase_mcp_lifecycle.py",
            "scope": "Project-local read-only MCP companion setup and loopback process management only.",
            "project_id": validated["project_id"],
            "workspace_id": validated["workspace_id"],
            "host_boundary": "Binds to loopback 127.0.0.1 by default; ChatGPT connects through Secure Tunnel or same-machine local testing, not by public project ports.",
            "port_conflict": "Port conflicts are local companion issues; choose another local companion port or stop the conflicting local process. Secure Tunnel is not public exposure. Do not expose arbitrary project ports publicly.",
            "chatgpt_boundary": "ChatGPT must not start the local companion, Codex, or project commands.",
        },
        "secure_tunnel": {
            "owner": "User/operator outside Codex",
            "profile_name": secure_tunnel_profile["profile_name"],
            "tunnel_id": secure_tunnel_profile["tunnel_id"],
            "target_type": secure_tunnel_profile["target_type"],
            "commands": ["init", "doctor", "run"],
            "init_argv": tunnel_commands["init_argv"],
            "doctor_argv": tunnel_commands["doctor_argv"],
            "run_argv": tunnel_commands["run_argv"],
            "requires": [
                "tunnel_id associated with the intended OpenAI organization and ChatGPT workspace",
                "runtime key or operator identity with Tunnels Read + Use",
                "MCP server reachable over stdio or HTTP from the tunnel-client host",
                "tunnel-client running in the same trust boundary as the private MCP server",
            ],
            "availability_boundary": "Connector discovery and MCP tool calls require tunnel-client run to stay running; product availability still depends on account, workspace, connector, and permission support.",
            "stop_rule": "Stop by stopping the user-run tunnel-client process or service; ChatGPT and Codex do not stop it implicitly.",
            "codex_boundary": "Codex may print setup guidance, but does not start tunnel-client, operate ChatGPT, or use MCP for direct Codex planning.",
        },
    }


def _build_diagnostics_guidance(
    validated: Mapping[str, Any],
    secure_tunnel_profile: Mapping[str, Any],
) -> dict[str, list[str]]:
    profile_name = secure_tunnel_profile["profile_name"]

    return {
        "tunnel_not_visible": [
            "Verify the tunnel_id and workspace association for the target ChatGPT workspace.",
            "Verify the connector operator has Tunnels Read + Use.",
            "A tunnel associated only with a Platform organization may not appear in the intended ChatGPT workspace.",
        ],
        "connector_discovery_or_tool_calls_fail": [
            "Confirm tunnel-client run --profile <name> is still running.",
            "Run tunnel-client doctor --profile <name> --explain for the selected profile.",
            f"For this setup card, the selected profile is {profile_name}.",
            "Confirm the MCP target is reachable from the host where tunnel-client runs.",
        ],
        "permission_or_workspace": [
            "Tunnels Read may allow inspection, while Tunnels Use is required for connector operation.",
            "Tunnels Manage is separate and is needed only for creating or editing tunnel metadata.",
            "Check account, organization, workspace association, connector UI availability, and permissions before treating the project setup as broken.",
        ],
        "port_conflict": [
            f"Port conflicts are a local companion issue on local loopback 127.0.0.1 for {validated['endpoint']}.",
            "Choose another local companion port or stop the conflicting local process.",
            "Secure Tunnel is not public exposure and does not require exposing arbitrary project ports publicly.",
        ],
        "client_stopped": [
            "If tunnel-client is stopped or disconnected, requests through the tunnel fail until tunnel-client reconnects.",
            "Restart the user-managed tunnel-client process or service, then retry connector discovery or the planning read.",
        ],
        "http_loopback_boundary": [
            "HTTP target guidance is a local loopback compatibility path for same-machine development or an already running MCP server URL.",
            "Do not expose arbitrary project ports publicly to make Secure Tunnel work; prefer the stdio target for the built-in read-only MCP server when available.",
        ],
    }


def _build_stdio_target(
    validated: Mapping[str, Any],
    *,
    python_command: str,
    stdio_server_script: str | None,
) -> dict[str, Any]:
    selected_python = _required_optional_text(python_command, "python_command")
    selected_script = _clean_optional_text(stdio_server_script) or str(
        Path(__file__).resolve().with_name("phase_mcp_stdio_server.py")
    )
    argv = [
        selected_python,
        selected_script,
        "--project-root",
        validated["workspace_root"],
        "--project-id",
        validated["project_id"],
        "--workspace-id",
        validated["workspace_id"],
    ]

    return {
        "target_type": "stdio",
        "server": "built-in read-only phase-workflow MCP server",
        "mcp_command_argv": argv,
        "mcp_command": _join_command(argv),
        "identity_fields": {
            "project_id": validated["project_id"],
            "workspace_id": validated["workspace_id"],
        },
        "path_boundary": "Local paths are for tunnel-client setup only and must not be copied into the ChatGPT-to-Codex handoff.",
    }


def _build_http_target(validated: Mapping[str, Any]) -> dict[str, str]:
    return {
        "target_type": "http",
        "mcp_server_url": validated["endpoint"],
        "recommended_for": "local development or compatibility with an already running MCP server URL.",
    }


def _build_tunnel_client_commands(
    profile_name: str,
    tunnel_id: str,
    *,
    target_type: str,
    stdio_target: Mapping[str, Any] | None,
    http_target: Mapping[str, Any] | None,
) -> dict[str, Any]:
    init_argv = [
        "tunnel-client",
        "init",
        "--sample",
        "sample_mcp_stdio_local" if target_type == "stdio" else "sample_mcp_http_local",
        "--profile",
        profile_name,
        "--tunnel-id",
        tunnel_id,
    ]
    if target_type == "stdio":
        if stdio_target is None:
            raise SetupOutputError("stdio target guidance is required")
        init_argv.extend(["--mcp-command", stdio_target["mcp_command"]])
    else:
        if http_target is None:
            raise SetupOutputError("http target guidance is required")
        init_argv.extend(["--mcp-server-url", http_target["mcp_server_url"]])

    return {
        "init_argv": init_argv,
        "doctor_argv": [
            "tunnel-client",
            "doctor",
            "--profile",
            profile_name,
            "--explain",
        ],
        "run_argv": [
            "tunnel-client",
            "run",
            "--profile",
            profile_name,
        ],
        "execution_boundary": "User runs tunnel-client outside Codex after providing runtime secrets.",
    }


def _validate_tunnel_target_type(value: str) -> str:
    if value not in {"stdio", "http"}:
        raise SetupOutputError("tunnel_target_type must be either stdio or http")
    return value


def _required_optional_text(value: str, key: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SetupOutputError(f"{key} is required")
    return value.strip()


def _clean_optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise SetupOutputError("optional tunnel fields must be text")
    cleaned = value.strip()
    return cleaned or None


def _default_tunnel_profile_name(project_id: str, workspace_id: str) -> str:
    base = _slug_text(f"phase-workflow-{project_id}-{workspace_id}")
    return base[:80].strip("-") or "phase-workflow-mcp"


def _slug_text(value: str) -> str:
    chars: list[str] = []
    previous_dash = False

    for char in value.lower():
        if char.isalnum():
            chars.append(char)
            previous_dash = False
        elif not previous_dash:
            chars.append("-")
            previous_dash = True

    return "".join(chars)


def _join_command(argv: list[str]) -> str:
    return " ".join(_quote_command_arg(arg) for arg in argv)


def _quote_command_arg(arg: str) -> str:
    if arg and all(char not in arg for char in (' ', '\t', '"')):
        return arg
    escaped = arg.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _tunnel_target_description(target_type: str) -> str:
    if target_type == "stdio":
        return "Preferred Secure Tunnel target for the built-in read-only MCP server: tunnel-client launches a local stdio MCP command."
    return "HTTP Secure Tunnel target for an already running MCP server URL, mainly for local companion development or compatibility."


def _allowed_files_summary(allowed_files: list[str]) -> str:
    count = len(allowed_files)
    suffix = "file" if count == 1 else "files"
    return f"{count} allowlisted {suffix}"

from __future__ import annotations

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
) -> dict[str, Any]:
    validated = _validate_inputs(project_config, workspace_status)
    allowed_files = validated["allowed_files"]

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
        "allowed_files_summary": _allowed_files_summary(allowed_files),
        "chatgpt_side_steps": [
            "In ChatGPT, connect or select the local MCP connector for this endpoint.",
            "Use the project_id and workspace_id from this card to select the intended local project.",
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
    requested_action: str = "Plan the next phase and return a Codex handoff.",
    stop_condition: str = "Return a short Codex handoff only; do not execute.",
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
            "Return a short Codex handoff after MCP-assisted planning.",
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
    requested_action: str = "Plan the next phase and return a Codex handoff.",
    stop_condition: str = "Return a short Codex handoff only; do not execute.",
) -> dict[str, Any]:
    setup_card = build_setup_card(project_config, workspace_status)
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


def _allowed_files_summary(allowed_files: list[str]) -> str:
    count = len(allowed_files)
    suffix = "file" if count == 1 else "files"
    return f"{count} allowlisted {suffix}"

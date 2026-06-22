# ChatGPT/MCP Planning Example

This example shows how to use optional ChatGPT/MCP planning with Codex execution while keeping
Codex responsible for gates, validation, commands, and file edits.

## Scenario

A project already uses `phase-workflow`. The user wants to discuss the next phase in ChatGPT
because the planning thread may be long, but wants Codex to execute commands and mutate files.

## Codex-Only Default Path

Codex-only remains the default path. In that path, Codex reads bounded recovery context,
shows the next phase gate, waits for separate confirmation, executes commands, edits files,
verifies, and updates recovery records.

No MCP setup is required for the Codex-only path.

## ChatGPT/MCP Planning Path

The optional path is ChatGPT/MCP planning with Codex execution. ChatGPT may use the
read-only MCP companion through an available connector path to inspect bounded project
context and produce a short handoff prompt for Codex.

The local read-only MCP companion must not write files.
The local companion must not call Codex, run `codex exec`, start Codex, or execute project
commands.

## Built-In Companion Enablement Flow

In a project that has adopted `phase-workflow`, the user asks Codex to enable optional
ChatGPT/MCP planning. After the visible gate and separate confirmation, Codex can configure
and manage the local companion for that project.

Typical local lifecycle commands use the installed skill copy:

- `python .codex/skills/phase-workflow/scripts/phase_mcp_lifecycle.py configure --project-root .`
- `python .codex/skills/phase-workflow/scripts/phase_mcp_lifecycle.py start <project_id> --workspace-id <workspace_id>`
- `python .codex/skills/phase-workflow/scripts/phase_mcp_lifecycle.py status <project_id> --workspace-id <workspace_id>`
- `python .codex/skills/phase-workflow/scripts/phase_mcp_lifecycle.py stop <project_id> --workspace-id <workspace_id>`

After status reports a running workspace, Codex can use `scripts/phase_mcp_setup_output.py`
to prepare the ChatGPT setup card and starter ChatGPT planning prompt. The setup output is
not the final Codex handoff. ChatGPT, not Codex configuration, generates the final Codex
handoff after MCP-assisted planning.

In ChatGPT, select the configured MCP connector or tunnel for this setup card. For remote
ChatGPT, use OpenAI Secure MCP Tunnel when available; local loopback endpoint details are for
same-machine development and smoke tests only. Paste the starter prompt, let ChatGPT read
through MCP, and copy the resulting short handoff back into Codex. Direct Codex chat still
follows the Codex-only path unless a valid handoff header is pasted back.

## OpenAI Secure MCP Tunnel

Use OpenAI Secure MCP Tunnel as the preferred remote ChatGPT connection path when available.
Local loopback remains useful for same-machine development and smoke tests. Secure Tunnel
keeps the MCP server private and uses outbound tunnel-client connectivity instead of public
inbound project ports.

The setup card can include a `secure_tunnel_profile` for ChatGPT connector setup:

Important setup fields include `tunnel_id`, `profile_name`, `target_type`, `stdio_target`,
`http_target`, `tunnel_client_commands`, `lifecycle_guidance`, and `diagnostics_guidance`.

```yaml
secure_tunnel_profile:
  connection_type: OpenAI Secure MCP Tunnel
  tunnel_id: <tunnel_id from OpenAI Platform tunnel settings>
  profile_name: phase-workflow-phase-demo-workspace-demo
  target_type: stdio
  stdio_target:
    server: built-in read-only phase-workflow MCP server
    mcp_command_argv:
      - python
      - .codex/skills/phase-workflow/scripts/phase_mcp_stdio_server.py
      - --project-root
      - .
      - --project-id
      - phase-demo
      - --workspace-id
      - workspace-demo
  http_target: null
  tunnel_client_commands:
    init_argv:
      - tunnel-client
      - init
      - --sample
      - sample_mcp_stdio_local
      - --profile
      - phase-workflow-phase-demo-workspace-demo
      - --tunnel-id
      - <tunnel_id>
      - --mcp-command
      - <mcp command from setup output>
    doctor_argv:
      - tunnel-client
      - doctor
      - --profile
      - phase-workflow-phase-demo-workspace-demo
      - --explain
    run_argv:
      - tunnel-client
      - run
      - --profile
      - phase-workflow-phase-demo-workspace-demo
lifecycle_guidance:
  local_companion: Codex can configure/start/status/stop after explicit user confirmation.
  secure_tunnel: User/operator runs tunnel-client outside Codex.
diagnostics_guidance:
  tunnel_not_visible: Check workspace association and Tunnels Read and Tunnels Use.
  connector_failure: Run tunnel-client doctor --profile <name> --explain.
  client_stopped: Restart tunnel-client run --profile <name>.
```

If tunnel-client is stopped or disconnected, requests through the tunnel fail until it
reconnects. Port conflicts are local companion issues. Do not expose arbitrary project ports
publicly to make Secure Tunnel work.

For diagnostics, use `tunnel-client doctor --profile <name> --explain` and confirm
`tunnel-client run --profile <name>` is still active.

Do not store OpenAI API keys, tunnel runtime keys, or other tunnel secrets in project config,
local registry, handoff prompts, README examples, or tests. The setup output is ChatGPT
connector guidance, not Codex execution authorization.

## Bounded Default Snapshot

The bounded default snapshot should match what Codex would read by default:

- `AGENTS.md`.
- The needed skill entry or reference guidance.
- The first 80-120 lines of a compact handoff or current-state file, when present.
- Current `TODO.md` sections: current phase, active task, blockers, next tasks, and
  do-not-do-yet.

Do not read full project history by default.

## On-Demand Reads

Use on-demand reads only when planning needs more context. Each read should name a concrete
file, heading, or section and record source refs.

Good examples:

- `PLAN.md#Phase 15`
- `docs/phases/phase_15_optional_chatgpt_mcp_planning_companion.md#Local Lifecycle Guidance`
- `DECISIONS.md#2026-06-19-optional-mcp-planning`

## Setup Card

The setup card helps ChatGPT select the intended local project:

```yaml
project_id: phase-workflow
workspace_id: desktop-phase-workflow
display_name: Phase Workflow Skill
workspace_root: C:\Users\Administrator\Desktop\phase-workflow
allowed_files:
  - AGENTS.md
  - TODO.md
  - SKILL.md
  - references/phase_policy.md
  - docs/phases/phase_15_optional_chatgpt_mcp_planning_companion.md
```

`workspace_root` stays in the local MCP registry. `allowed_files` is the explicit read
allowlist for MCP planning.
The setup card fields include `project_id`, `workspace_id`, `workspace_root`, and
`allowed_files`.

## Project Configuration And Local Registry

Explicit user request is required before creating or updating project MCP configuration or the
local registry. Project-local MCP config lives under `.phase-workflow/mcp/project.json`. The
project config stores `schema_version`, `project_id`, `display_name`, and `allowed_files`.
The project config must not store the local absolute `workspace_root`.

The local MCP registry lives at `~/.phase-workflow/mcp/registry.json`. The local registry
stores `project_id`, `workspace_id`, `workspace_root`, port, endpoint, and PID or lock
metadata. `project_id` is generated once for the project and stored in project config.
`workspace_id` is generated per local checkout and stored in the local registry. Missing or
ambiguous `project_id` or `workspace_id` fails closed. Configuration writes stay inside the
selected project and the documented local registry path.

## Handoff Prompt

ChatGPT should hand Codex a short copyable prompt, not a full transcript:

```text
phase_workflow_handoff: 1
project_id: phase-workflow
workspace_id: desktop-phase-workflow
mode: ChatGPT/MCP planning with Codex execution
source_refs:
  - TODO.md#Current Phase
  - TODO.md#Next Tasks
  - docs/phases/phase_15_optional_chatgpt_mcp_planning_companion.md#Local Lifecycle Guidance
snapshot_id: mcp-snapshot-2026-06-19T10-30-00
requested_action: Show the Phase 15.7 start gate.
stop_condition: Stop after the visible start gate and wait for separate user confirmation.
```

The handoff fields include `source_refs`, `snapshot_id`, `requested_action`, and
`stop_condition`.
The handoff is planning input only, not a source of truth or execution authorization.

Handoff recognition is header-based. Do not infer ChatGPT/MCP handoff mode from natural
language alone. Missing header means ordinary Codex-only conversation. A valid header includes
`phase_workflow_handoff: 1`, `mode: ChatGPT/MCP planning with Codex execution`, `project_id`,
`source_refs`, `snapshot_id`, `requested_action`, and `stop_condition`. `workspace_id` is
required when multiple local checkouts or ambiguity exist. Missing required fields, mismatched
project identity, missing source refs, unclear stop condition, or wrong `mode` fails closed
before execution. A valid handoff remains planning input only, not a source of truth or
execution authorization. Codex must revalidate local files, phase gates, authorization branch,
and stop condition before execution.

Direct conversation with Codex remains Codex-only. Codex must not route its own planning,
recovery reads, local validation, command execution, or file mutations through MCP. MCP is
only for ChatGPT-side planning reads. Codex may configure, start, check status, and stop the
local MCP companion after user confirmation, but service management does not make Codex
planning use MCP.

## Codex Execution Boundary

After receiving the handoff, Codex revalidates local files, phase gates, authorization branch,
and stop condition before execution. If the user later confirms execution, Codex executes only
the currently confirmed phase and stops at the next phase boundary.

Codex should not trust ChatGPT memory, missing source refs, or the copied handoff as
authorization to edit files.

## Local Lifecycle Boundary

The local companion lifecycle stays lightweight: start, status, and stop. Bind to loopback by
default, track the running process with a PID or lock file, report port conflicts explicitly,
and fail closed when `project_id` is missing, unknown, or ambiguous.

ChatGPT connects only after the local companion is already running. ChatGPT must not start
Codex, start the local companion, or execute project commands.

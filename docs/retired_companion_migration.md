# Retired Planning Companion Migration

The built-in ChatGPT/MCP planning companion is retired and unsupported. Current
`phase-workflow` installations use Codex-native conversation, direct local project reads,
phase gates, verification, and file-based recovery without that runtime.

## Upgrade An Older Installation

An overlay copy can leave files that were removed from the new skill version. Use a
deletion-aware synchronization method or remove the selected old skill installation and perform
a clean installation. Confirm the selected project and destination before deleting anything;
do not remove similarly named files from another workspace.

The current skill must not contain a `scripts/` package, `phase_mcp_*.py` files, dedicated MCP
runtime tests, or the old MCP planning example. Verify the resulting file inventory after the
upgrade.

## Old Running Processes And Registries

Repository retirement does not prove that an older installed copy has no running process. Do
not trust a shared registry PID by itself because process identifiers can be reused. Before any
later cleanup, verify the real process command line and the workspace it serves. Stop only the
process whose command line and workspace both identify the selected old installation.

If a shared registry still contains an entry, remove only the selected workspace entry after
the process and workspace identity have been verified. Do not rewrite or delete unrelated
entries.

## External Product State

ChatGPT Connector settings, Tunnel profiles, and tunnel-client state are user-owned external
state. Inspecting or changing them, stopping a process, or editing a shared registry is a
separate explicitly authorized task. This migration note provides a safety boundary only; the
repository retirement phase performs none of those external actions.

Do not replace the retired runtime with another service, transport, connector protocol, or
local bridge. Generic conversation, reminder hooks, recovery, and handoff remain part of the
normal Codex workflow.

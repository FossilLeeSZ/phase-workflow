# Handoff Protocol Compatibility Redirect

This path remains only for compatibility with older installations and links.

## Compatibility Redirect

The single canonical recovery and context rule set is
[`references/recovery_protocol.md`](recovery_protocol.md). Follow that protocol for
same-conversation, compressed-context, no-chat, partial-execution, Context Gap, anchor,
end-of-round checkpoint, and authorization recovery behavior.

Handoff remains an optional, non-authoritative pointer index. Missing or stale handoff content
cannot override authoritative anchors, and a handoff cannot grant execution authorization.

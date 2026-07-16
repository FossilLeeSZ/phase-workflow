# Handoff Template

Template role: structural, not authoritative. Follow
[recovery protocol](../references/recovery_protocol.md) for the canonical recovery prompt,
owner files, and optional handoff behavior.

Handoff is optional and non-authoritative. Missing handoff is supported. This index points to
authoritative owner files; it must not copy current phase, status, output ledger, verification,
next action, or authorization facts. It cannot grant execution authorization.

## Authority Notice

This handoff is a pointer-only compatibility index. Validate every pointer against
`references/recovery_protocol.md` and the owner file. A stale or conflicting handoff becomes a
Context Gap and cannot override an authoritative anchor.

## Anchor Pointers

- TODO current state:
- Active phase note:
- Matching PLAN phase:
- Relevant decisions:
- Stable PROJECT_CONTEXT headings, when present:
- Latest verification record:

## Context Gaps

- Gap IDs and owner phase-note pointers only; do not copy detailed evidence.

## Recommended New Window Prompt

```text
Use the canonical new-window prompt from references/recovery_protocol.md and supply only the
project-specific anchor pointers and Context Gap IDs listed above.
```

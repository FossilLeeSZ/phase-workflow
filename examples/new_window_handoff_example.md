# New Window Handoff Example

This example shows how a new Codex window can recover context from files.

## Opening Prompt

```text
Use phase-workflow for this repository. Do not rely on previous chat history.
Read AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, DECISIONS.md, and the latest phase
note or handoff note. Summarize current phase, verified state, blockers, and next
recommended action before editing files.
```

## Expected Recovery Steps

1. Read `AGENTS.md` for repository rules.
2. Read `PLAN.md` for phase boundaries.
3. Read `TODO.md` for active and next tasks.
4. Read `DEV_LOG.md` for recent work and verification status.
5. Read `DECISIONS.md` for durable decisions.
6. Read the latest phase note or handoff note if present.

## Example Recovered State

```text
Current phase: Phase 1.
Verified state: Phase 0 completed with python -m pytest -q.
Active task: tighten SKILL.md and references.
Known blockers: none recorded.
Next action: update SKILL.md, then run documentation tests.
Do not do: add Web UI, database, complex CLI, cloud sync, or issue tracker integration.
```

The recovered state should come from files, not from memory. If two files
conflict, stop and resolve the conflict before editing.

## Example TODO Update

After recovery, the new window can update `TODO.md` only if the file-based
state is clear:

```markdown
## Current Phase

Phase 1: Tighten skill instructions and templates.

## Active Task

- [x] Recover current state from project files.
- [ ] Update SKILL.md resource navigation.
- [ ] Update template fields.
- [ ] Run final verification.

## Blocked

- None.
```

If the files are incomplete, do not invent missing history. Use a narrow TODO
instead:

```markdown
## Blocked

- Need clarification: `TODO.md` says Phase 2, but `DEV_LOG.md` has no Phase 1
  verification result.
```

## Important Rule

If the files do not explain a decision, do not invent chat history. Mark the point as unknown,
ask a focused question if it affects implementation, or record it as a TODO.

The new window should not continue from unstated assumptions. It should either
recover a coherent state from files or make the uncertainty visible before
changing behavior.

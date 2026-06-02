# New Window Handoff Example

This example shows how a new Codex window can recover context from files.

## Opening Prompt

```text
Use phase-workflow for this repository. Do not rely on previous chat history.
Read `AGENTS.md` first.
Read only the first 80-120 lines of the latest compact handoff or current-state file.
Read only the current phase, active task, blocked, and next task sections of `TODO.md`.
Use `rg` to inspect `PLAN.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, or phase notes only when
compact state is missing, conflicting, or explicitly requested.
Summarize current phase, verified state, blockers, and next recommended action before editing
files.
```

## Expected Recovery Steps

1. Read `AGENTS.md` for repository rules.
2. Read the first 80-120 lines of the latest compact handoff or current-state file.
3. Read only the current phase, active task, blocked, and next task sections of `TODO.md`.
4. Use `rg` or scoped section reads for `PLAN.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, and
   phase notes only when scope changes, conflicts, missing verification, unclear decision
   sources, or explicit history requests require them.

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

- Need clarification: `TODO.md` says Phase 2, but the Phase 1 phase note has no
  verification result.
```

Do not read full `PLAN.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, full `TODO.md`, full
handoff files, or full phase notes by default. Treat them as audit and policy history, then
look up exact sections only when the compact recovery files conflict or omit verification
context.

## Important Rule

If the files do not explain a decision, do not invent chat history. Mark the point as unknown,
ask a focused question if it affects implementation, or record it as a TODO.

The new window should not continue from unstated assumptions. It should either
recover a coherent state from files or make the uncertainty visible before
changing behavior.

# Handoff Protocol

Use this protocol to resume work without chat history and let a new Codex window continue from
project files.

## New Window Reading Order

Read compact recovery context first:

1. Read `AGENTS.md` first.
2. Read only the first 80-120 lines of the latest compact handoff or current-state file.
3. Read only the current phase, active task, blocked, and next task sections of `TODO.md`.

If a repository has additional local instructions, follow the highest-priority instructions first.

Do not read full `PLAN.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, `DEV_LOG.md`, full
`TODO.md`, or full handoff files by default. Treat `PLAN.md`, `DECISIONS.md`,
`PROJECT_CONTEXT.md`, full `TODO.md`, full handoff files, phase notes, and `DEV_LOG.md` as
targeted or on-demand recovery sources.

Use `rg` or scoped section reads for the heavier files. Use `rg` to inspect `PLAN.md`,
`DECISIONS.md`, `PROJECT_CONTEXT.md`, `DEV_LOG.md`, or phase notes only when compact state is
missing, conflicting, or explicitly requested. Read older entries only when scope changes,
conflicts, missing verification, unclear decision sources, or explicit history requests
require them.

Use a bounded DEV_LOG read when needed. `DEV_LOG.md` is a complete audit history and an
on-demand history source, not default full-file startup context.

## Summarize Current State

After reading the files, summarize:

- Current phase.
- Last completed phase.
- Active task.
- Files changed recently.
- Verification commands already run.
- Known issues or blockers.
- Next recommended action.

Do not assume prior chat context. If the files do not explain something, treat it as unknown.

## Determine The Next Step

Choose the next step by checking:

- The compact handoff or current-state file for current state, warnings, and non-goals.
- Current `TODO.md` sections for active and next tasks.
- Targeted `PLAN.md` phase matches when phase boundaries or scope changes are unclear.
- Targeted `DECISIONS.md` matches when durable constraints conflict or their source is unclear.
- Targeted phase note or `DEV_LOG.md` entries when recent verification needs confirmation.

If these files conflict, stop and clarify before implementing.

## End-Of-Round Records

Before ending a development round, update:

- `TODO.md`
- `DEV_LOG.md`
- Active phase note, if present
- Handoff note, if present
- `DECISIONS.md`, when a durable decision changed

Phase-exit and end-of-round record updates use the same bounded context rule. Do not read full
`PLAN.md`, `TODO.md`, `DEV_LOG.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, full handoff files,
or full phase notes just to update status records. For `TODO.md`, read and update only the
current phase, active task, blocked, and next task sections. For `DEV_LOG.md`, prepend or
append the new entry without reading the full audit history; read only the latest 1-3 entries
when needed for continuity. For `PLAN.md`, use `rg` or heading-scoped reads to locate the
relevant phase only when phase boundaries, scope, or roadmap entries change. For
`PROJECT_CONTEXT.md`, use scoped reads around the summary, constraints, or current-state
heading being updated. For handoff and phase notes, read only the relevant heading or the
first 80-120 lines unless a conflict requires more context.

Records that claim completion or test status must include actual verification commands and
results. Records that do not claim completion or test status may record blocker, unfinished,
handoff, or current-state status without a fresh verification command. If verification has not
run, record that status honestly.

A status/handoff-record mutation requires current phase execution or phase exit context. It
can update `TODO.md`, `DEV_LOG.md`, phase notes, handoff notes, and `DECISIONS.md` when
recording a durable decision already made inside the authorized phase or phase exit context.
It must record actual verification results when claiming completion or test status. If
verification has not run, record that status honestly and do not claim completion or passing
tests. It can update blocker, unfinished status, handoff, or current-state records without a
fresh verification command when no completion or test status is claimed. It does not authorize
plan changes, new strategy decisions, technical implementation, or recovery repair.

Status/handoff-record mutation checks:

- Is the update reporting current phase execution, verification, blocker, unfinished status,
  handoff, or current-state status?
- Is it limited to `TODO.md`, `DEV_LOG.md`, phase notes, handoff notes, or a narrow
  `DECISIONS.md` update?
- Is any `DECISIONS.md` update limited to recording a durable decision already made inside the
  authorized phase or phase exit context?
- Are actual verification results recorded when completion or test status is claimed?
- If verification has not run, does the record say so without claiming completion or passing
  tests?
- Does it avoid plan changes, technical implementation, and recovery repair?

## Avoiding Chat-History Dependency

- Do not write "as discussed above" without restating the decision.
- Do not leave the only copy of a decision in chat.
- Do not mark work complete without recording how it was verified.
- Do not rely on memory for next steps.

## Recommended New Window Prompt

```text
Use phase-workflow for this repository. Do not rely on previous chat history.
Read `AGENTS.md` first.
Read only the first 80-120 lines of the latest compact handoff or current-state file.
Read only the current phase, active task, blocked, and next task sections of `TODO.md`.
Use `rg` to inspect `PLAN.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, `DEV_LOG.md`, or phase
notes only when compact state is missing, conflicting, or explicitly requested.
Summarize the current phase, verified state, blockers, and next recommended action before
editing files.
```

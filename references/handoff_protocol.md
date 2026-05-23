# Handoff Protocol

Use this protocol to resume work without chat history and let a new Codex window continue from
project files.

## New Window Reading Order

Read compact recovery context first:

1. `AGENTS.md`
2. `PLAN.md`
3. `TODO.md`
4. `DECISIONS.md`
5. Latest handoff note or phase note
6. Latest 1-3 `DEV_LOG.md` entries only if recent verification or conflict context is needed

If a repository has additional local instructions, follow the highest-priority instructions first.

Use a bounded DEV_LOG read by default. `DEV_LOG.md` is a complete audit history and an
on-demand history source, not default full-file startup context. Read older entries only when
compact state files conflict, verification results are missing, a decision source is unclear, or
the user explicitly asks for historical detail.

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

- `TODO.md` for active and next tasks.
- `PLAN.md` for phase boundaries.
- `DECISIONS.md` for durable constraints.
- Latest handoff note or phase note for current state, warnings, and non-goals.
- Latest 1-3 `DEV_LOG.md` entries when recent verification needs confirmation.

If these files conflict, stop and clarify before implementing.

## End-Of-Round Records

Before ending a development round, update:

- `TODO.md`
- `DEV_LOG.md`
- Active phase note, if present
- Handoff note, if present
- `DECISIONS.md`, when a durable decision changed

The records should include actual verification commands and results.

## Avoiding Chat-History Dependency

- Do not write "as discussed above" without restating the decision.
- Do not leave the only copy of a decision in chat.
- Do not mark work complete without recording how it was verified.
- Do not rely on memory for next steps.

## Recommended New Window Prompt

```text
Use phase-workflow for this repository. Do not rely on previous chat history.
Read AGENTS.md, PLAN.md, TODO.md, DECISIONS.md, and the latest handoff note or phase note.
Read only the latest 1-3 DEV_LOG.md entries if recent verification or conflicts need context.
Summarize the current phase, verified state, blockers, and next recommended action before
editing files.
```

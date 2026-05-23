# Handoff Protocol

Use this protocol to resume work without chat history and let a new Codex window continue from
project files.

## New Window Reading Order

Read these files first:

1. `AGENTS.md`
2. `PLAN.md`
3. `TODO.md`
4. `DEV_LOG.md`
5. `DECISIONS.md`
6. Latest phase note or handoff note

If a repository has additional local instructions, follow the highest-priority instructions first.

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
- `DEV_LOG.md` for the latest verified state.
- `DECISIONS.md` for durable constraints.
- Latest handoff note for warnings and non-goals.

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
Read AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, DECISIONS.md, and the latest phase
note or handoff note. Summarize the current phase, verified state, blockers, and
next recommended action before editing files.
```

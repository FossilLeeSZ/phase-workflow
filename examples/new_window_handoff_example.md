# New Window Handoff Example

Example role: illustrative, not authoritative. Follow the
[recovery protocol](../references/recovery_protocol.md) for anchor ownership and Context Gaps,
and the [phase policy](../references/phase_policy.md#authorization-and-recovery-state-machine)
for the resulting authorization state.

## Scenario

A new Codex task opens after prior conversation was compressed or is unavailable. `TODO.md`
points to the exact Phase 2 note and matching PLAN section. The note records one remaining output
and a blocking `GAP-2-03`: the required escaped-delimiter behavior is ambiguous. An optional
handoff may be missing, stale, or present only as a pointer index.

## Opening Prompt

```text
Use phase-workflow for this project. Read AGENTS.md and open the current SKILL.md.
Follow references/recovery_protocol.md.
Use relevant available conversation when present, but do not invent unavailable history or
treat imported chat, a compressed summary, or old confirmation as authorization.
Follow TODO's exact active phase-note and PLAN pointers, read only referenced decisions and
stable project-context headings, and compare factual claims with repository evidence.
List Context Gaps. If a blocking gap remains, enter CONTEXT_BLOCKED and stop. Otherwise show the
required revalidation gate and wait for a new live confirmation before mutation.
Desired response language: Chinese for this task.
```

## Expected Recovery Steps

1. Read repository instructions and the current skill.
2. Use relevant available conversation as current-intent context.
3. Read TODO's compact current sections and follow its exact active-note pointer.
4. Read the matching PLAN section and compare the phase-contract revision.
5. Read only TODO-referenced decisions and stable project-context headings.
6. Compare the anchors with actual files, tests, artifacts, and recorded verification.
7. Record each Context Gap in the active phase note and mirror only blocking IDs in TODO.
8. Apply materiality: a gap affecting outputs, acceptance, approach, or safety blocks mutation.
9. Choose the state from current evidence; do not reconstruct an old authorization transition.

## Example Recovered State

- Current intent source: current request and relevant available conversation.
- Compact current state owner: `TODO.md`.
- Phase contract owner: the TODO-linked PLAN section.
- Detailed execution owner: the exact TODO-linked active phase note.
- Actual state owner: repository evidence.
- Remaining output: escaped-delimiter behavior.
- Blocking Context Gap: `GAP-2-03`, because the expected delimiter semantics affect output and
  acceptance.
- Authorization state: `CONTEXT_BLOCKED`.
- Allowed mutation: none.

## Example TODO Update

```markdown
## Current Phase

Phase 2: Parser Edge Cases.

## Compact Status

Two declared outputs are verified. The remaining escaped-delimiter output is blocked by
GAP-2-03.

## Active Task

- [ ] Resolve GAP-2-03 before resuming the remaining output.

## Next Action

Resolve or clarify GAP-2-03 against the Phase 2 contract and user intent.

## Blocked

- GAP-2-03

## Context Anchors

- PLAN phase: `PLAN.md` -> `## Phase 2: Parser Edge Cases`
- Active phase note: `docs/phases/phase_2_parser_edge_cases.md` -> `# Phase 2 Parser Edge Cases`
- Relevant decisions: `DECISIONS.md` -> `## D-0004: Preserve Escape Semantics`
- Stable project context: `PROJECT_CONTEXT.md` -> `## Stable Verification Entry Points`
- Latest verification: `docs/phases/phase_2_parser_edge_cases.md` -> `## Latest Verification`

## Do Not Do Yet

- Do not mutate the remaining parser output while GAP-2-03 is blocking.
- Do not start Phase 3 or repeat the two verified outputs.
```

Detailed evidence for `GAP-2-03` remains only in the active phase note. TODO mirrors the blocking
ID and compact consequence, not the evidence ledger.

## Missing Or Stale Handoff

Missing handoff is a supported normal path. If an optional handoff exists, validate only its
pointers and Context Gap IDs against TODO and the owner files. A stale or conflicting handoff is
itself a Context Gap and cannot override current owners or repository evidence.

## Important Rule

Only after all blocking Context Gaps are resolved may recovery enter a visible revalidation gate
and `AWAITING_LIVE_CONFIRMATION`. The gate must then stop and wait for a new live confirmation.

A handoff, TODO, phase note, imported chat, compressed summary, old confirmation, or file saying
`confirmed` may describe prior work but cannot grant execution authorization. Recovery either
remains `CONTEXT_BLOCKED` or ends at the applicable gate; it never reconstructs permission.

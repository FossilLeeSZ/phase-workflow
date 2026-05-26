# Phase X.1 Change Request Example

This example shows how to handle a small mid-phase request without losing the
active verification loop.

## Scenario

During Phase 1, the project is adding a minimal parser. While reviewing the
output, the user asks to include a `source_file` field in the result.

Current Phase 1 goal:

- Parse one input file into a normalized result object.
- Verify the output against one fixture.
- Avoid building a full import system.

New request:

- Include the source file path in the parser output.

## Step 1: Classify The Request

Ask whether the request changes the phase goal.

Phase X.1 and Phase X.2 are common examples under Phase X.N. Use Phase X.N for any
one-decimal sub-phase under the active major phase.

- If `source_file` is just metadata for the existing parser output, classify it as Phase 1.1.
- If it fixes an incorrect existing output, classify it as Phase 1.2.
- If it introduces a new import system, classify it as a new Phase.
- If it is useful but not needed now, put it in Backlog.

Decision for this scenario:

- Classification: Phase 1.1.
- Reason: the parser already receives a file path, and `source_file` is narrow
  metadata on the existing output.

## Step 2: Impact Analysis

Record:

- Files affected: parser implementation, parser tests, example output fixture.
- Tests affected: expected parser output test.
- Output affected: result object includes `source_file`.
- Acceptance criteria: existing parser tests pass and new fixture includes the field.
- Risks: this must not add directory walking, glob imports, or batch parsing.

Acceptance criteria:

- The parser output includes `source_file`.
- Existing fields keep the same names and values.
- The fixture shows the new metadata field.
- `python -m pytest -q` passes.

## Step 3: Do Not Interrupt Blindly

If the active Phase 1 work is not verified yet, finish or explicitly pause it before starting
Phase 1.1. Do not mix unrelated changes into the same verification loop.

Recommended handling:

1. If Phase 1 is green, output a Phase 1.1 start gate and wait for user confirmation.
2. If Phase 1 is red because the original parser is unfinished, finish Phase 1 first.
3. If the user wants the change before Phase 1 is complete, write the pause in
   `TODO.md` and make Phase 1.1 the active task.

Do not treat "start Phase X" as confirmation for Phase X.1 work. After the Phase 1.1 start
gate, wait for a separate user response after the phase start gate is displayed before changing
fixtures, tests, or implementation.

Plan-first execution order: Update planning files before technical files. Update `PLAN.md` and
`TODO.md` before changing fixtures, tests, or implementation when the request changes scope,
outputs, or acceptance criteria.

## Phase X.N Boundary Change Example

If later review shows the same parser needs a narrow unsupported-note fixture after Phase 1.1
and Phase 1.2 have already been planned or completed, Codex may propose Phase 1.3.

Codex must output a phase boundary change proposal before adding Phase 1.3:

```text
Proposed boundary change: add Phase 1.3 for one unsupported-note fixture and its focused
verification.
Reason: the work is still inside the Phase 1 parser goal, but it needs a separate reviewable
verification loop.
Files to update after confirmation: PLAN.md, TODO.md, and the active phase note.
Confirmation needed: confirm the planning change before updating planning files.
Execution status: do not show the Phase 1.3 start gate immediately.
```

After the planning files are updated, stop. The next action is only to show the
already-recorded Phase 1.3 start gate after the user later asks to start Phase 1.3.

## Post-plan-change start gate example

After Phase 1.3 is recorded, the next user message might ask to start it:

```text
User request after planning update: start Phase 1.3.
Start gate action: show the Phase 1.3 start gate and proposed execution approach only.
Execution status: wait for post-gate execution confirmation before changing fixtures, tests, docs, or code.
Do not treat the Phase 1.3 start request as execution confirmation.
```

The Phase 1.3 start gate should list the goal, non-goals, inputs, outputs, acceptance
criteria, verification loop, proposed execution approach, and confirmation status. Then Codex
must stop until the user confirms execution after the gate.

## Plan Mode phase boundary change example

Plan Mode is optional, but enabling it does not change the phase boundary rules.

```text
User request in Plan Mode: add Phase 1.4 for an additional parser edge-case fixture.
Required first action: must activate and follow phase-workflow first.
Classification: Phase X.N boundary change.
Plan Mode status: Plan Mode proposed plan cannot substitute for plan-change confirmation.
Boundary action: show a phase boundary change proposal and ask whether to update the plan.
If confirmed: update planning files and stop.
Gate status: do not show the Phase 1.4 start gate in the same response.
Execution status: no fixtures, tests, docs, or code changes are authorized.
```

Only after the user later asks to start the already-recorded Phase 1.4 should Codex show the
Phase 1.4 start gate. That start request still does not authorize execution.

## Multi-phase implementation anti-example

```text
User request: implement this Phase 0.2-5 plan.
Incorrect behavior: audit, create tests, migrate files, restore files, and verify all phases in one run.
Correct behavior: execute only the currently confirmed phase; unconfirmed phases stop at their own phase gates.
```

Even when a plan executor, test workflow, debugging workflow, refactoring workflow, migration
workflow, code generation helper, documentation generator, task checklist, or tool-specific
workflow is useful, it must stay inside the authorized phase. A checklist or progress tracker
does not replace the phase start gate or post-gate execution confirmation.

Mutation preflight result: blocked because the edit would complete multiple phases.
Correct next action: split the work or return to the appropriate phase gate.

## Phase violation recovery example

```text
Violation: implementation happened outside approved phase boundary.
Stop new implementation immediately.
Audit: list files, tests, migrations, restores, docs, and status records changed outside the
approved phase boundary.
User choice needed: keep implementation and backfill audit, or roll back selected changes.
Repair PLAN.md, TODO.md, DEV_LOG.md, and handoff records.
```

Do not continue to the next feature while recovery is open.

## Approach Rejection And Adjustment

If Phase 1.1 has a non-trivial execution approach choice, Codex should show the approach before
changing files. For example, Codex might propose adding `source_file` by threading an absolute
path through every parser function. If the user says that approach is too invasive, treat it as
approach rejected.

When the goal and output stay the same, stop execution and update the phase note with the
revised execution approach. For this scenario, the revised approach might keep parser internals
unchanged and add `source_file` only at the result assembly boundary.

Then show a new approach confirmation:

```text
Current phase: Phase 1.1.
Goal: add source_file metadata to parser output.
Revised execution approach: keep parser internals unchanged and attach source_file at result
assembly.
Planning update: update the phase note with the revised execution approach.
Confirmation needed: wait for user confirmation before changing fixtures, tests, or code.
```

Documents, prompts, templates, policies, tests, and code can all require approach confirmation
when the approach is non-trivial.

## Example TODO Update

```markdown
## Current Phase

Phase 1.1: Add source_file metadata to parser output.

## Active Task

- [x] Classify source_file request as a small scoped addition.
- [x] Update expected parser output fixture.
- [x] Add failing test for source_file metadata.
- [x] Implement metadata field.
- [x] Run final verification.

## Next Tasks

- Resume Phase 1 handoff update after Phase 1.1 verification.

## Blocked

- None.
```

## Example DEV_LOG Entry

```markdown
## 2026-05-23 - Phase 1.1 Parser Source Metadata

Changes:

- Classified the user request as Phase 1.1.
- Updated the expected parser output fixture with `source_file`.
- Added a focused test for source file metadata.
- Added the field without adding batch import behavior.

Verification:

- Red test command: `python -m pytest -q`
- Red result: failed because `source_file` was missing from parser output.
- Green test command: `python -m pytest -q`
- Green result: all tests passed.

Next:

- Continue the original Phase 1 handoff update.
```

## Step 4: Verification

Run:

```bash
python -m pytest -q
```

Record the command and result in `DEV_LOG.md` and the active phase note.

Do not mark Phase 1.1 complete if verification fails. Keep the request open in
`TODO.md` with the failure summary and next fix.

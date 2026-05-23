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

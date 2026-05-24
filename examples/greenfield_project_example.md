# Greenfield Project Example

This example shows how to use `phase-workflow` to start a small MVP project
without relying on chat history.

## Scenario

A user wants to create a new command-line helper that reads a plain text note and
returns a short list of action items. The project is still greenfield, so the
first goal is not to build the whole helper. The first goal is to create a
recoverable project baseline and then implement one narrow behavior.

## Before Phase 0: Chat-to-Codex Handoff

Before Codex edits the target project, use Chat to brainstorm the project goal,
MVP boundary, non-goals, constraints, and success criteria. Chat should then
generate a Codex startup prompt that carries those decisions into the project
folder.

Codex should use the prompt to draft a rough phase plan, check whether Phase 0
should stay whole or split, and wait for the user to confirm Phase 0 before
creating files.

## Example Startup Prompt

```text
Use phase-workflow for this new project.

Brainstorm summary:
- Goal: create a small command-line helper that reads a plain text note and
  returns a short list of action items.
- MVP boundary: support one basic note format first.
- Non-goals: no database, no cloud sync, no full CLI framework, no deployment.
- Success criteria: Phase 0 creates recoverable project files and minimal tests;
  Phase 1 implements one fixture-backed extraction behavior.

First, create a rough phase plan and decide whether Phase 0 is one verification
loop or needs to split. Report the proposed boundary and wait for me to confirm
Phase 0 before creating or editing files.
```

## Phase 0 Start Gate In An Empty Folder

When the target project is an empty folder, Codex should output a visible Phase 0 start gate
before creating any project files.

Example Phase 0 start gate:

```text
Current phase: Phase 0.
Folder state: empty folder.
Goal: create recoverable baseline workflow files and minimal verification.
Baseline workflow files: README.md, AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, and DECISIONS.md.
Split decision: do not split; Phase 0 is one initialization and verification loop.
Verification command: python -m pytest -q.
Confirmation needed: wait for user confirmation before creating any project files.
After this gate: stop after reporting the phase start gate and wait for a separate user
response after the phase start gate is displayed.
```

## Phase 0: Initialize The Project

Goal:

- Create a small repository skeleton.
- Add `README.md`, `AGENTS.md`, `PLAN.md`, `TODO.md`, `DEV_LOG.md`, and `DECISIONS.md`.
- Add initial tests that check the expected project structure.
- Record the first planned capability in `PLAN.md` without implementing it.

Non-goals:

- Do not build product features yet.
- Do not add deployment, database, or cloud integrations.
- Do not add a full CLI framework before the first behavior exists.

Example files:

```text
README.md
AGENTS.md
PLAN.md
TODO.md
DEV_LOG.md
DECISIONS.md
tests/test_project_docs.py
```

Verification:

```bash
python -m pytest -q
```

Handoff:

- Record what files exist.
- Record the test command and result.
- Record Phase 1 as the next step.
- Record the non-goals so the next session does not expand scope.

## Phase 1: First Minimal Capability

Before creating fixtures, tests, or implementation changes, Codex should output a visible phase
start gate and wait for user confirmation.

Plan-first execution order: Update planning files before technical files. Update `PLAN.md` and
`TODO.md` before changing fixtures, tests, or implementation when Phase 1 scope, outputs, or
acceptance criteria change.
Rule wording: Update `PLAN.md` and `TODO.md` before changing fixtures, tests, or implementation.

Example phase start gate:

```text
Current phase: Phase 1.
Goal: implement one fixture-backed action extraction behavior.
Non-goals: no full CLI framework, no database, no cloud sync, no extra parsing modes.
Split decision: do not split; Phase 1 is one user-visible behavior and one verification loop.
Change request classification options remain Phase X.1, Phase X.2, New Major Phase, or Backlog.
Verification loop: fixture, failing test, minimal parser, python -m pytest -q.
Confirmation needed: wait for user confirmation before creating fixtures, tests, or
implementation changes.
After this gate: stop after reporting the phase start gate and wait for a separate user
response after the phase start gate is displayed.
```

## Reviewability split example

If the user says Phase 1 feels too large or too opaque, Codex should treat that as a valid
split reason even if the work still targets one user-visible capability.

Example split interpretation gate:

```text
Split reason: reviewability, transparency, and avoiding opaque large phases.
Interpretation: split Phase 1 into Phase 1.1 for fixtures and tests, then Phase 1.2 for the
minimal parser implementation and verification.
Files to update after confirmation: PLAN.md, TODO.md, and the active phase note.
Confirmation needed: confirm the split before updating planning files.
Execution status: do not execute Phase X.1 immediately.
```

After the user confirms the split, update the planning files and stop. The next Codex action
should be a separate Phase 1.1 start gate, not fixtures, tests, or implementation.

Rule wording: documents, prompts, templates, policies, tests, and code can all require approach confirmation
when the execution approach is non-trivial.

Goal:

- Define one narrow user-visible capability.
- Prepare fixtures/examples that describe expected behavior.
- Write failing tests against those fixtures.
- Implement only the minimal code needed for the tests to pass.
- Update project records after verification.

Example flow:

1. Add `examples/basic_note.txt` with one realistic input note.
2. Add `examples/basic_actions.json` with the expected action items.
3. Add `tests/test_extract_actions.py` that compares actual output to the fixture.
4. Run `python -m pytest -q` and confirm the test fails for the expected reason.
5. Implement the smallest parser function that passes the fixture test.
6. Run `python -m pytest -q` again.
7. Update `TODO.md`, `DEV_LOG.md`, and the handoff note.

Acceptance criteria:

- The fixture documents the first supported input shape.
- The test fails before implementation and passes after implementation.
- No extra parsing modes, configuration files, or integrations are added.
- The next task is recoverable from project files.

## Example TODO State

```markdown
## Current Phase

Phase 1: First minimal action extraction.

## Active Task

- [x] Add basic note fixture.
- [x] Add expected action output fixture.
- [x] Add failing extraction test.
- [x] Implement minimal extraction behavior.
- [x] Run final verification.

## Next Tasks

- Phase 2: Add one more input fixture only after a real unsupported note appears.

## Blocked

- None.
```

## Example DEV_LOG Entry

```markdown
## 2026-05-23 - Phase 1 Minimal Action Extraction

Changes:

- Added a basic note input fixture.
- Added the expected action output fixture.
- Added a fixture-based extraction test.
- Implemented the smallest extraction behavior needed for the fixture.

Verification:

- Red test command: `python -m pytest -q`
- Red result: failed because extraction behavior was not implemented.
- Green test command: `python -m pytest -q`
- Green result: all tests passed.

Next:

- Wait for a concrete unsupported note before expanding examples.
```

## Handoff At The End

The handoff note should say:

- Current phase and status.
- What was verified.
- What files changed.
- What not to do yet.
- Next recommended task.
- The exact prompt a new Codex window should use to recover context.

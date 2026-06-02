# Existing Structured Project Adoption Example

This example shows how to adopt `phase-workflow` into an existing project with a clear
structure. It does not show code cleanup, feature work, or a roadmap inferred from code.

## Scenario

The target project already has:

- `README.md`
- `pyproject.toml`
- `src/`
- `tests/`

It does not yet have `AGENTS.md`, `PLAN.md`, `TODO.md`, `DECISIONS.md`, or
`PROJECT_CONTEXT.md`.

## Folder State Classification

Codex may classify the folder as:

```text
Folder state: existing structured project candidate.
Evidence: README.md, pyproject.toml, src/, and tests/ are present.
Detected verification command: python -m pytest -q.
Recommendation: use Phase 0.1 to adopt workflow files around the current project state.
Execution status: not authorized until the user confirms after this gate.
```

If the main entrypoint, test command, or current goal cannot be identified, Codex should report
`unclear project state` and stop instead of creating workflow files.

## Phase 0.1 Adoption Start Gate

```text
Current phase: Phase 0.1.
Folder state: existing structured project candidate.
Goal: adopt phase-workflow around the current project state.
Detected existing files: README.md, pyproject.toml, src/, tests/.
Detected test/build/smoke command: python -m pytest -q.
Files to create or fill: AGENTS.md, PLAN.md, TODO.md, DECISIONS.md, PROJECT_CONTEXT.md, and a
handoff note.
Files not to overwrite: README.md, pyproject.toml, source files, test files, and existing
project documentation.
Non-goals: no feature work, no refactor, no cleanup campaign, no roadmap.
Confirmation status: wait for separate user confirmation.
```

After this gate, Codex must stop. User confirmation is required before creating files.

## PROJECT_CONTEXT.md

`PROJECT_CONTEXT.md` should summarize the current project for future Codex sessions:

````markdown
# PROJECT_CONTEXT.md

## What This Project Is

A small Python package that extracts action items from plain text notes.

## Current User-Visible Purpose

Parse one supported note format and return structured action items.

## Important Directories

- `src/`: package code.
- `tests/`: pytest coverage.

## Verification Commands

```bash
python -m pytest -q
```

## Current Known Constraints

Keep the parser behavior fixture-backed and avoid broad format support until requested.

## Do Not Change Casually

Do not rename package modules, change public parser output fields, or replace the test runner
without user confirmation.

## Workflow Adoption Status

Phase 0.1 adopted `phase-workflow` without modifying application code.

## Next Planning Step

Ask the user whether to start Phase 0.2 and provide or confirm the next project goal.
````

## Phase 0.2 Planning Start Gate

Phase 0.2 is separate from Phase 0.1. It starts only after the user asks for planning and then
confirms the Phase 0.2 gate.

Plan-first execution order: Update planning files before technical files. Update `PLAN.md` and
`TODO.md` before changing fixtures, tests, or implementation when the planning baseline changes
phase scope.

```text
Current phase: Phase 0.2.
Inputs: PROJECT_CONTEXT.md and user-confirmed next project goal.
Goal: create a rough planning baseline for future phase work.
Files to update: PLAN.md, TODO.md, phase note, and handoff note.
Non-goals: no code changes, no audit, no refactor planning unless explicitly requested.
Acceptance criteria: rough phase roadmap and candidate Phase 1 goal.
Confirmation status: wait for separate user confirmation.
```

## Confirmation Stops

- Phase 0.1 completion does not authorize Phase 0.2.
- Phase 0.2 completion does not authorize Phase 1.
- Every phase and sub-phase requires its own visible start gate and separate user confirmation.
- `Start Phase X` only asks Codex to show the gate; it is not execution confirmation.
- If Phase 0.2 uses a non-trivial roadmap structure, prompt strategy, policy wording, template
  field design, or test strategy, show the execution approach and wait for confirmation before
  updating planning files.

## Example TODO State

```markdown
## Current Phase

Phase 0.1: Existing structured project workflow adoption.

## Active Task

- [x] Classify folder state.
- [x] Create workflow files without overwriting existing project files.
- [x] Create PROJECT_CONTEXT.md.
- [x] Run python -m pytest -q.

## Next Tasks

- Ask the user whether to start Phase 0.2 planning baseline.
```

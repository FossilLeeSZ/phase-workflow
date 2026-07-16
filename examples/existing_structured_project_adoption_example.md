# Existing Structured Project Adoption Example

Example role: illustrative, not authoritative. Follow
[phase policy](../references/phase_policy.md) for adoption gates and
[recovery protocol](../references/recovery_protocol.md) for context ownership.

This example shows how to adopt `phase-workflow` into an existing codebase with a clear
structure when the user wants re-baselining from a zero-based project direction. It does not
show code cleanup, feature work, or a roadmap inferred from code.

For existing codebases, zero-based direction means redefining the project goal, boundaries,
phases, acceptance criteria, and complete delivery path around the user's current intent.

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

## Missing-Fact Handling

Inspect each adoption fact independently. Missing facts do not determine workflow applicability;
project maturity, project size, and team size are not rejection criteria.

| Item | Initial handling | Prohibited behavior | Blocking condition |
| --- | --- | --- | --- |
| Main entry point | Continue bounded read-only discovery; if unavailable, record a Context Gap | do not guess an entry point | Block only when the absence affects declared outputs, acceptance, approach, or safety |
| Test/build/smoke command | Discover configured commands; if unavailable, record that fact and define honest alternative verification | do not guess that tests exist or passed | Block only when the absence affects declared outputs, acceptance, approach, or safety |
| Current user goal | Use relevant conversation; if unavailable, record a Context Gap and keep factual adoption separate from later roadmap planning | do not guess a goal or roadmap | Block only when the absence affects declared outputs, acceptance, approach, or safety |
| Repository evidence | Inspect bounded files and observed commands; record unavailable evidence explicitly | do not guess capabilities or completion | Block only when the absence affects declared outputs, acceptance, approach, or safety |

Stop adoption only when a genuinely blocking boundary remains unclear. A missing current goal may
block the later Phase 0.2 planning contract without automatically blocking Phase 0.1's factual
assessment. A missing existing test command requires honest alternative verification; it does
not permit an invented pass claim.

## Phase 0.1 Adoption Start Gate

```text
Current phase: Phase 0.1.
Folder state: existing structured project candidate.
Goal: adopt phase-workflow around the current project state.
Detected existing files: README.md, pyproject.toml, src/, tests/.
Detected test/build/smoke command: python -m pytest -q.
Declared outputs: create or fill AGENTS.md, PLAN.md, TODO.md, DECISIONS.md,
PROJECT_CONTEXT.md, and the active Phase 0.1 note. Create a pointer-only handoff only if selected.
Files not to overwrite: README.md, pyproject.toml, source files, test files, and existing
project documentation.
Non-goals: no feature work, no refactor, no cleanup campaign, no roadmap.
Confirmation status: wait for separate live confirmation of these declared outputs.
```

After this gate, Codex must stop. User confirmation is required before creating files.

## PROJECT_CONTEXT.md

`PROJECT_CONTEXT.md` should preserve an evidence-backed stable project baseline. Follow
`references/recovery_protocol.md`; do not put current workflow state in this file:

````markdown
# PROJECT_CONTEXT.md

## System Identity

- Project: a small Python package that extracts action items from plain text notes.
- Existing-system type: maintained library with fixture-backed behavior.

## Factual Baseline

- Observed capability: parse one supported note format and return structured action items.
- Runtime: Python package with pytest coverage.

## Durable Constraints

- Keep parser behavior fixture-backed.
- Do not rename public output fields without a separately confirmed boundary.

## Important Directories

- `src/`: package code.
- `tests/`: pytest coverage.

## Stable Verification Entry Points

```bash
python -m pytest -q
```

## Evidence Sources

- `pyproject.toml`
- `src/`
- `tests/`
- observed `python -m pytest -q` result
````

The next gated action belongs only in `TODO.md`. The matching PLAN section owns the phase
boundary, and the active phase note owns detailed execution context. None belongs in the stable
`PROJECT_CONTEXT.md` baseline.

## Phase 0.2 Planning Start Gate

Phase 0.2 is separate from Phase 0.1. It starts only after the user asks for planning and then
confirms the Phase 0.2 gate.

Plan-first execution order: Update planning files before technical files. Update `PLAN.md` and
`TODO.md` before changing fixtures, tests, or implementation when the planning baseline changes
phase scope.

```text
Current phase: Phase 0.2.
Inputs: the factual PROJECT_CONTEXT.md baseline, the current user request and relevant available
conversation, and current code, test, build, or runtime evidence.
Goal: confirm the complete-project boundary, delivery conditions, capability dependencies, and a
phased path of real capabilities toward complete delivery.
Declared outputs: update PLAN.md, TODO.md, and the active phase note only. An optional handoff
may point to those owners but cannot duplicate their facts.
Non-goals: no code changes, no audit, no refactor planning unless explicitly requested.
Acceptance criteria: confirmed complete-project target and completion conditions, a
dependency-ordered delivery path, and a candidate Phase 1 real capability mapped to that path.
Confirmation status: wait for separate live confirmation of the planning-only declared outputs.
```

## Confirmation Stops

- Phase 0.1 completion does not authorize Phase 0.2.
- Phase 0.2 completion does not authorize Phase 1.
- This example stops after each scenario-specific output set. The general gate, approach, and
  declared-output rules remain in the linked phase policy rather than being duplicated here.

## Example TODO State

```markdown
## Current Phase

Phase 0.1: Existing structured project workflow adoption.

## Compact Status

Phase 0.1 outputs are verified. The next action is a separate Phase 0.2 gate request.

## Active Task

- [x] Classify folder state.
- [x] Create workflow files without overwriting existing project files.
- [x] Create PROJECT_CONTEXT.md.
- [x] Run python -m pytest -q.

## Next Action

Wait for the user to request the Phase 0.2 planning baseline gate.

## Blocked

- None.

## Context Anchors

- PLAN phase: `PLAN.md` -> `## Phase 0.1: Existing Structured Project Adoption`
- Active phase note: `docs/phases/phase_0_1_adoption.md` -> `# Phase 0.1 Adoption`
- Relevant decisions: none.
- Stable project context: `PROJECT_CONTEXT.md` -> `## System Identity`
- Latest verification: `docs/phases/phase_0_1_adoption.md` -> `## Latest Verification`

## Do Not Do Yet

- Do not start Phase 0.2 without its own gate and live confirmation.
```

# Greenfield Project Example

Example role: illustrative, not authoritative. Follow
[phase policy](../references/phase_policy.md),
[recovery protocol](../references/recovery_protocol.md), and
[verification policy](../references/verification_policy.md) for the governing contracts.

This example shows how to use `phase-workflow` to start a new project from a zero-based,
complete-project direction. It uses relevant available conversation while writing the durable
anchors needed for later sessions to continue without the full transcript.

## Scenario

A user wants to create a new command-line helper that reads a plain text note and returns a short
list of action items. The agreed complete-project target is a working local command that handles
the supported note format, returns useful output, reports invalid input honestly, and is verified
end to end. The target folder is empty, so Phase 0 creates a recoverable project baseline and
delivery path. Phase 1 then implements the first real capability on that path without redefining
the complete-project endpoint. Empty-folder state selects this bootstrap scenario; it does not
limit the eventual product capability.

## Before Phase 0: Chat-to-Codex Handoff

Before Codex edits the target project, use relevant available conversation to clarify the project
goal, project boundary, release boundary when useful, non-goals, constraints, and complete-system
success criteria. If that conversation is already available in the current Codex task, use it
directly as working context. If it is not available, provide a concise startup prompt that carries
the confirmed decisions without copying the full transcript.

Codex should use the prompt to draft a rough phase plan, check whether Phase 0
should stay whole or split, and wait for the user to confirm Phase 0 before
creating files.

## Example Startup Prompt

```text
Use phase-workflow for this new project.

Brainstorm summary:
- Complete-project target: deliver a working local command-line helper that reads a plain text
  note, returns a short list of action items, handles invalid input honestly, and is verified end
  to end.
- First release boundary: support one basic note format first.
- Non-goals: no database, no cloud sync, no full CLI framework, no deployment.
- Candidate delivery path: Phase 0 records the target and durable roadmap; the first real
  capability implements extraction for the agreed note format; a later real capability connects
  command input, output, and error handling; final verification proves the agreed command flow.
- Success criteria: every phase proves its declared real capability, and the project is complete
  only when the agreed command works end to end rather than when fixtures or tests exist alone.

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
Complete-project target: deliver the agreed working local note-to-actions command.
Goal: establish a recoverable and verifiable workflow baseline, record the complete delivery
path, and prove that every declared baseline path and required heading exists.
Declared output paths:
- README.md
- AGENTS.md
- PLAN.md
- TODO.md
- DECISIONS.md
- docs/phases/phase_0_initialize_project.md
- tests/test_project_docs.py
Test template source:
.agents/skills/phase-workflow/templates/test_project_docs_template.py
Verification evidence: run python -m pytest -q and record the command, date, exit status, and
result summary in the Phase 0 note at docs/phases/phase_0_initialize_project.md.
Product boundary: Phase 0 does not promise product runtime. Its real declared capability is a
recoverable workflow baseline whose files, anchors, and structure test are present and verified.
Split decision: do not split; Phase 0 is one initialization and verification loop.
Verification command: python -m pytest -q.
Confirmation needed: wait for user confirmation before creating any project files.
After this gate: stop after reporting the phase start gate and wait for a separate user
response after the phase start gate is displayed.
```

After the live confirmation, Phase 0 may create those missing declared outputs because
authorization follows the disclosed phase contract, not by file type. It may not create a
product feature, undisclosed script, or later-phase output.

Create `tests/test_project_docs.py` from the installed
`templates/test_project_docs_template.py`. The copied test reads the current phase and current
owner pointers from TODO and cross-checks PLAN and the active phase note. Do not hard-code the
Phase 0 identifier, PLAN heading, or Phase 0 note path; the same copied test must remain valid
when the canonical owners move to a later phase.

## Phase 0: Initialize The Project

Goal:

- Create the declared workflow baseline structure.
- Add `README.md`, `AGENTS.md`, `PLAN.md`, `TODO.md`, and `DECISIONS.md`.
- Add `docs/phases/phase_0_initialize_project.md` as the detailed Phase 0 execution and evidence
  record.
- Add the transition-stable project-document test that checks the current owner relationships.
- Record the complete-project target, completion conditions, capability dependencies, and first
  real capability in `PLAN.md` without implementing product behavior.

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
DECISIONS.md
docs/phases/phase_0_initialize_project.md
tests/test_project_docs.py
```

Verification:

```bash
python -m pytest -q
```

Owner record updates:

- Record created files, verification, and non-goals in the Phase 0 note.
- Record the compact next gated action and exact pointers in TODO.
- If an optional handoff is selected, store pointers only as shown later in this example.

## Phase 1: First Real Capability Slice

Before creating fixtures, tests, or implementation changes, Codex should output a visible phase
start gate and wait for user confirmation.

Plan-first execution order: Update planning files before technical files. Update `PLAN.md` and
`TODO.md` before changing fixtures, tests, or implementation when Phase 1 scope, outputs, or
acceptance criteria change.

Example phase start gate:

```text
Current phase: Phase 1.
Goal: implement one fixture-backed action extraction behavior.
Complete-delivery mapping: this real extraction behavior is required by the agreed command, but
the project is not complete until command input, output, error handling, and end-to-end verification
also satisfy the recorded target.
Non-goals: no full CLI framework, no database, no cloud sync, no extra parsing modes.
Split decision: do not split; Phase 1 is one user-visible behavior and one user-value loop or end-to-end capability loop.
Change requests: route any new boundary through references/change_request_policy.md rather than
classifying or allocating it inside this example.
Verification loop: fixture, failing test, action extractor behavior, python -m pytest -q.
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
Interpretation: do not split fixtures and tests from implementation. If the extraction boundary
contains two independently useful real behaviors, Phase 1.1 can implement and verify extraction
from a one-action note in the agreed format, then Phase 1.2 can implement and verify multiple-action
aggregation in that same format. If no honest real-capability split exists, keep Phase 1 whole and
use review checkpoints instead of hollow sub-phases. Do not create a fixtures-and-tests-only
sub-phase unless the declared product is explicitly a contract artifact.
Boundary route: use the canonical change-request policy to inspect recorded state, propose the
complete visible split, assign identifiers, and record Change Type separately.
Files to update after confirmation: PLAN.md, TODO.md, and the active phase note.
Confirmation needed: confirm the split before updating planning files.
Execution status: do not execute the newly assigned Phase X.N immediately; for this example,
do not execute Phase 1.1 immediately.
```

After the user confirms the split, update the planning files and stop. The next Codex action
should be a separate Phase 1.1 start gate, not fixtures, tests, or implementation.

Detailed split allocation and approach-revision behavior remain in the linked canonical
policies; this example only shows the concrete extraction capabilities.

Goal:

- Define one narrow user-visible capability.
- Prepare fixtures/examples that describe expected behavior.
- Write failing tests against those fixtures.
- Implement the real capability inside the declared phase boundary without adding extra modes.
- Update project records after verification.

Example flow:

1. Add `examples/basic_note.txt` with one realistic input note.
2. Add `examples/basic_actions.json` with the expected action items.
3. Add `tests/test_extract_actions.py` that compares actual output to the fixture.
4. Run `python -m pytest -q` and confirm the test fails for the expected reason.
5. Implement the parser behavior promised by the phase boundary and no extra parsing modes.
6. Run `python -m pytest -q` again.
7. Update compact current state and pointers in `TODO.md` and detailed execution evidence in the
   active phase note. Refresh a pointer-only handoff only if selected.

Acceptance criteria:

- The fixture documents the first supported input shape.
- The test fails before implementation and passes after implementation.
- No extra parsing modes, configuration files, or integrations are added.
- The next task and its boundaries are recoverable from durable anchors and repository evidence
  without requiring the full conversation transcript.

## Example TODO State

Follow `references/recovery_protocol.md`. TODO owns compact current state and exact pointers:

```markdown
## Current Phase

Phase 1: First real action extraction slice.

## Compact Status

The declared Phase 1 capability and verification are complete.

## Active Task

- [x] Complete and verify fixture-backed action extraction.

## Next Action

Wait for a concrete unsupported note, then show the next phase gate.

## Blocked

- None.

## Context Anchors

- PLAN phase: `PLAN.md` -> `## Phase 1: First Real Action Extraction Slice`
- Active phase note: `docs/phases/phase_1_action_extraction.md` -> `# Phase 1 Action Extraction`
- Relevant decisions: none.
- Stable project context: not present.
- Latest verification: `docs/phases/phase_1_action_extraction.md` -> `## Latest Verification`

## Do Not Do Yet

- Do not add another parsing mode without a separate phase boundary.
```

## Example Phase Note Entry

The active phase note owns the detailed execution and verification ledger:

```markdown
# Phase 1 Action Extraction

## Contract Revision

- phase-contract revision: 1
- Approach revision: 1

## Intent Summary

Complete one real fixture-backed action extraction capability without extra parsing modes.

## Output Ledger

- [x] Add the basic note input fixture.
- [x] Add the expected action output fixture.
- [x] Add the failing extraction test.
- [x] Implement and verify the declared extraction behavior.

## Modified Files

- `examples/basic_note.txt`
- `examples/basic_actions.json`
- `tests/test_extract_actions.py`
- `src/action_parser.py`

## Latest Verification

- Red: `python -m pytest -q`, failed because extraction was not implemented.
- Green: `python -m pytest -q`, all tests passed.

## Context Gaps

- None.

## Exit Conditions

- Freeze this note as Phase 1 history and stop before the next gate.
```

## Handoff At The End

Handoff is optional and non-authoritative. If selected, it should contain only:

- an authority notice;
- pointers to TODO, the exact active phase note, the matching PLAN phase, relevant decisions,
  stable project context, and latest verification;
- Context Gap IDs; and
- a new-window prompt that directs Codex to `references/recovery_protocol.md`.

It must not copy current phase, status, modified files, verification results, next action, or
authorization facts. Missing handoff is a supported normal path.

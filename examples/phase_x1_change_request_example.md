# Sequential Phase X.N Change Request Example

Example role: illustrative, not authoritative. Follow the
[change-request policy](../references/change_request_policy.md#phase-boundary-changes) for
classification, allocation, and planning updates; follow the
[phase policy](../references/phase_policy.md#live-confirmation-binding) for the later gate and
execution authorization; and follow the
[verification policy](../references/verification_policy.md) for completion evidence.

## Scenario

Phase 1 already delivers and verifies one concrete capability: parse one supported input file
into a normalized result object. During review, the user asks for that result to include a
`source_file` field.

Repository evidence shows no recorded direct sub-phase under Phase 1. Under the canonical
change-request policy, the bounded request is proposed as Phase 1.1 and records
`Change Type: addition` separately from its identifier. The example does not restate the
allocator or classification rules.

## Required Two-Confirmation Flow

This scenario has two distinct confirmations and a required stop between planning and the later
phase gate:

| Order | State | Allowed mutation | Must wait or stop |
| --- | --- | --- | --- |
| 1 | BOUNDARY_PROPOSAL | none | plan-change confirmation |
| 2 | PLAN_UPDATE_AUTHORIZED | PLAN.md, TODO.md, active phase note | stop after the planning update |
| 3 | GATE_READY -> AWAITING_LIVE_CONFIRMATION | none | separate live execution confirmation |
| 4 | EXECUTION_AUTHORIZED | declared Phase 1.1 outputs only | Phase 1.1 phase exit stop |

The first confirmation cannot authorize the gate or technical work. The later request to start
the now-recorded Phase 1.1 requests the visible gate only. Only the separate live execution
confirmation after that gate authorizes its declared outputs.

## Phase 1.1 Impact And Contract

- Reason: `source_file` is output metadata inside the supported single-file parse capability.
- Route and identifier: Phase 1.1, derived under the canonical change-request policy from the
  recorded repository state.
- Change Type: `addition`.
- Goal: include the source file path in the normalized parser result.
- Files likely affected: parser result assembly, parser tests, and the expected-output fixture.
- Declared outputs: an updated fixture, a failing metadata test, the bounded implementation, and
  verification evidence.
- Acceptance: `source_file` is present and accurate; existing fields retain their names and
  values; the full test suite passes.
- Non-goals: no directory walking, glob import, batch parsing, new import system, or unrelated
  parser refactor.
- Risk: threading paths through every parser function would be more invasive than attaching the
  field at result assembly.

## Boundary Proposal

Before any planning or technical mutation, show a proposal such as:

```text
Proposed boundary change: add Phase 1.1 for source_file metadata and its focused verification.
Recorded numbering state: Phase 1 has no recorded direct sub-phase; the canonical policy assigns
the next sequential identifier.
Change Type: addition.
Reason: the output contract changes, but the request remains inside the single-file parser goal.
Planning owners after confirmation: PLAN.md, TODO.md, and the active phase note.
Confirmation needed: confirm the planning change only.
Execution status: no gate, fixture, test, documentation, or implementation mutation is authorized.
```

If the user rejects or revises this boundary, remain read-only and update the proposal. Do not
turn a request to start Phase 1.1 into plan-change confirmation.

## Planning Update And Required Stop

After the user confirms the planning change, update only the three named planning owners:

- add the Phase 1.1 contract to `PLAN.md`;
- point `TODO.md` to Phase 1.1 and its exact anchors; and
- create or update the active Phase 1.1 note with the contract and proposed approach.

Then stop. Do not display the Phase 1.1 gate in the same response, and do not create the fixture,
test, documentation, or implementation output.

## Later Visible Gate

Only after a later user request to start the already-recorded Phase 1.1 should Codex display a
gate. The gate binds the Phase ID, contract and approach revisions, repository state, goal,
complete-delivery mapping, declared outputs, acceptance criteria, non-goals, risk, verification
loop, and stop condition.

The gate then stops in `AWAITING_LIVE_CONFIRMATION`. A start request, the completed planning
update, TODO text, or an old reply cannot substitute for the separate live execution
confirmation.

## Post-Gate Execution

After the later confirmation matches the displayed gate and mutation preflight passes:

1. Update the expected result fixture with `source_file`.
2. Add the focused test and run it to record the expected failure.
3. Attach `source_file` at result assembly without expanding the parser boundary.
4. Run the focused test and `python -m pytest -q`.
5. Record actual modified files and command results in the active phase note.
6. Update compact current state and pointers in `TODO.md`.
7. Stop at Phase 1.1 exit; do not resume Phase 1 or enter another phase automatically.

If the disclosed result-assembly approach materially changes, use the phase policy's
[approach-confirmation route](../references/phase_policy.md#approach-confirmation) and wait for
renewed confirmation. Do not copy that detailed lifecycle into this example.

## Verification

The active phase note records the actual RED and GREEN commands, exit statuses, result summaries,
deviations, and remaining gaps. `TODO.md` stores only compact current state and the pointer to
that evidence. A failing verification keeps Phase 1.1 open.

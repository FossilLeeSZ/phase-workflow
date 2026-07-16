# Change Request Policy

> Policy role: canonical owner for change classification, sequential Phase X.N allocation,
> Change Type, phase-boundary creation, and plan-change updates.
> `policy-owner: change-requests`

Use this policy to classify and contain scope changes when new requirements appear during an
active phase.

Use [phase policy](phase_policy.md) for gate and live-authorization outcomes,
[recovery protocol](recovery_protocol.md) for state ownership, and
[verification policy](verification_policy.md) for completion.

## Classification

Choose the route, identifier, and work type separately. The route is Phase X.N, New Major
Phase, or Backlog. A Phase X.N identifier expresses sequence only.

### Sequential Phase X.N Identifier

When the route is Phase X.N:

- Read the repository's durably recorded direct sub-phases under major Phase X.
- Treat every suffix N as a positive integer.
- If none exist, assign Phase X.1.
- Otherwise assign `max(existing N) + 1`.
- Count completed, cancelled, superseded, or abandoned identifiers as already used.
- Do not fill a gap or reuse an identifier.
- Do not let an occupied or otherwise conflicting chat-proposed number override repository
  state.
- Treat X.10 as the tenth sub-phase identifier, not as a decimal value.

## Change Type

Every Phase X.N change record must include `Change Type:` separately from its identifier. The
allowed values are:

- `addition`: adds a narrow clarification, missing piece, or compatible capability inside the
  recorded phase boundary.
- `bugfix`: fixes incorrect runtime behavior.
- `correction`: fixes incorrect policy, documentation, fixture, expectation, or other
  non-runtime behavior.
- `migration`: moves an existing capability, representation, dependency, or data shape to a
  new supported form.
- `documentation`: produces documentation as the declared product of the change.
- `other`: covers a type not represented above and requires a short explanation.

The type describes the work but never selects or changes the identifier. If the type changes
later, keep the recorded Phase X.N identifier. Record classification reasoning when the type
affects scope, verification, or rollout. A narrow addition and a blocking bugfix can each be
Phase X.1 if they are the first recorded sub-phase under different major phases; if the bugfix
is first and an addition follows it under the same major phase, they are Phase X.1 and Phase
X.2 respectively.

Example: adding a missing Context Gap field can be `Change Type: addition`; fixing a test that
checks the wrong required filename can be `Change Type: correction`. Their Phase X.N numbers
still come only from recorded sequence state.

### New Major Phase

Use a New Major Phase when the change:

- Adds an independent capability.
- Changes the workflow structure or project direction.
- Requires new examples, tests, acceptance criteria, or a separate verification loop.
- Would distract from the active phase.

Example: Add Markdown link linting after Phase 0 docs already exist.

### Backlog

Use Backlog when the change:

- Has possible future value.
- Is not needed for the current phase.
- Would expand the current project or release boundary or add operational complexity.

Example: Integrate with an issue tracker.

## Required Impact Analysis

Before implementing a change request, record the classification and impact analysis in planning
files. For scope-changing work, update planning files before technical files.

- Reason for the change.
- Route: Phase X.N, New Major Phase, or Backlog.
- Assigned identifier and the recorded numbering state used to derive it, when the route is
  Phase X.N.
- Change Type and classification reasoning. Record classification reasoning when the type
  affects scope, verification, or rollout.
- Files likely affected.
- Tests to add or update.
- Outputs that will change.
- Acceptance criteria.
- Risks or deferred work.

## Phase Boundary Changes

A change request that creates or changes a sub-phase is a phase boundary change. This includes
splits, any direct Phase X.N sub-phase, New Major Phase work, Backlog moves, and phase goal,
non-goal, acceptance criteria, or verification loop changes.

Any phase split is a phase boundary change, regardless of whether the split is requested by
the user or recommended by Codex. Use one split flow for both sources. When Codex recommends a
split, it must propose the complete currently visible sub-phase structure before asking for
confirmation. Starting after the highest already-recorded N, the proposal must assign the next
sequential Phase X.N identifiers to all known follow-up sub-phases and mark uncertain or
out-of-scope work as later phase work or Backlog. Do not create only one immediate next
sequential Phase X.N and route the user directly to its start gate.

Before adding Phase X.N, Codex must explain why it is needed, show a phase boundary change
proposal, and ask the user to confirm the planning change before updating planning files. If
the user confirms, update `PLAN.md`, `TODO.md`, and any relevant phase note, then stop. Do not
show the already-recorded Phase X.N start gate until a later user request.

Plan-change confirmation only authorizes planning-file updates, then stop. It does not
authorize tests, code, scripts, migrations, restores, or other technical files.

After the planning files are updated, the change request flow is complete. Do not continue
from a completed planning update into fixtures, tests, documents, prompts, templates,
policies, or code changes.

The later phase-start gate and live execution confirmation are owned by
[phase policy](phase_policy.md); this planning confirmation cannot substitute for either.

Use one sub-phase nesting level only; do not introduce Phase X.N.M. X.10 follows X.9 as an
integer sequence identifier.

## Plan Mode Change Requests

Plan Mode is optional. When enabled, use the current `SKILL.md` for activation and apply the
same classification and confirm-plan-update-stop flow. Authorization remains owned by
[phase policy](phase_policy.md).

## Handling During An Active Phase

- Do not let a change request silently interrupt the active phase.
- If the change is urgent and fixes incorrect runtime behavior, record `Change Type: bugfix`.
  If it needs a separate verification loop, assign the next sequential Phase X.N.
- If the change needs a separate goal, acceptance criteria, or verification loop, classify it
  as New Major Phase.
- If the change is useful but not blocking, record it in `TODO.md` or Backlog.
- If the change affects long-term workflow strategy, add a decision record to
  `DECISIONS.md`.
- Do not implement a New Major Phase until the plan is updated and the user confirms the new
  phase boundary.
- Do not treat `PLAN.md` or `TODO.md` as after-the-fact summaries for change requests.
- Prohibited order: Implement first, document plan later.

## Approach Override

Classify any scope-changing consequence here. The stop, revalidation, and renewed-confirmation
semantics for a material approach revision are owned by [phase policy](phase_policy.md).

## Completion Rule

A change request is complete only under [verification policy](verification_policy.md). Store
completion evidence through the owners defined by [recovery protocol](recovery_protocol.md).

# Change Request Policy

Use this policy to classify and contain scope changes when new requirements appear during an
active phase.

## Classification

`Phase X.1` and `Phase X.2` are common examples under the broader Phase X.N pattern. Phase
X.N means any one-decimal sub-phase under the current major phase.

### Phase X.1: Small Scoped Addition

Use Phase X.1 when the change:

- Supports the current phase goal.
- Adds a narrow clarification or missing piece.
- Does not change the acceptance criteria substantially.
- Can be verified with the current test approach.

Example: Add a missing "Known issues" field to a handoff template during a documentation phase.

### Phase X.2: Current Phase Bug Fix

Use Phase X.2 when the change:

- Fixes incorrect behavior or documentation in the current phase.
- Keeps the same goal and outputs.
- Prevents the current phase from exiting cleanly if ignored.

Example: Fix a test that checks the wrong required filename.

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
- Would expand the MVP or add operational complexity.

Example: Integrate with an issue tracker.

## Required Impact Analysis

Before implementing a change request, record the classification and impact analysis in planning
files. For scope-changing work, update planning files before technical files.

- Reason for the change.
- Classification: Phase X.N, New Major Phase, or Backlog. Use Phase X.1 and Phase X.2 as
  common examples when they fit.
- Files likely affected.
- Tests to add or update.
- Outputs that will change.
- Acceptance criteria.
- Risks or deferred work.

## Phase Boundary Changes

A change request that creates or changes a sub-phase is a phase boundary change. This includes
splits, any one-decimal Phase X.N sub-phase, New Major Phase work, Backlog moves, and phase
goal, non-goal, acceptance criteria, or verification loop changes.

Any phase split is a phase boundary change, regardless of whether the split is requested by
the user or recommended by Codex. Use one split flow for both sources. When Codex recommends a
split, it must propose the complete currently visible sub-phase structure before asking for
confirmation. The proposal must assign Phase X.1, Phase X.2, and later one-decimal numbers to
known follow-up sub-phases, and mark uncertain or out-of-scope work as later phase work or
Backlog. Do not create only the immediate next Phase X.1 and route the user directly to the
Phase X.1 start gate.

Before adding Phase X.N, Codex must explain why it is needed, show a phase boundary change
proposal, and ask the user to confirm the planning change before updating planning files. If
the user confirms, update `PLAN.md`, `TODO.md`, and any relevant phase note, then stop. Do not
show the already-recorded Phase X.N start gate until a later user request.

Plan-change confirmation only authorizes planning-file updates, then stop. It does not
authorize tests, code, scripts, migrations, restores, or other technical files.

After the planning files are updated, the change request flow is complete. Do not continue
from a completed planning update into fixtures, tests, documents, prompts, templates,
policies, or code changes.

After plan-change update, a later request to start, continue, enter, or execute that
already-recorded Phase X.N only authorizes the phase start gate. It does not authorize
execution. The start gate must stop before execution and wait for post-gate execution
confirmation.

Plan-change confirmation, phase start request, and post-gate execution confirmation cannot
substitute for each other.

Use one decimal level only; do not introduce Phase X.N.M.

## Plan Mode Change Requests

Plan Mode is optional. When Plan Mode is enabled for a task covered by this workflow, Codex
must activate and follow phase-workflow first.

Plan Mode cannot bypass phase-workflow activation, phase boundary change checks, or the
confirm-plan-update-stop flow. In Plan Mode, plan, phase, scope, or design-change requests
still require change request classification before returning a proposed plan.

Plan Mode proposed plan cannot substitute for plan-change confirmation, phase start request,
and post-gate execution confirmation. Plan Mode does not authorize execution.

## Handling During An Active Phase

- Do not let a change request silently interrupt the active phase.
- If the change is urgent and blocks verification, classify it as Phase X.2.
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

If the user rejects the proposed execution approach, stop execution. Do not keep editing
fixtures, tests, implementation, documents, prompts, templates, or policies under the rejected
approach.

If the goal and output stay the same, update `TODO.md` or the active phase note with the revised execution approach, then show the revised approach confirmation before continuing.

If acceptance criteria, outputs, risk, or the verification loop changes, handle the request as
scope-changing work: update `PLAN.md`, `TODO.md`, and any relevant phase note before technical
file changes.

Approach rejection does not automatically cancel the phase. It pauses execution until the
revised approach is recorded and confirmed.

## Completion Rule

A change request is not complete until its verification command has run and the result is
recorded in the phase note or `DEV_LOG.md`.

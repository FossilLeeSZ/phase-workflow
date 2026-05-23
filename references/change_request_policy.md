# Change Request Policy

Use this policy to classify and contain scope changes when new requirements appear during an
active phase.

## Classification

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

Before implementing a change request, record:

- Reason for the change.
- Classification: Phase X.1, Phase X.2, New Major Phase, or Backlog.
- Files likely affected.
- Tests to add or update.
- Outputs that will change.
- Acceptance criteria.
- Risks or deferred work.

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

## Completion Rule

A change request is not complete until its verification command has run and the result is
recorded in the phase note or `DEV_LOG.md`.

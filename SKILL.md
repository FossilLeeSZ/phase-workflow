---
name: phase-workflow
description: Use this skill for early-stage software projects that need phase-based planning, fixtures-first and tests-first implementation, scope control, change request tracking, verification, and handoff documents for continuing work across Codex sessions.
---

# phase-workflow

Use this skill to keep early-stage project work phase-based, testable, and recoverable across
Codex sessions.

## Resource Navigation

Load only the resource needed for the current decision:

- Read `references/phase_policy.md` when starting, exiting, renumbering, or splitting a phase.
- Read `references/change_request_policy.md` when a new request appears during an active phase.
- Read `references/handoff_protocol.md` when resuming work in a new window or ending a work round.
- Read `references/verification_policy.md` before marking a phase complete or reporting test status.
- Copy from `templates/` when creating phase notes, handoff notes, TODOs, dev log entries, or
  decision records in a target project.
- Use `examples/` only when the user needs a concrete pattern for a greenfield start, change
  request, or new-window handoff.

## When To Use This Skill

Use this skill when the user is working on:

- A new project.
- An MVP project.
- A Phase 0 initialization.
- A phase-based development plan.
- Scope control for a small or changing project.
- New-window handoff after prior Codex work.
- Mid-phase change request handling.
- Updates to `TODO.md`, `DEV_LOG.md`, `DECISIONS.md`, phase notes, or handoff documents.

## When Not To Use This Skill

Do not use this skill when:

- The user is only asking a simple question.
- The user explicitly asks for a direct small bug fix.
- The project is mature and already has a process the user does not want to change.
- The current task does not need long-term context management.
- The repository has higher-priority development instructions.

## Core Workflow

For each phase:

1. Lock phase scope.
2. Prepare fixtures/examples.
3. Write failing tests.
4. Implement the minimal capability.
5. Verify with actual commands.
6. Update phase notes and handoff.
7. Move to the next phase only after verification.

## Operating Rules

- Keep one phase focused on one closed loop.
- Before starting a major phase or sub-phase, output a visible phase start gate.
- The phase start gate must include the current phase, goal, non-goals, split decision,
  verification loop, and confirmation status.
- Before starting a major phase, report whether the scope is one single verification loop.
- A request to start a phase is not confirmation. It only authorizes phase analysis and the
  phase start gate.
- Rule wording: do not treat "start Phase X" as confirmation.
- Do not treat "start Phase X" as confirmation. Do not treat "begin Phase X", "continue
  Phase X", "进行 Phase X", or similar requests as execution confirmation either.
- Do not write `Confirmation status: received in your current request` unless the current
  message is a clear confirmation after the gate has already been shown.
- Always stop after reporting the phase start gate. Execution requires a separate user response
  after the phase start gate is displayed.
- If the user gives an ambiguous response, ask a short explicit confirmation question and do
  not edit files.
- If the target folder is an empty folder, treat Phase 0 initialization as gated work.
- Output a visible Phase 0 start gate before creating any project files.
- Do not create baseline workflow files before user confirmation. Baseline workflow files
  include README.md, AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, and DECISIONS.md.
- Split only when there are multiple independent outputs, unrelated user-visible capabilities,
  or separate verification loops.
- Do not split just because one coherent phase has multiple tasks.
- Do not automatically start the next phase; wait for explicit user confirmation.
- Do not create fixtures, tests, or implementation changes before user confirmation of the
  phase boundary.
- Prefer fixtures/examples before implementation.
- Prefer failing tests before changing behavior.
- Implement only the minimum capability needed for the active phase.
- Record scope changes before implementing them.
- Run actual verification commands before marking work complete.
- Update project files so the next Codex session can resume without chat history.
- Follow repository instructions when they are more specific than this skill.

## Phase Start Checklist

Before creating fixtures, tests, implementation changes, or any project files for Phase 0,
output a phase start gate and wait for user confirmation.

Identify:

- Current phase.
- Whether the previous phase is complete.
- Whether the target folder is an empty folder.
- Current phase goal.
- Current phase non-goals.
- Split decision: keep the current phase, split into Phase X.1 or Phase X.2, move to a New
  Major Phase, or place in Backlog.
- Whether the phase is still one single verification loop.
- Inputs.
- Outputs.
- Acceptance criteria.
- Work that is not allowed in this phase.
- For Phase 0, baseline workflow files to create.
- Whether user confirmation has been received.
- Confirmation source: a separate user response after the phase start gate is displayed.
- If the response is unclear or ambiguous, ask a short explicit confirmation question before
  editing files.

If the boundary is unclear, stop and clarify the phase before editing files.

## Phase Exit Checklist

Before marking a phase complete, confirm:

- Tests pass.
- Smoke test passes, when applicable.
- Outputs match the current phase agreement.
- `TODO.md` is updated.
- `DEV_LOG.md` is updated.
- Phase note is updated.
- Handoff note is updated.
- No unexplained scope expansion occurred.
- Verification results and the recommended next action have been reported.
- User confirmation is received before starting the next phase.

## Change Request Policy

Classify mid-phase changes before implementing them:

- Small scoped addition: Phase X.1.
- Current phase bug fix: Phase X.2.
- New capability or separate verification loop: New Major Phase.
- Valuable but not now: Backlog.
- MVP expansion idea: record only, do not implement directly.

Every change request should include impact on files, tests, outputs, and acceptance criteria.
If the classification is New Major Phase, update the plan and wait for user confirmation before
implementing it.

## Handoff Policy

Do not rely on chat history. Recover context from project files.

At the start of a new window, read in this order:

1. `AGENTS.md`
2. `PLAN.md`
3. `TODO.md`
4. `DEV_LOG.md`
5. `DECISIONS.md`
6. The latest phase note or handoff note

At the end of each development round, leave a recoverable state by updating the active TODOs,
development log, phase note, and handoff note.

## Verification Policy

Run actual commands before claiming completion.

Default test command:

```bash
python -m pytest -q
```

Rules:

- Do not use "should run" as a completion standard.
- Do not mark a phase complete when verification fails.
- Record the actual command and result in the phase note or development log.
- If a CLI exists, include a smoke test for the CLI.

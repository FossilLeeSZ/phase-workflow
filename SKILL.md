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
- Copy `templates/project_context_template.md` as `PROJECT_CONTEXT.md` when adopting an
  existing structured project.
- Use `examples/` only when the user needs a concrete pattern for a greenfield start, existing
  structured project adoption, change request, or new-window handoff.

## When To Use This Skill

Use this skill when the user is working on:

- A new project.
- An existing project with a clear structure that needs lightweight phase planning and handoff
  files.
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
- The project state is unclear, heavily tangled, or lacks an identifiable entrypoint,
  verification command, or current goal.
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
- After plan-change update, a later request to start, continue, enter, or execute an
  already-recorded Phase X.N only authorizes the phase start gate; it does not authorize
  execution. The start gate must stop before execution.
- Plan-change confirmation, phase start request, and post-gate execution confirmation cannot
  substitute for each other. Post-gate execution confirmation is the only approval that allows
  fixtures, tests, documents, prompts, templates, policies, or code changes.
- Rule wording: after plan-change update, plan-change confirmation, phase start request, and post-gate execution confirmation cannot substitute for each other.
- If the user gives an ambiguous response, ask a short explicit confirmation question and do
  not edit files.
- If the target folder is an empty folder, treat Phase 0 initialization as gated work.
- Before Phase 0, classify folder state as `empty folder`, `existing structured project
  candidate`, or `unclear project state`.
- Folder state classification is only a recommendation. It must be reported with evidence and
  does not authorize execution.
- For an existing structured project candidate, use Phase 0.1 for workflow adoption and
  Phase 0.2 for a planning baseline.
- During Phase 0.1, create or fill workflow files and `PROJECT_CONTEXT.md`; do not overwrite
  existing project files, plan a roadmap, modify application code, refactor, or start a cleanup
  campaign.
- Rule wording: do not overwrite existing project files.
- During Phase 0.2, use `PROJECT_CONTEXT.md` and a user-confirmed next project goal to create
  a rough planning baseline; do not infer the roadmap from code observations alone.
- Phase 0.1 completion does not authorize Phase 0.2. Phase 0.2 completion does not authorize
  Phase 1. Every phase and sub-phase requires its own visible start gate and separate user
  confirmation.
- Output a visible Phase 0 start gate before creating any project files.
- Do not create baseline workflow files before user confirmation. Baseline workflow files
  include README.md, AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, and DECISIONS.md.
- Split when the user requests a split, when there are multiple independent outputs,
  unrelated user-visible capabilities, separate verification loops, or when reviewability,
  transparency, phase size, risk, user confidence, or avoiding opaque large phases makes the
  phase easier to supervise.
- Do not split only because one coherent phase has several mechanical tasks, but do split when
  the user wants a large phase broken down for review.
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

## Plan-First Execution

Planning records are execution inputs, not after-the-fact summaries.
Rule wording: planning records are execution inputs.

For scope-changing work, update planning files before technical files. This applies to new
phases or sub-phases, phase splits, New Major Phase work, Phase 0.1 workflow adoption,
Phase 0.2 planning baseline, route changes, changes to the current phase goal, non-goals,
outputs, acceptance criteria, or any request that changes the current `PLAN.md` or `TODO.md`
task boundary.

Planning files include `PLAN.md`, `TODO.md`, and, when relevant, the active phase note,
handoff note, `PROJECT_CONTEXT.md`, or `DECISIONS.md`.

Do not start fixtures, tests, implementation, or other technical file changes until the
relevant plan record exists. Do not use `PLAN.md` or `TODO.md` as after-the-fact summaries for
scope-changing work. Prohibited order: Implement first, document plan later.

Current-scope implementation details, verification results, actual modified file lists,
`DEV_LOG.md` entries, handoff summaries, and small non-scope-changing corrections can be
recorded after the technical work.

## Reviewable Splits And Approach Confirmation

User-requested splits have the highest priority. When the user asks to split a phase, output a
split interpretation gate first, wait for confirmation, then update `PLAN.md`, `TODO.md`, and
the active phase note. After those planning files are updated, stop. The split confirmation
only authorizes planning file updates; it does not authorize Phase X.N or any implementation
work.

Phase boundary change confirmation applies to splits, any one-decimal Phase X.N sub-phase,
New Major Phase work, Backlog moves, and phase goal, non-goal, acceptance criteria, or
verification loop changes. Phase X.1 and Phase X.2 are common examples, not the complete
boundary. When Codex proposes a new Phase X.N, it must explain why that sub-phase is needed,
show a phase boundary change proposal, and ask whether to update the plan. After confirmed
planning-file updates, Codex stops before showing the new phase or sub-phase start gate. Show
the already-recorded Phase X.N start gate only after the user later asks to start it. Use one
decimal level only; do not introduce Phase X.N.M.

After plan-change update, that later request still only authorizes the phase start gate. It
does not authorize execution. The start gate must stop before execution and wait for
post-gate execution confirmation.

When Codex recommends a split, explain the basis before asking for confirmation. Valid reasons
include reviewability, transparency, phase size, risk, user confidence, avoiding opaque large
phases, multiple independent outputs, unrelated user-visible capabilities, or separate
verification loops.

Approval model:

> Split confirmation controls phase boundaries. Phase confirmation controls execution
> permission. Approach confirmation controls how non-trivial work will be done.

Approach confirmation applies to any phase or sub-phase. If a phase or sub-phase has a
non-trivial execution approach choice, show the proposed execution approach and wait for user
confirmation before modifying related files. A phase confirmation does not approve an unstated
approach.

Non-trivial execution approach choices include algorithms, architecture, libraries or
dependencies, data structures, Markdown document structure, prompt rewrite strategy, template
field design, policy semantics, test strategy, migration or compatibility strategy, and
user-visible output format. Documents, prompts, templates, policies, tests, and code can all
require approach confirmation when the approach affects outputs, maintainability, validation,
or long-term behavior.

If the user rejects the proposed approach, stop execution. Update `TODO.md`, `PLAN.md`, or the
active phase note as needed, show a revised approach confirmation, and wait for user
confirmation before continuing.

Do not treat split confirmation as execution approval. Do not treat phase or sub-phase
confirmation as approval for an unstated approach. Do not continue implementation after the
user rejects the approach.

## Phase Start Checklist

Before creating fixtures, tests, implementation changes, or any project files for Phase 0,
output a phase start gate and wait for user confirmation.

Identify:

- Current phase.
- Whether the previous phase is complete.
- Folder state: `empty folder`, `existing structured project candidate`, or `unclear project
  state`.
- Current phase goal.
- Current phase non-goals.
- Split decision: keep the current phase, split into Phase X.N, move to a New Major Phase, or
  place in Backlog.
- Whether the phase is still one single verification loop.
- Proposed execution approach, when the work has a non-trivial approach choice.
- Inputs.
- Outputs.
- Acceptance criteria.
- Work that is not allowed in this phase.
- For Phase 0, baseline workflow files to create.
- For Phase 0.1, detected existing files, files to create or fill, files not to overwrite,
  verification command, and `PROJECT_CONTEXT.md` fields.
- For Phase 0.2, `PROJECT_CONTEXT.md`, user-confirmed next project goal, files to update, and
  candidate Phase 1 goal.
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

- One-decimal current-phase sub-phase: Phase X.N.
- Common small scoped addition example: Phase X.1.
- Common current phase bug fix example: Phase X.2.
- New capability or separate verification loop: New Major Phase.
- Valuable but not now: Backlog.
- MVP expansion idea: record only, do not implement directly.

Every change request should include impact on files, tests, outputs, and acceptance criteria.
If the classification is New Major Phase, update the plan and wait for user confirmation before
implementing it.

## Handoff Policy

Do not rely on chat history. Recover context from project files.

At the start of a new window, read compact recovery context in this order:

1. `AGENTS.md`
2. `PLAN.md`
3. `TODO.md`
4. `DECISIONS.md`
5. The latest handoff note or phase note
6. The latest 1-3 `DEV_LOG.md` entries only when recent verification or conflict context is
   needed

Treat `DEV_LOG.md` as a bounded DEV_LOG read and on-demand history source. It is complete
audit history, not default full-file startup context. Read older log entries only when compact
state files conflict, verification results are missing, a decision source is unclear, or the
user explicitly asks for history.

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

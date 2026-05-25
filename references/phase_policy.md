# Phase Policy

Use this policy to define phase boundaries and keep early-stage work small, explicit, and
verifiable.

## Numbering Rules

- Phase 0: initialization, project skeleton, baseline docs, first verification.
- Phase 0.1: workflow adoption for an existing structured project candidate.
- Phase 0.2: planning baseline for an adopted existing structured project.
- Phase 1: first real capability or first pass over the core workflow.
- Phase 1.1: small scoped addition to Phase 1 that does not change the main goal.
- Phase 1.2: bug fix or correction within the current phase boundary.
- Phase X.N: any one-decimal sub-phase under the current major phase. Phase X.1 and Phase X.2
  are common examples, not the complete boundary.
- Phase 2: next independent capability after Phase 1 exits cleanly.
- Phase 5: phase start gate and split confirmation bug fix based on real use.
- Phase 5.1: visible phase start gate before fixtures, tests, or implementation changes.
- Phase 5.2: Phase 0 start gate before creating files in an empty folder.
- Phase 5.3: separate post-gate confirmation before execution.
- Phase 6: README workflow diagram and usage guidance documentation improvement.
- Phase 6.1: pre-release README and plan consistency polish.
- Phase 7: iteration from real early-stage project feedback.
- Phase 8: context-light recovery and bounded DEV_LOG read policy.
- Phase 9: existing structured project adoption.
- Phase 10: plan-first execution order and README flow alignment.
- Phase 11: reviewable splits and approach confirmation.

Use one decimal level only. Do not introduce Phase X.N.M. If the change no longer fits under
the current major phase, make it a New Major Phase or backlog item.

## Phase Meanings

### Phase 0

Create the project baseline. For this repository, that means docs, references, templates,
examples, and minimal tests.

When the target folder is an empty folder, Phase 0 still starts with a visible Phase 0 start
gate. Codex must list the baseline workflow files before creating any project files. Baseline
workflow files include README.md, AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, and DECISIONS.md.

Before Phase 0, classify folder state as `empty folder`, `existing structured project
candidate`, or `unclear project state`.

For an existing structured project candidate, use Phase 0.1 for workflow adoption. Phase 0.1
creates or fills workflow files and `PROJECT_CONTEXT.md` around the current project state. It
must list detected existing files, detected test/build/smoke commands when available, files to
create or fill, and files not to overwrite. Phase 0.1 must not overwrite existing project
files, plan future feature work, modify application code, refactor code, or start a cleanup
campaign.

Use Phase 0.2 for a planning baseline only after the user separately requests it and provides
or confirms the next project goal. Phase 0.2 uses `PROJECT_CONTEXT.md` and the user-confirmed
goal to update `PLAN.md`, `TODO.md`, and handoff notes with a rough roadmap and candidate
Phase 1 goal. It must not infer the roadmap from code observations alone.

If the folder state is `unclear project state`, stop and report why adoption is not recommended
yet. Ask for clarification or recommend a separate project assessment instead of creating
workflow files.

### Phase 1

Improve the first meaningful version of the skill after initialization. This should refine
instructions and templates before adding larger capabilities.

### Phase 1.1

Use for a small addition discovered during Phase 1, such as adding one missing field to a
template or clarifying one policy section.

### Phase 1.2

Use for a correction to work already inside Phase 1, such as fixing a broken test or correcting
a contradiction in documentation.

### Phase 2

Use for the next coherent capability after Phase 1 has been verified and handed off.

### Phase 3

Add lightweight documentation completeness tests and local lint checks. This phase should keep
checks simple, local, and dependency-free.

### Phase 4

Prepare installation notes and usage examples for copying the skill into a normal Codex skill
layout. This phase should avoid platform-specific assumptions beyond the standard skill
directory shape.

### Phase 5

Fix the phase start gate so Codex must report a split decision and wait for user confirmation
before creating fixtures, tests, or implementation changes.

Phase 5.1 covers major phase and sub-phase start gates. Phase 5.2 covers empty folder Phase 0
startup and baseline workflow files. Phase 5.3 covers separate post-gate confirmation before
execution.

### Phase 6

Add README workflow diagram and usage guidance that explain the file-based phase loop without
changing the workflow behavior. This phase covers the diagram, phase start request
clarification, Plan Mode review tip, new-window hygiene, and pre-release consistency polish.
It should keep the diagram as Markdown/Mermaid text and avoid generated image assets or new
dependencies.

### Phase 7

Iterate from real early-stage project feedback. This phase should tie changes to observed
usage and record durable methodology changes in `DECISIONS.md`.

### Phase 8

Reduce new-window context cost by treating `DEV_LOG.md` as complete audit history rather than
default startup context. This phase should keep recovery file-based, make the latest handoff
note or phase note the compact recovery source, and document the bounded DEV_LOG read policy.

### Phase 9

Support adopting `phase-workflow` into existing projects with a clear structure. This phase
adds the Phase 0.1 workflow adoption path, the Phase 0.2 planning baseline path,
`PROJECT_CONTEXT.md`, no-overwrite rules, and folder state classification.

### Phase 10

Require plan-first execution order for scope-changing work and align README flow guidance.
Planning records are execution inputs, not after-the-fact summaries.
Rule wording: planning records are execution inputs.

### Phase 11

Require reviewable split decisions and explicit approach confirmation for non-trivial work.
This phase makes reviewability, transparency, phase size, risk, user confidence, and avoiding
opaque large phases valid reasons to split a phase even when the outputs are related.

Phase 11.1 adds phase boundary change confirmation so any Phase X.N sub-phase follows the same
confirm-plan-update-stop flow as a split.

## One Closed Loop Per Phase

Each phase should include:

1. Scope boundary.
2. Fixtures or examples.
3. Failing tests.
4. Minimal implementation.
5. Verification.
6. Documentation and handoff.

Do not start later-phase implementation while the current phase is still open.

## Execution Order

Scope-changing work must update planning files before technical files. After a phase start
gate and separate user confirmation, the first file changes for new phases, sub-phases, phase
splits, New Major Phase work, route changes, or acceptance criteria changes should update
`PLAN.md`, `TODO.md`, and any relevant phase note, handoff note, `PROJECT_CONTEXT.md`, or
`DECISIONS.md`.
Rule wording: scope-changing work must update planning files before technical files.

Do not start fixtures, tests, implementation, or other technical file changes before the
relevant plan record exists. Do not treat `PLAN.md` or `TODO.md` as after-the-fact summaries
for scope-changing work. Prohibited order: Implement first, document plan later.

Verification results, actual modified file lists, `DEV_LOG.md` entries, handoff summaries, and
small non-scope-changing corrections can be recorded after technical work.

## Phase Boundary Change Confirmation

Phase boundary changes include splits, any one-decimal Phase X.N sub-phase, New Major Phase
work, Backlog moves, and phase goal, non-goal, acceptance criteria, or verification loop
changes. Phase X.1 and Phase X.2 are common examples, not the complete boundary.

When Codex proposes a new Phase X.N, it must:

1. Explain why the sub-phase is needed.
2. Show a phase boundary change proposal.
3. Ask the user to confirm the planning change before updating planning files.
4. If confirmed, update `PLAN.md`, `TODO.md`, and any relevant phase note.
5. Stop.
6. Show the already-recorded Phase X.N start gate only after the user later asks to start it.

After confirmed planning-file updates, Codex stops before showing the new phase or sub-phase
start gate. Use one decimal level only; do not introduce Phase X.N.M.

After plan-change update, a later request to start, continue, enter, or execute the
already-recorded Phase X.N only authorizes the phase start gate. It does not authorize
execution. The start gate must stop before execution and wait for post-gate execution
confirmation.

Plan-change confirmation, phase start request, and post-gate execution confirmation cannot
substitute for each other.

## Reviewable Split Policy

A split can be justified by reviewability, transparency, phase size, risk, user confidence,
avoiding opaque large phases, multiple independent outputs, unrelated user-visible
capabilities, or separate verification loops.

User-requested splits take priority. Codex should interpret the requested split, output the
proposed Phase X.N boundary, and wait for user confirmation. Codex-recommended splits must
explain the rationale before asking for confirmation.

Split flow:

1. Recommend or interpret the split.
2. Wait for user confirmation of the split boundary.
3. Update planning files such as `PLAN.md`, `TODO.md`, and the active phase note.
4. Stop.
5. Show the next phase or sub-phase start gate only after the user asks to continue.

Rule wording: split confirmation only authorizes planning file updates. It does not authorize
Phase X.N execution, fixtures, tests, implementation, or other technical file changes.

## Approach Confirmation

Rule wording: approach confirmation applies to any phase or sub-phase.

If there is a non-trivial execution approach choice, the phase start gate or execution plan
must show the proposed execution approach before related file changes begin. Wait for user
confirmation of that approach before modifying documents, prompts, templates, policies, tests,
or code.
Rule wording: documents, prompts, templates, policies, tests, and code can all require
approach confirmation.

Non-trivial approach choices include algorithms, architecture, libraries or dependencies, data
structures, Markdown document structure, prompt rewrite strategy, template field design,
policy semantics, test strategy, migration or compatibility strategy, and user-visible output
format.

Approval model:

> Split confirmation controls phase boundaries. Phase confirmation controls execution
> permission. Approach confirmation controls how non-trivial work will be done.

Rule wording: Split confirmation controls phase boundaries. Phase confirmation controls execution permission. Approach confirmation controls how non-trivial work will be done.

Do not treat phase or sub-phase confirmation as approval for an unstated approach.

## Phase Start Checklist

- What is the current phase?
- Is the previous phase complete and verified?
- What is the folder state: `empty folder`, `existing structured project candidate`, or
  `unclear project state`?
- What is the current phase goal?
- What are the non-goals?
- What is the visible phase start gate summary?
- What is the split decision: keep the phase, use Phase X.N, create a New Major Phase, or put
  it in Backlog?
- Is the phase still one single verification loop?
- Is there a non-trivial execution approach choice? If yes, what approach is being proposed?
- What inputs are available?
- What outputs must exist?
- What acceptance criteria define completion?
- What work is explicitly not allowed?
- For Phase 0, what baseline workflow files will be created?
- For Phase 0.1, what existing files were detected, what files will be created or filled, what
  files will not be overwritten, and what verification command is available?
- For Phase 0.2, what `PROJECT_CONTEXT.md` content and user-confirmed next project goal are
  being used?
- Has the user confirmed the phase boundary?
- A request to start a phase is not confirmation.
- Is the confirmation source a separate user response after the phase start gate is displayed?
- If this start request follows a plan-change update, remember that it only authorizes the
  phase start gate and does not authorize execution.
- Remember that `PLAN.md` phase boundaries are not user confirmation.
- Remember that phase exit confirmation is not next phase start confirmation.
- Do not treat "start Phase X" as confirmation; it only triggers phase analysis and a phase
  start gate.
- Always stop after reporting the phase start gate.
- If the reply is an ambiguous response, ask a short explicit confirmation question before
  editing files.

Do not create fixtures, tests, or implementation changes until the phase start gate is reported
and the user confirms the boundary.

For empty folder startup, do not create any project files until the Phase 0 start gate is
reported and the user confirms the boundary.

Phase 0.1 completion does not authorize Phase 0.2. Phase 0.2 completion does not authorize
Phase 1. Every phase and sub-phase requires its own visible start gate and separate user
confirmation. `Start Phase X` only asks Codex to show the gate; it is not execution
confirmation.

## Phase Exit Checklist

- Required tests pass.
- Smoke test passes, if relevant.
- Outputs match the phase agreement.
- `TODO.md` is current.
- `DEV_LOG.md` records what changed and how it was verified.
- The phase note records scope, files, tests, risks, and next steps.
- The handoff note lets a new Codex session continue without chat history.
- Scope expansion is either absent or documented as a change request.

## Avoiding Scope Creep

- Write non-goals at phase start.
- Treat "while we are here" ideas as change requests.
- Move new capabilities to a future phase.
- Put useful but non-urgent ideas in Backlog.
- Do not implement unplanned features because they seem small.
- Update `DECISIONS.md` when the long-term strategy changes.

# Phase Policy

> Policy role: canonical owner for applicability, complete delivery, real-capability semantics,
> phase lifecycle, visible gates, live authorization, mutation preflight, and violation
> recovery. `policy-owner: phase-lifecycle`

Use this policy to define phase boundaries and keep zero-based project work small, explicit,
and verifiable without hollowing out the promised capability. A phase can be small, but it must
not be hollow. Use [change-request policy](change_request_policy.md) for Phase X.N allocation
and scope-change routing, [recovery protocol](recovery_protocol.md) for context/state recovery,
and [verification policy](verification_policy.md) for evidence and completion.

## Quick Navigation

- [Phase meanings](#phase-meanings)
- [Project context, applicability, and complete delivery](#project-context-applicability-and-complete-delivery)
- [Optional shared-understanding interview](#optional-shared-understanding-interview)
- [Authorization and recovery state machine](#authorization-and-recovery-state-machine)
- [Live confirmation binding](#live-confirmation-binding)
- [Partial execution revalidation](#partial-execution-revalidation)
- [Mutation preflight](#mutation-preflight)
- [Violation recovery and selected rollback](#violation-recovery-and-selected-rollback)
- [Approach confirmation](#approach-confirmation)
- [Phase start checklist](#phase-start-checklist)
- [Phase exit checklist](#phase-exit-checklist)

## Phase Meanings

### Phase 0

Create the target project baseline. When the target folder is an empty folder, Phase 0 still
starts with a visible Phase 0 start gate. Codex must list the baseline workflow files before
creating any project files. Baseline workflow files include README.md, AGENTS.md, PLAN.md,
TODO.md, and DECISIONS.md.

Those files are Phase 0 outputs, not preconditions. The gate uses relevant available
conversation, read-only folder evidence, and provisional anchors and gaps until the user
authorizes their creation.

Before Phase 0, classify folder state as `empty folder`, `existing structured project
candidate`, `existing workflow project`, or `unclear project state`. Missing one entry point,
test command, goal, or evidence source does not by itself determine this result; inspect each
fact and apply the Context Gap materiality rule.

Use `unclear project state` only when a genuinely blocking uncertainty still affects the
adoption outputs, acceptance, approach, or safety after bounded read-only assessment. Enter
`CONTEXT_BLOCKED`, report the gap, and stop instead of guessing or creating workflow files.

For an existing workflow project, recover compact current state from project files before
proposing the next phase gate.

### Phase 0.1

Use Phase 0.1 for workflow adoption in an existing structured project candidate. Phase 0.1
creates or fills workflow files and `PROJECT_CONTEXT.md` around the current project state. It
must list detected existing files, detected test/build/smoke commands when available, files to
create or fill, and files not to overwrite.

Phase 0.1 must not overwrite existing project files, plan future feature work, modify
application code, refactor code, or start a cleanup campaign.

Missing adoption files are expected Phase 0.1 outputs. Use relevant available conversation and
read-only repository evidence to propose a stable factual baseline; do not require the new
anchors to exist before their gate and authorized creation.

`AGENTS.md` and `.codex/hooks.json` are Phase 0 or Phase 0.1 adoption outputs. Create or fill
`.codex/hooks.json` only when optional project-level hook support is selected or explicitly
requested.

### Phase 0.2

Use Phase 0.2 for a planning baseline only after the user separately requests it and provides
or confirms the next project goal. Phase 0.2 reconciles the factual `PROJECT_CONTEXT.md`
baseline, relevant available conversation, repository evidence, and the user-confirmed goal to
update `PLAN.md`, `TODO.md`, and the active phase note with the target boundary, project-level
completion target, complete delivery path, candidate major capability phases, and candidate
Phase 1 goal. It must not infer the roadmap from code observations alone.

Phase 0.2 allows planning records only: `PLAN.md`, `TODO.md`, phase notes, selected optional
handoff indexes, planning baselines, roadmaps, and candidate Phase 1 goals. During Phase 0.2
there are no
tests, code skeletons, migrations, file restores, technical implementation, scripts, or
non-planning technical documentation. Non-planning technical documentation includes API docs,
architecture docs, migration guides, usage docs, module docs, or generated technical docs. Do
not treat planning records as technical deliverables. In short: no tests, code skeletons,
migrations, file restores, or technical implementation. After Phase 0.2, stop before Phase 1.

### Phase N

Use Phase N for the next coherent major capability after the previous phase exits cleanly.
Keep the phase focused on one goal and one user-value loop or end-to-end capability loop.

Phase X.N allocation, New Major Phase routing, Backlog routing, Change Type, and split
classification are owned by [change-request policy](change_request_policy.md#classification).
After a phase or direct sub-phase is confirmed and recorded there, it enters the same visible
gate, independent verification, and stop lifecycle defined by this policy. One direct
sub-phase level is supported; the change-request policy prohibits Phase X.N.M.

## Project Context, Applicability, And Complete Delivery

### Context source responsibilities

Use relevant available conversation for current intent and durable anchors for persisted
meaning. Detailed source responsibilities, recovery order, conflict resolution, Context Gaps,
and state ownership are owned by [recovery protocol](recovery_protocol.md). Recovery inputs do
not grant mutation authorization; the live state defined by this policy does.

### Applicability and target-product boundary

Applicability is not determined by maturity, project size, implementation size, or team size:
solo developers, small teams, and large teams may all use the workflow. Do not classify or
reject work merely because the project is mature, large, long-running, multi-release,
regulated, a repair or migration, or needs a large refactor. An unclear or tangled repository
requires a bounded read-only assessment rather than immediate adoption or permanent rejection.

A target product or target system may legitimately require a database, Web UI, cloud service,
authentication, complex CLI, business workflow, issue-tracker integration, migration, or large
refactor. Architecture restrictions and non-goals for this repository limit the
`phase-workflow` implementation itself; they are not restrictions on the target product or
target system governed by the workflow.

Do not adopt the workflow for a one-off question that needs no continuity, an explicit user
opt-out, or a higher-priority process that is incompatible and that the user does not want
changed. A compatible mature or regulated process may use `phase-workflow` as a subordinate
file-based execution anchor.

A project that has not adopted the workflow may handle a direct small task through direct
execution when the user requests it. Inside an adopted project, a direct bugfix still follows
the workflow unless the user explicitly chooses to opt out for that request; classify any required
sub-phase through the change-request policy.

### Complete-delivery and phase mapping

Plan toward the complete target system. Record the project goal, target boundary, project-level
completion target, complete delivery path, durable constraints, non-goals, and candidate major
capability phases. Each executable phase must identify the project-level completion criterion
it advances and verify the real capability declared by that phase.

MVP, prototype, pilot, preview, smoke, or first release is a user-selected, project-specific
possible milestone, not the default project identity, universal cap, or project completion
target. Completing a milestone or one phase does not silently reduce the target, prove the
whole project complete, authorize unlimited scope, or authorize the next phase.

Fixtures, tests, documents, scaffolding, UI shells, job stubs, and fake results do not
substitute for the real capability or prove runtime or executable behavior when the phase
promises such behavior. Documents are the declared product only when the phase explicitly says
so; in that case, verify the real document deliverable and its acceptance criteria. Otherwise
documentation does not substitute for a promised runtime capability.

### Bootstrap and missing context

For Phase 0 or Phase 0.1, missing durable files are expected. Show provisional Context Anchors
and Context Gaps in the visible gate and create the durable baseline files as declared phase
outputs; do not require those outputs to pre-exist or already exist before their authorized
creation. From Phase 0.2 and ordinary technical phases onward, revalidate the applicable
durable anchors before execution.

When relevant conversation is unavailable, recover known anchors from project files and
repository evidence, make missing or conflicting meaning explicit as Context Gaps, and do not
invent history or require a full transcript. Recovered context never restores a previous
execution confirmation.

## Optional Project-Level Hook Reminders

Hook adoption and operation are user-facing setup concerns owned by [README](../README.md).
The policy invariant is compact: a hook is optional and reminder-only; it cannot invoke the
skill, mutate files, recover state, or grant authorization. When the workflow applies, open the
current `SKILL.md` regardless of hook presence.

## Optional Shared-Understanding Interview

Use the [shared-understanding protocol](shared_understanding_protocol.md) when the user explicitly
asks to be grilled or to stress-test a plan, or when a material unresolved user decision affects
outputs, acceptance, approach, or safety. For an ordinary well-defined phase, do not require the
optional interview; continue through the existing gate path.

The interview does not create a new lifecycle state. Keep it read-only within
`READ_ONLY_RECOVERY` or `CONTEXT_BLOCKED` while facts and decisions are reconciled. If it begins
after a gate and changes the contract or material approach, use the existing contract or
approach-revision route and require a new gate binding.

Shared-understanding closure does not advance lifecycle state and cannot satisfy plan-change
confirmation, a phase-start request, the visible gate, or live execution confirmation. After
closure, return to the applicable existing classification, plan-change, recovery, or gate flow.

## Authorization Model

Use this single authorization model before the detailed phase-boundary rules below. Authorization
follows the recorded phase contract and its declared outputs, not the file type being changed.
When two signals conflict, the narrower authorization controls and Codex must stop at the next
required gate.

| Signal | Authorizes | Does not authorize | Required stop |
| --- | --- | --- | --- |
| Plan-change confirmation | The disclosed planning-boundary update only | A phase gate, current-phase execution, technical work, or later phases | Stop after the planning update |
| Phase start request | phase analysis and visible start gate only | Execution, file edits, or current-phase mutations | Stop after the gate |
| Post-gate execution confirmation | The current phase's disclosed declared outputs that pass mutation preflight | Undeclared outputs, later phases, multi-phase execution, or a changed contract or approach | Stop when the current phase exits |
| Approach confirmation | The fully disclosed non-trivial approach inside the current phase; it may share one explicit reply with execution confirmation | An unstated or materially revised approach, phase boundary changes, or broader scope | Stop when the approach is rejected or materially revised |
| Mutation preflight pass | The checked current state transition and declared-output mutation | Failed-gate, stale-confirmation, wrong-state, undeclared-output, later-phase, or multi-phase mutations | Stop before files if any check fails |
| Phase violation detected | Read-only violation audit before user choice; keep-and-audit record repair or selected rollback after the corresponding live choice | New implementation, next-feature work, continuing the violated flow, or mutations outside the selected recovery branch | Stop before the recovery choice and again after recovery verification |

Plan-change confirmation, phase start request, post-gate execution confirmation, approach
confirmation, mutation preflight, and phase violation recovery are separate controls. They
cannot substitute for each other and do not authorize multi-phase execution. A successful
authorization does not authorize next-phase work and does not authorize multi-phase execution.
Do not use the phase violation row to write recovery record repairs before user choice.

## Authorization And Recovery State Machine

The state machine below is normative. A state transition, rather than a filename category,
determines whether a mutation is allowed. Every mutation must be part of one row, use the row's
required evidence, remain within its allowed mutation, and stop at its Required stop. If no row
fits or the evidence is incomplete, enter `CONTEXT_BLOCKED` and do not mutate files.

| State | Trigger and required evidence | Allowed mutation | Forbidden outcome | Required stop |
| --- | --- | --- | --- | --- |
| `READ_ONLY_RECOVERY` | Current request plus relevant available conversation, scoped Context Anchors, and repository evidence | None; read and reconcile only | Treating recovered text as permission | Move to `CONTEXT_BLOCKED`, `PLAN_UPDATE_AUTHORIZED`, or `GATE_READY` |
| `CONTEXT_BLOCKED` | A material Context Gap, conflicting anchor, missing field, or unclear repository state affects output, acceptance, approach, or safety | None | Guessing the missing contract or continuing an old confirmation | Stop for clarification or a corrected boundary |
| `PLAN_UPDATE_AUTHORIZED` | Explicit confirmation of a disclosed phase-boundary, roadmap, goal, non-goal, output, acceptance, or verification-loop change | Only the named planning-boundary update and matching planning records | Tests, implementation, a phase gate in the same turn, or current/later phase execution | Stop after the planning update; a later request may show the gate |
| `GATE_READY` | Current phase, previous verification, repository state, contract revision, approach revision, declared outputs, acceptance, verification loop, non-goals, and stop condition have been revalidated | Show the visible gate only | Any repository mutation | Move to `AWAITING_LIVE_CONFIRMATION` and stop |
| `AWAITING_LIVE_CONFIRMATION` | The visible gate has been shown in the current task and no later material drift is known | None | Treating `Start Phase X`, files, summaries, or historical replies as confirmation | Stop until an explicit live confirmation arrives |
| `EXECUTION_AUTHORIZED` | A live confirmation matches the binding in the shown gate and mutation preflight passes | Only the disclosed declared outputs, including their tests, documents, code, planning-only outputs, and bounded evidence/status records | Undeclared output, changed approach, next phase, multi-phase work, or reusable authorization receipt | Move to `PARTIAL_REVALIDATION`, `APPROACH_REVISION_REQUIRED`, `VIOLATION_AUDIT`, or `PHASE_EXIT` |
| `PARTIAL_REVALIDATION` | Execution was interrupted; actual files, completed outputs, remaining outputs, modified files, and verification results have been inspected | Verified remaining declared outputs only | Repeating verified completed work or assuming unverified completion | Resume `EXECUTION_AUTHORIZED`, or return to a revalidation gate if the binding cannot be proven |
| `APPROACH_REVISION_REQUIRED` | The phase contract or material approach changed after confirmation | Record the proposed revision only under the applicable planning/status rule | Continuing under stale confirmation | Show a revalidation gate and return to `AWAITING_LIVE_CONFIRMATION` |
| `VIOLATION_AUDIT` | Evidence shows an approved boundary was crossed | None; perform a read-only audit and chat-visible incident report | New implementation, rollback, or record repair before user choice | Move to `RECOVERY_CHOICE_REQUIRED` and stop |
| `RECOVERY_CHOICE_REQUIRED` | The audit identifies affected technical changes and records | None | Inferring keep-and-audit or rollback from old context | Stop for a live user choice |
| `SELECTED_ROLLBACK_AUTHORIZED` | A live user choice names the reverse technical scope and matching records | User-named reverse technical changes, corresponding record repair, and verification only | Broad cleanup, forward implementation, unrelated rollback, or later-phase work | Stop after verification and an honest recovery record |
| `PHASE_EXIT` | Declared outputs and acceptance criteria are met by actual verification | Bounded verification, TODO, phase-note, handoff/current-state, and durable-decision records disclosed by the phase contract | Next-phase work or an unverified completion claim | Stop before the next phase's separate gate and separate live confirmation |

`keep-and-audit` is the recovery alternative to `SELECTED_ROLLBACK_AUTHORIZED`. After a live
keep-and-audit choice, repair only the records needed to describe the already-existing changes,
verification, violation, and remaining boundary. It does not authorize new technical work.

## Live Confirmation Binding

A valid live confirmation is bound to the shown Phase ID, phase-contract revision, approach
revision, declared outputs, acceptance criteria, verification loop, revalidated repository
state, and stop condition. Record those values in the visible gate in readable form; do not
persist the reply as a reusable authorization receipt.

`Start Phase X`, `begin`, `continue`, `next`, or similar phase-start language does not authorize
execution. It requests gate analysis only. A fully disclosed approach may be confirmed by the
same one explicit reply that confirms execution. The reply must clearly accept both execution
and that disclosed approach; a generic phase request does neither.

A phase-contract revision or material approach revision invalidates the prior confirmation. A
related unknown repository drift, missing binding field, context compaction that removes direct
evidence of the gate and reply, or a new window also returns the workflow to a concise
revalidation gate and `AWAITING_LIVE_CONFIRMATION`. Harmless conversation changes that do not
affect the binding do not force a new confirmation.

Imported chat, a compressed summary, handoff text, TODO text, a phase note, historical
confirmation, or a file saying `confirmed` is context or audit evidence only. None can enter
`EXECUTION_AUTHORIZED` or `SELECTED_ROLLBACK_AUTHORIZED` without the applicable live transition.

## Declared-Output Authorization

Post-gate authorization is determined by the current phase's declared outputs, not by file
type. A declared output may be a document, planning record, fixture, test, script, code change,
migration, restore, generated artifact, status record, or verification command. Mutation
preflight checks that the exact output and purpose were disclosed before allowing it.

- Phase 0 may create its gate-listed workflow baseline as declared outputs after post-gate live
  confirmation, even though those files did not exist before the gate.
- Phase 0.1 may create or fill its gate-listed adoption and `PROJECT_CONTEXT.md` outputs after
  post-gate live confirmation without overwriting excluded project files.
- Phase 0.2 is planning-only. Its post-gate confirmation authorizes exactly its declared
  planning outputs and no technical implementation. This is phase execution, not a later
  plan-change shortcut.
- An ordinary technical phase may change only its declared technical, documentation, test,
  verification, and bounded status outputs.
- A plan-change branch is for changing the recorded phase boundary, contract, roadmap, or
  verification loop. It updates only the disclosed planning boundary and must stop before a
  gate or execution.

Classify by intent and declared output, not by filename. The same `TODO.md` or phase-note file
may contain a Phase 0.2 declared planning output, a current execution-status output, a later
boundary change, or a recovery repair; each requires its own applicable state transition.

Before the gate binds Declared Outputs, inventory lifecycle-coupled tests and artifacts whose
expectations depend on the current Phase ID, PLAN anchor or heading, active phase-note path or
heading, owner revision, or other changing workflow state. Make each one derive current values
from the canonical owners, or name it as an exact Declared Output with its transition purpose.
Do not assume a test is lifecycle-independent merely because it passed in the previous phase.

A later-discovered stale lifecycle-coupled test or artifact remains current failed evidence. If
it is undeclared, do not edit it under an implicit maintenance exception; stop and route the
new output through a contract revision and renewed live confirmation. Discovery never expands
the existing authorization.

## Partial Execution Revalidation

When execution is interrupted, inspect actual files, completed outputs, remaining outputs,
modified files, and verification results. Mark only evidence-backed completion. Do not repeat
verified completed work merely because the prior conversation was compacted.

Resume the verified remaining outputs only when the current task still contains direct evidence
of the gate, live confirmation, unchanged binding, and repository state. Otherwise show a short
revalidation gate that states the recovered completed outputs, remaining outputs, drift check,
contract and approach revisions, verification still needed, and stop condition; then wait for
new live confirmation.

## Workflow Authority

When `phase-workflow` applies, it is the highest phase-boundary and authorization workflow. It
controls scope, authorization, phase boundaries, and file-modification boundaries.

Plan executors, test workflows, debugging workflows, refactoring workflows, migration
workflows, code generation helpers, documentation generators, task checklists, and
tool-specific workflows can only guide work inside the currently authorized phase. They cannot
decide phase boundaries, advance to the next phase, or execute multiple phases in one run.

Requests such as "implement this plan" do not collapse multiple phases into one authorized
execution. If the requested plan contains multiple phases, multiple verification loops, or
multiple independent outputs, only the currently confirmed phase may execute. Unconfirmed
phases must stop at a phase gate.

Todo lists, checklists, progress trackers, and `update_plan` cannot substitute for phase start
gates, split confirmation, approach confirmation, or post-gate execution confirmation.

Do not record batch phase completions such as `Phase 1-5 complete`, `Phase 2/3/4`, or
`multi-phase migration complete`; each phase must have separate TODO status and phase-note
verification/history. An optional handoff index does not replace either owner.

## Mutation Preflight

Before repository mutations, run a mutation preflight. Repository mutations include file
writes, deletes, moves, restores, generated tests, generated docs, scripts, migrations, and
implementation changes. Any work that changes repository files must pass mutation preflight
before modifying files.

Mutation Authorization Branches:

- Read-only recovery and violation audit allow no repository mutation.
- A plan-update mutation requires explicit plan-change confirmation, the named planning-boundary
  output, and a stop before any gate or phase execution.
- A declared-phase-output mutation requires a visible gate, matching live confirmation, valid
  binding, and mutation preflight. It may include planning-only, technical, documentation,
  test, verification, or status outputs disclosed by the phase.
- A keep-and-audit record repair requires the live recovery choice and may describe only the
  already-existing violated state.
- A selected rollback requires the live user-named reverse scope and may perform only those
  reverse technical changes, corresponding record repair, and verification.
- If the state transition, mutation intent, or declared output is unclear, stop before mutating
  files.

For every proposed mutation, answer:

- What is the current state and Phase ID?
- What live signal entered this state?
- What phase-contract and approach revisions were confirmed?
- Which exact declared output does the mutation produce?
- Is the repository state still the state revalidated for the gate?
- Does the mutation stay inside the acceptance criteria and one verification loop?
- Is the required stop still explicit?
- Would it create an undeclared output, complete multiple phases, or enter a later phase?

For plan updates, also confirm the named boundary change and stop after its planning records.
For partial execution, confirm completed and remaining outputs from evidence. For recovery,
confirm the live keep-and-audit or selected rollback choice. If any answer fails, stop before
mutating files.

## Violation Recovery And Selected Rollback

Use Phase Violation Recovery when an approved phase boundary has already been crossed. This is
a mandatory recovery flow, not permission to continue implementation.

When a violation is discovered, stop new implementation and enter a read-only audit. Report
`implementation happened outside approved phase boundary`, affected files, tests, migrations,
restores, docs, status records, known verification, and uncertain effects. Then enter
`RECOVERY_CHOICE_REQUIRED` and ask for a live choice between keep-and-audit and selected
rollback. No mutation is allowed before that choice.

Keep-and-audit permits corresponding record repair only. Record the already-existing changes,
violation, evidence, unfinished work, and current boundary; do not add new feature work.

Selected rollback is a bounded reverse-technical branch. Require the user-named reverse
technical changes, corresponding record repair, and verification plan. Change only that named
scope, repair only the records affected by it, run verification, report remaining effects, and
stop. It authorizes no new feature work, cleanup, unrelated restore, later phase, or broad reset.

A new window does not inherit and therefore invalidates an earlier rollback authorization. A
compressed summary, handoff, recovery record, or old reply may describe the audit but cannot
restore the live rollback choice. Show the recovered audit and selected scope in a revalidation
gate, then wait for new live confirmation before reverse technical changes.

## One Real Capability Loop Per Phase

Each phase should include:

1. Scope boundary.
2. Fixtures or examples.
3. Failing tests.
4. The real capability inside the declared phase boundary.
5. Verification of the phase-declared capability, not merely an internal mechanism.
6. Documentation and recoverable context checkpoint.

The phase may be narrow, but it must be vertically complete for the promised capability.
Preview, smoke, contract-only, stub, fake, or simulated behavior is acceptable only when the
phase boundary and user-facing labels say so. If UI, job, progress, artifact, and result
surfaces imply a real capability, the real execution path must be connected before the phase is
marked complete.

Do not start later-phase implementation while the current phase is still open.

## Execution Order

Scope-changing work must update planning files before technical files. After a phase start gate
only when the phase boundary already exists and the live confirmation authorizes its declared
outputs. Creating or changing a phase boundary follows
[change-request policy](change_request_policy.md): propose, confirm the planning change, update
the planning owners, and stop before any phase start gate or technical work.

Do not start fixtures, tests, implementation, or other technical file changes before the
relevant plan record exists. Do not treat `PLAN.md` or `TODO.md` as after-the-fact summaries
for scope-changing work. Prohibited order: Implement first, document plan later.

Verification results, actual modified file lists, phase note updates, handoff summaries, and
small non-scope-changing corrections can be recorded after technical work.

## Phase Boundary Authorization

Phase-boundary creation, split proposals, sequential identifiers, and plan-change updates are
owned by [change-request policy](change_request_policy.md). This policy owns the authorization
outcome after that planning flow: plan-change confirmation, a later phase-start request, and a
post-gate live execution confirmation are distinct signals and cannot substitute for each
other.

Reviewability can motivate a split, but the reasons, complete proposed split, allocation, and
planning update are owned by
[change-request policy](change_request_policy.md#phase-boundary-changes). Once recorded, every
resulting phase or sub-phase requires its own gate, live confirmation, real-capability
verification, and exit stop.

## Plan Mode Skill Invocation Guard

Plan Mode is optional. When Plan Mode is enabled and the task is covered by this workflow,
Codex must activate and follow phase-workflow first.

Plan Mode cannot bypass phase-workflow activation, phase boundary change checks, phase start
gates, or post-gate execution confirmation. In Plan Mode, plan, phase, scope, or design-change
requests still require `phase-workflow` classification before returning a proposed plan.

Plan Mode proposed plan cannot substitute for plan-change confirmation, phase start request,
and post-gate execution confirmation. Plan Mode does not authorize execution.

## Approach Confirmation

Approach confirmation applies to any phase or sub-phase.

If there is a non-trivial execution approach choice, the phase start gate or execution plan
must show the proposed execution approach before related file changes begin. Wait for user
confirmation of that approach before modifying documents, prompts, templates, policies, tests,
or code. Documents, prompts, templates, policies, tests, and code can all require approach
confirmation.

Non-trivial approach choices include algorithms, architecture, libraries or dependencies, data
structures, Markdown document structure, prompt rewrite strategy, template field design, policy
semantics, test strategy, migration or compatibility strategy, and user-visible output format.

A material approach revision invalidates the earlier live confirmation even when the goal and
declared outputs stay the same. Record the revised approach in the active phase note, update
TODO's compact state and next action, show a revalidation gate, and wait for a new live
confirmation before continuing. If outputs, acceptance criteria, risk, or the verification loop
also changes, route the change through `references/change_request_policy.md`.

Approval model:

> Split confirmation controls phase boundaries. Phase confirmation controls execution permission. Approach confirmation controls how non-trivial work will be done.

Do not treat phase or sub-phase confirmation as approval for an unstated approach.

## Phase Start Checklist

- What is the current phase?
- Is the previous phase complete and verified?
- What is the folder state: `empty folder`, `existing structured project candidate`,
  `existing workflow project`, or `unclear project state`?
- What is the current phase goal?
- What are the non-goals?
- What is the visible phase start gate summary?
- What is the split decision: keep the phase, use Phase X.N, create a New Major Phase, or put
  it in Backlog?
- Is the phase still one single verification loop?
- Is there a non-trivial execution approach choice? If yes, what approach is being proposed?
- What inputs are available?
- What outputs must exist?
- Which lifecycle-coupled tests or artifacts depend on the current phase, owner anchors, paths,
  headings, or revisions?
- Does each lifecycle-coupled artifact derive current values from canonical owners, or is it an
  exact declared output for this transition?
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

Use [verification policy](verification_policy.md) for evidence, failure handling, phase versus
project completion, and the completion record. After verified exit, update each fact in its
owner defined by [recovery protocol](recovery_protocol.md), then stop before the next phase
gate.

## Avoiding Scope Creep

Write non-goals at phase start. Route new requirements through
[change-request policy](change_request_policy.md) rather than absorbing them into the active
phase. Record durable strategy changes in `DECISIONS.md`.

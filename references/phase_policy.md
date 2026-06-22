# Phase Policy

Use this policy to define phase boundaries and keep early-stage work small, explicit, and
verifiable.

## Numbering Rules

- Phase 0: initialization, project skeleton, baseline docs, first verification.
- Phase 0.1: workflow adoption for an existing structured project candidate.
- Phase 0.2: planning baseline for an adopted existing structured project.
- Phase N: one coherent major phase after the baseline. It should have one goal, one reviewable
  output set, and one closed verification loop.
- Phase N.x: any one-decimal sub-phase under the current major phase. Phase X.1 and Phase X.2
  are common examples, not the complete boundary.
- Phase X.1: common small scoped addition example under the current major phase.
- Phase X.2: common bug fix or correction example within the current phase boundary.
- New Major Phase: a separate capability, direction change, or verification loop that no longer
  fits the current major phase.
- Backlog: useful but non-urgent work that should not interrupt the current phase.

Use one decimal level only. Do not introduce Phase X.N.M. If the change no longer fits under
the current major phase, make it a New Major Phase or backlog item.

## Phase Meanings

### Phase 0

Create the target project baseline. When the target folder is an empty folder, Phase 0 still
starts with a visible Phase 0 start gate. Codex must list the baseline workflow files before
creating any project files. Baseline workflow files include README.md, AGENTS.md, PLAN.md,
TODO.md, and DECISIONS.md.

Before Phase 0, classify folder state as `empty folder`, `existing structured project
candidate`, `existing workflow project`, or `unclear project state`.

If the folder state is `unclear project state`, stop and report why adoption is not recommended
yet. Ask for clarification or recommend a separate project assessment instead of creating
workflow files.

For an existing workflow project, recover compact current state from project files before
proposing the next phase gate.

### Phase 0.1

Use Phase 0.1 for workflow adoption in an existing structured project candidate. Phase 0.1
creates or fills workflow files and `PROJECT_CONTEXT.md` around the current project state. It
must list detected existing files, detected test/build/smoke commands when available, files to
create or fill, and files not to overwrite.

Phase 0.1 must not overwrite existing project files, plan future feature work, modify
application code, refactor code, or start a cleanup campaign.

`AGENTS.md` and `.codex/hooks.json` are Phase 0 or Phase 0.1 adoption outputs. Create or fill
`.codex/hooks.json` only when optional project-level hook support is selected or explicitly
requested.

### Phase 0.2

Use Phase 0.2 for a planning baseline only after the user separately requests it and provides
or confirms the next project goal. Phase 0.2 uses `PROJECT_CONTEXT.md` and the user-confirmed
goal to update `PLAN.md`, `TODO.md`, and handoff notes with a rough roadmap and candidate
Phase 1 goal. It must not infer the roadmap from code observations alone.

Phase 0.2 allows planning records only: `PLAN.md`, `TODO.md`, phase notes, handoff notes,
planning baselines, roadmaps, and candidate Phase 1 goals. During Phase 0.2 there are no
tests, code skeletons, migrations, file restores, technical implementation, scripts, or
non-planning technical documentation. Non-planning technical documentation includes API docs,
architecture docs, migration guides, usage docs, module docs, or generated technical docs. Do
not treat planning records as technical deliverables. In short: no tests, code skeletons,
migrations, file restores, or technical implementation. After Phase 0.2, stop before Phase 1.

### Phase N

Use Phase N for the next coherent major capability after the previous phase exits cleanly.
Keep the phase focused on one goal and one closed verification loop.

### Phase N.x

Use Phase N.x for one-decimal sub-phases under the active major phase. Create a sub-phase only
after a phase boundary change proposal is confirmed and recorded. A sub-phase does not
authorize work in later sub-phases.

### New Major Phase

Use a New Major Phase when the change adds an independent capability, changes project
direction, requires separate examples or tests, changes acceptance criteria substantially, or
needs a separate verification loop.

### Backlog

Use Backlog for ideas that may be valuable later but are not needed for the current phase.
Backlog items do not authorize implementation.

## Optional Project-Level Hook Reminders

Optional project-level Codex hook support stays reminder-only. The hook may inject context, but
it must not scan the project, recover project state, read workflow files, write files, or invoke
the skill directly. Codex still decides whether `phase-workflow` applies.

`AGENTS.md` and `.codex/hooks.json` are Phase 0 or Phase 0.1 adoption outputs while keeping
their responsibilities separate. Do not overwrite existing files; merge only the
`phase-workflow` `UserPromptSubmit` entry and ask before replacing conflicts. If a
`phase-workflow` hook entry already exists, do not add it again. A conflicting hook command or
hook location requires user confirmation before replacement.

Use an absolute path for the hook command. Do not rely on the hook runner's current working
directory. Restart Codex and re-review/trust the hook after changing the absolute hook command.

Mandatory skill invocation and hook boundary: Open the current `SKILL.md` when
`phase-workflow` applies; hook reminders do not count as invocation. Project `AGENTS.md` rules
and compressed chat history do not replace opening the skill.

## Optional ChatGPT/MCP Planning Boundary

Optional ChatGPT MCP Planning Companion guidance adds an optional planning path without changing
the default Codex-only workflow.

Codex-only remains the default compatible path. Codex reads bounded recovery context from
project files, shows gates, validates authorization, executes commands, and edits files after
confirmation.

ChatGPT/MCP planning with Codex execution is optional. ChatGPT may use a local read-only MCP
companion to read bounded project context and generate a short handoff prompt for Codex. Codex
still validates local files, phase gates, authorization branch, and stop conditions before
execution.

Codex-direct MCP planning is not a supported mode. The local MCP companion does not call Codex,
run `codex exec`, start Codex, or use Codex as a compression backend.

The default snapshot matches bounded Codex recovery context. Read `AGENTS.md`, the needed skill
entry or reference guidance, the first 80-120 lines of the compact handoff or current-state
file when present, and current `TODO.md` sections: current phase, active task, blockers, next
tasks, and do-not-do-yet. Full `PLAN.md`, full `TODO.md`, `DECISIONS.md`, full handoff files,
and phase notes are targeted or on-demand reads. Do not route MCP snapshot reads through Codex.

Use on-demand reads only when planning needs more context. Name a concrete file, heading, or
section for each on-demand read. Do not read the whole project history. Record source refs for
every on-demand read. On-demand reads remain targeted and read-only: do not write files,
execute commands, or route reads through Codex.

The handoff is planning input only, not a source of truth or execution authorization. Do not
include full project history or full file contents. Include a stop condition such as show the
next phase gate only or execute only the current confirmed phase and stop. Codex still
revalidates local files, phase gates, authorization branch, and stop condition before
execution.

Handoff recognition is header-based. Do not infer ChatGPT/MCP handoff mode from natural
language alone. Missing header means ordinary Codex-only conversation. A valid header includes
`phase_workflow_handoff: 1`, `mode: ChatGPT/MCP planning with Codex execution`, `project_id`,
`source_refs`, `snapshot_id`, `requested_action`, and `stop_condition`. `workspace_id` is
required when multiple local checkouts or ambiguity exist. Missing required fields, mismatched
project identity, missing source refs, unclear stop condition, or wrong `mode` fails closed
before execution. A valid handoff remains planning input only, not a source of truth or
execution authorization. Codex must revalidate local files, phase gates, authorization branch,
and stop condition before execution.

Direct conversation with Codex remains Codex-only. Codex must not route its own planning,
recovery reads, local validation, command execution, or file mutations through MCP. MCP is
only for ChatGPT-side planning reads. Codex may configure, start, check status, and stop the
local MCP companion after user confirmation, but service management does not make Codex
planning use MCP.

`project_id` selects the project. `workspace_id` distinguishes local checkouts. `display_name`
is human-facing only. Do not use `display_name` as an identity anchor. The setup card is
connector configuration guidance, not execution authorization.

Explicit user request is required before creating or updating project MCP configuration or the
local registry. Project-local MCP config lives under `.phase-workflow/mcp/project.json`. The
project config stores `schema_version`, `project_id`, `display_name`, and `allowed_files`.
The project config must not store the local absolute `workspace_root`. The local MCP registry
lives at `~/.phase-workflow/mcp/registry.json`. The local registry stores `project_id`,
`workspace_id`, `workspace_root`, port, endpoint, and PID or lock metadata. `project_id` is
generated once for the project and stored in project config. `workspace_id` is generated per
local checkout and stored in the local registry. Missing or ambiguous `project_id` or
`workspace_id` fails closed. Configuration writes stay inside the selected project and the
documented local registry path.

Lifecycle controls remain start, status, and stop only. Bind to loopback by default. Track the
running process with a PID or lock file. Report port conflicts explicitly. Fail closed when
`project_id` is missing, unknown, or ambiguous. ChatGPT must not start Codex, start the local
companion, or execute project commands.

### Built-In Read-Only MCP Companion

For projects that have adopted `phase-workflow`, use the built-in read-only MCP companion only
when the user explicitly asks to enable optional ChatGPT/MCP planning for that project.

Use `scripts/phase_mcp_lifecycle.py` for configure/start/status/stop only after explicit user
request and confirmation. Use `scripts/phase_mcp_setup_output.py` after the selected workspace
reports `running` to prepare ChatGPT setup guidance and a starter ChatGPT planning prompt.

Do not hard-code unstable ChatGPT product UI steps; provide endpoint, project identity,
workspace identity, allowed files summary, and starter prompt. The final Codex handoff is
ChatGPT output after MCP-assisted planning, not Codex configuration output.

Do not make Codex read, plan, validate, execute, or mutate files through MCP. Direct Codex
conversation remains Codex-only unless a valid ChatGPT/MCP handoff header is pasted back and
passes local validation.

## Compact Recovery And Handoff

Compact recovery is the default: start with `AGENTS.md`, the first 80-120 lines of the latest
compact handoff or current-state file when present, and current `TODO.md` sections. Full plans,
decision logs, project context, handoff files, and phase notes are targeted or on-demand
sources.

Use `rg` or scoped section reads for heavier files. Use `rg` to inspect `PLAN.md`,
`DECISIONS.md`, `PROJECT_CONTEXT.md`, or phase notes only when compact state is missing,
conflicting, or explicitly requested. Read older entries only when scope changes, conflicts,
missing verification, unclear decision sources, or explicit history requests require them.

The compact handoff/current-state file is not a complete history, audit log, phase table, or
`PLAN.md` summary. Historical completed task lists belong in phase notes, not in the default
`TODO.md` recovery area.

`PROJECT_CONTEXT.md` is an adoption/background baseline, not a routine status file. Update it
only when stable project identity, directory responsibilities, verification commands, or
durable boundaries change.

`DECISIONS.md` is for durable decisions only. Do not record ordinary phase completion,
verification logs, or execution history there.

`DEV_LOG.md` is not a baseline workflow file, default recovery source, end-of-round record, or
recovery repair target. Legacy `DEV_LOG.md` files may remain in adopted projects, but the
workflow no longer requires creating, reading, or updating them.

Phase-exit and end-of-round record updates use the same bounded context rule. Do not read full
`PLAN.md`, `TODO.md`, `DECISIONS.md`, `PROJECT_CONTEXT.md`, full handoff files, or full phase
notes just to update status records. For `TODO.md`, read and update only the current phase,
active task, blocked, next task, and do-not-do sections. For `PLAN.md`, use `rg` or
heading-scoped reads to locate the relevant phase only when phase boundaries, scope, or roadmap
entries change. For `PROJECT_CONTEXT.md`, use scoped reads only for adoption or stable baseline
changes. For handoff and phase notes, read only the relevant heading or the first 80-120 lines
unless a conflict requires more context.

## Authorization Model

Use this single authorization model before the detailed phase-boundary rules below. When two
signals conflict, the narrower authorization controls and Codex must stop at the next required
gate.

| Signal | Authorizes | Does not authorize | Required stop |
| --- | --- | --- | --- |
| Plan-change confirmation | planning-file updates only | Technical files, fixtures, tests, implementation, scripts, migrations, or restores | Stop after planning files |
| Phase start request | phase analysis and visible start gate only | Execution, file edits, or current-phase mutations | Stop after the gate |
| Post-gate execution confirmation | current-phase technical mutations that pass mutation preflight | Next-phase work, multi-phase execution, planning-file mutations, recovery-record mutations, or unstated approach choices | Stop when the current phase exits |
| Approach confirmation | approved non-trivial approach inside the current phase | Phase boundary changes or broader scope | Stop if the approach is rejected |
| Mutation preflight pass | The checked current-phase mutation branch | Failed-gate, unconfirmed, wrong-branch, next-phase, or multi-phase mutations | Stop before files if any check fails |
| Phase violation detected | read-only recovery audit and chat-visible incident report before user choice; recovery record repairs after user choice | New implementation, next-feature work, continuing the violated flow, or pre-choice record repair | Stop before record repairs until the user chooses keep-and-audit or rollback |

Plan-change confirmation, phase start request, post-gate execution confirmation, approach
confirmation, mutation preflight, and phase violation recovery are separate controls. They
cannot substitute for each other and do not authorize multi-phase execution. A successful
authorization does not authorize next-phase work and does not authorize multi-phase execution.
Do not use the phase violation row to write recovery record repairs before user choice.

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
`multi-phase migration complete`; each phase must have separate status, verification, and
handoff records.

## Mutation Preflight

Before repository mutations, run a mutation preflight. Repository mutations include file
writes, deletes, moves, restores, generated tests, generated docs, scripts, migrations, and
implementation changes. Any work that changes repository files must pass mutation preflight
before modifying files.

Mutation Authorization Branches:

- A planning-file mutation requires plan-change confirmation and planning-file scope only; it
  does not require post-gate execution confirmation.
- A recovery audit before user choice is read-only and may produce only a chat-visible
  incident report.
- A recovery-record mutation requires Phase Violation Recovery and the user's keep-or-rollback
  choice. After the user chooses, recovery-record mutations may repair `PLAN.md`, `TODO.md`,
  phase notes, and handoff records.
- A status/handoff-record mutation requires current phase execution or phase exit context. It
  can update `TODO.md`, phase notes, handoff notes, and `DECISIONS.md` when recording a
  durable decision already made inside the authorized phase or phase exit context.
  It must record actual verification results when claiming completion or test status. If
  verification has not run, record that status honestly and do not claim completion or passing
  tests. It can update blocker, unfinished status, handoff, or current-state records without a
  fresh verification command when no completion or test status is claimed. It does not
  authorize plan changes, new strategy decisions, technical implementation, or recovery repair.
- A technical mutation requires visible phase start gate, post-gate execution confirmation,
  and mutation preflight.
- If the mutation type is unclear, stop before mutating files.

Post-gate execution confirmation authorizes technical mutations only. It does not authorize
planning-file mutations or recovery-record mutations. Planning-file mutations use plan-change
confirmation. Recovery-record mutations use Phase Violation Recovery.

Classify mutation branches by change intent and content, not by file name alone. `TODO.md`,
phase notes, and handoff notes can contain planning-file mutations or status/handoff-record
mutations. Scope, phase boundary, active task, acceptance criteria, or roadmap changes are
planning-file mutations. Verification results, current status, and handoff summaries are
status/handoff-record mutations.

Do not apply technical mutation gate checks to planning-file mutations or recovery-record
mutations; visible phase start gate and post-gate execution confirmation are technical
mutation checks.

Planning-file mutation checks:

- What planning change has the user confirmed?
- Is every changed file a planning file or planning note?
- Will the work stop after planning-file updates?
- Would this mutation complete multiple phases at once?

Recovery-record mutation checks:

- Is Phase Violation Recovery open?
- Has the user chosen keep implementation and backfill audit, or roll back selected changes?
- Is the mutation limited to repairing planning, phase, and handoff records?
- Does the mutation avoid new implementation?

Status/handoff-record mutation checks:

- Is the update reporting current phase execution, verification, blocker, unfinished status,
  handoff, or current-state status?
- Is it limited to `TODO.md`, phase notes, handoff notes, or a narrow `DECISIONS.md` update?
- Is any `DECISIONS.md` update limited to recording a durable decision already made inside the
  authorized phase or phase exit context?
- Are actual verification results recorded when completion or test status is claimed?
- If verification has not run, does the record say so without claiming completion or passing
  tests?
- Does it avoid plan changes, technical implementation, and recovery repair?

Technical mutation checks:

- What is the current phase?
- Has the visible phase start gate been shown?
- Is there a separate post-gate execution confirmation?
- Does this mutation belong only to the current phase?
- Would this mutation complete multiple phases at once?

If any answer fails, stop before mutating files. Do not use one mutation to complete multiple
phases; split the work or return to the appropriate phase gate.

Plan-change confirmation only authorizes planning-file updates, then stop. It does not
authorize tests, code, scripts, migrations, restores, or other technical files.

## Phase Violation Recovery

Use Phase Violation Recovery when an approved phase boundary has already been crossed. This is
a mandatory recovery flow, not permission to continue implementation.

When a violation is discovered, stop new implementation immediately, do not continue to the
next feature, and do not keep implementing while recovery is open. Before the user chooses
keep-and-audit or rollback, recovery audit is read-only. Audit files and records changed
outside the approved phase boundary as a read-only step. Use a chat-visible incident report to
mark `implementation happened outside approved phase boundary`. The chat-visible incident
report should record which files, tests, migrations, restores, docs, and status records were
affected.

Ask the user to choose between keeping implementation and backfilling the audit, or rolling
back selected changes. Do not write recovery record repairs before the user chooses. After the
user chooses, recovery-record mutations may repair `PLAN.md`, `TODO.md`, phase notes, and
handoff records. The goal is to make the state honest and recoverable so a new Codex session
can resume without chat history.

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

Scope-changing work must update planning files before technical files. After a phase start gate
and separate user confirmation, the first file changes for new phases, sub-phases, phase
splits, New Major Phase work, route changes, or acceptance criteria changes should update
`PLAN.md`, `TODO.md`, and any relevant phase note, handoff note, `PROJECT_CONTEXT.md`, or
`DECISIONS.md`.

Do not start fixtures, tests, implementation, or other technical file changes before the
relevant plan record exists. Do not treat `PLAN.md` or `TODO.md` as after-the-fact summaries
for scope-changing work. Prohibited order: Implement first, document plan later.

Verification results, actual modified file lists, phase note updates, handoff summaries, and
small non-scope-changing corrections can be recorded after technical work.

## Phase Boundary Change Confirmation

Any phase split is a phase boundary change, regardless of whether the split is requested by the
user or recommended by Codex. Use one split flow for both sources. Phase boundary changes
include splits, any one-decimal Phase X.N sub-phase, New Major Phase work, Backlog moves, and
phase goal, non-goal, acceptance criteria, or verification loop changes. Phase X.1 and Phase
X.2 are common examples, not the complete boundary.

When Codex recommends a split, it must propose the complete currently visible sub-phase
structure before asking for confirmation. The proposal must assign Phase X.1, Phase X.2, and
later one-decimal numbers to known follow-up sub-phases, and mark uncertain or out-of-scope
work as later phase work or Backlog. Do not create only the immediate next Phase X.1 and route
the user directly to the Phase X.1 start gate.

When Codex proposes a new Phase X.N, it must:

1. Explain why the sub-phase is needed.
2. Show a split interpretation or phase boundary change proposal.
3. Ask the user to confirm the planning change before updating planning files.
4. If confirmed, update `PLAN.md`, `TODO.md`, and any relevant phase note.
5. Stop.
6. Show the already-recorded Phase X.N start gate only after a later user request.

After confirmed planning-file updates, Codex stops before showing the new phase or sub-phase
start gate. Use one decimal level only; do not introduce Phase X.N.M.

After plan-change update, a later request to start, continue, enter, or execute the
already-recorded Phase X.N only authorizes the phase start gate. It does not authorize
execution. The start gate must stop before execution and wait for post-gate execution
confirmation.

Plan-change confirmation, phase start request, and post-gate execution confirmation cannot
substitute for each other.

## Plan Mode Skill Invocation Guard

Plan Mode is optional. When Plan Mode is enabled and the task is covered by this workflow,
Codex must activate and follow phase-workflow first.

Plan Mode cannot bypass phase-workflow activation, phase boundary change checks, phase start
gates, or post-gate execution confirmation. In Plan Mode, plan, phase, scope, or design-change
requests still require `phase-workflow` classification before returning a proposed plan.

Plan Mode proposed plan cannot substitute for plan-change confirmation, phase start request,
and post-gate execution confirmation. Plan Mode does not authorize execution.

## Reviewable Split Policy

A split can be justified by reviewability, transparency, phase size, risk, user confidence,
avoiding opaque large phases, multiple independent outputs, unrelated user-visible
capabilities, or separate verification loops.

Any phase split is a phase boundary change, regardless of whether the split is requested by the
user or recommended by Codex. Use one split flow for both sources. Codex should interpret the
requested or recommended split, output the proposed Phase X.N boundary, and wait for user
confirmation.

When Codex recommends a split, it must propose the complete currently visible sub-phase
structure before asking for confirmation. The proposal must assign Phase X.1, Phase X.2, and
later one-decimal numbers to known follow-up sub-phases, and mark uncertain or out-of-scope
work as later phase work or Backlog. Do not create only the immediate next Phase X.1 and route
the user directly to the Phase X.1 start gate.

Split flow:

1. Recommend or interpret the split.
2. Show a split interpretation or phase boundary change proposal.
3. Ask the user to confirm the planning change before updating planning files.
4. Wait for user confirmation of the split boundary.
5. Update planning files such as `PLAN.md`, `TODO.md`, and the active phase note.
6. Stop.
7. Show the next phase or sub-phase start gate only after the user asks to continue.

Split confirmation only authorizes planning-file updates, then stop. It does not authorize
Phase X.N execution, fixtures, tests, implementation, or other technical file changes.

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
- The phase note records historical scope, files, tests, risks, and next steps.
- The handoff note lets a new Codex session continue without chat history.
- `DECISIONS.md` records durable decisions only.
- Scope expansion is either absent or documented as a change request.
- Record updates should use scoped reads, not default full-file reads.

## Avoiding Scope Creep

- Write non-goals at phase start.
- Treat "while we are here" ideas as change requests.
- Move new capabilities to a future phase.
- Put useful but non-urgent ideas in Backlog.
- Do not implement unplanned features because they seem small.
- Update `DECISIONS.md` when the long-term strategy changes.

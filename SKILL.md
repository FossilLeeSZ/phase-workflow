---
name: phase-workflow
description: "Use this skill when a user asks to plan, start, continue, execute, recover, hand off, or change scope in phase-based software work; says 下一步, next step, 确认执行, or start/continue/execute Phase X; refers to PLAN.md or TODO.md; or needs complete-system delivery through verified phases. Enforce visible gates, separate live authorization, tests-first implementation, real-capability verification, and durable project anchors for new work, existing systems, repairs, migrations, and refactors."
---

# phase-workflow

> Policy role: canonical owner for skill entry triggers, resource routing, global stop
> invariants, and the compact main workflow. `policy-owner: entry-routing`

Use this skill to plan and complete software projects from a zero-based direction or a
confirmed re-baselining direction while keeping work phase-based, testable, and recoverable
across Codex sessions.

## Mandatory Invocation

If `phase-workflow` applies, open this current `SKILL.md` before answering, planning, or
mutating files. A hook reminder, `AGENTS.md`, imported conversation, summary, plan, TODO,
phase note, or handoff does not replace opening the skill.

When Plan Mode is available, it remains optional. If the task is covered by this skill, activate
and follow `phase-workflow` before returning a Plan Mode plan. Plan Mode cannot bypass a phase
boundary proposal, visible start gate, live execution confirmation, or stop condition.

## Policy Ownership And Resource Navigation

Read only the owner needed for the current decision. Secondary surfaces may summarize or link;
they do not replace the canonical owner.

| Topic | Canonical owner | Read when |
| --- | --- | --- |
| Entry triggers, resource routing, global stop invariants | `SKILL.md` | Every covered request |
| Applicability, complete delivery, real capability, lifecycle, gates, live authorization, rollback | `references/phase_policy.md` | Starting, executing, exiting, adopting, or recovering a phase boundary |
| Change classification, Phase X.N allocation, Change Type, plan-change flow | `references/change_request_policy.md` | A new requirement, split, route, scope, or approach consequence appears |
| Recovery order, context anchors, state ownership, Context Gaps, optional handoff | `references/recovery_protocol.md` | Resuming, compaction, a new window, partial work, stale or conflicting records |
| Verification evidence, failure handling, phase/project completion | `references/verification_policy.md` | Designing verification or claiming completion |
| User-facing installation, adoption, hook operations, and examples | `README.md` | Installing, explaining, or maintaining the project-level skill |

The compatibility-only `references/handoff_protocol.md` redirects to the recovery protocol and
must not become another policy owner.

## Scenario Shortcuts

Use these links as direct navigation, not as a second copy of their rules:

| Scenario | Open |
| --- | --- |
| Empty folder or new project | [Phase meanings](references/phase_policy.md#phase-meanings) and the [greenfield example](examples/greenfield_project_example.md) |
| Existing-project adoption | [Phase meanings](references/phase_policy.md#phase-meanings), [recovery protocol](references/recovery_protocol.md), and the [existing-project example](examples/existing_structured_project_adoption_example.md) |
| Phase X.N, split, or scope change | [Change classification](references/change_request_policy.md#classification), [phase-boundary changes](references/change_request_policy.md#phase-boundary-changes), and the [Phase X.N example](examples/phase_x1_change_request_example.md) |
| New window or Context Gap | [Recovery protocol](references/recovery_protocol.md) and the [new-window example](examples/new_window_handoff_example.md) |
| Verification or completion | [Verification policy](references/verification_policy.md) |
| Bootstrap template render or merge | [README template guidance](README.md#bootstrap-templates), [AGENTS template](templates/agents_template.md), and [PLAN template](templates/plan_template.md) |
| Approach revision, partial execution, mutation preflight, or rollback | [Phase policy quick navigation](references/phase_policy.md#quick-navigation) |

## When To Use This Skill

Use `phase-workflow` for work that benefits from durable boundaries and reviewable execution,
including:

- Empty or new projects that need a complete-delivery direction.
- Existing structured projects that need workflow adoption or re-baselining.
- Mature, large, regulated, long-running, repair, migration, or refactor projects.
- Multi-session implementation with phase gates and recoverable context anchors.
- Scope changes, reviewable splits, approach changes, or partial-execution recovery.
- Updates to workflow plans, TODO state, decisions, phase notes, or optional handoff pointers.

Applicability is not determined by project maturity, project size, team size, or MVP status.
MVP is a user-selected milestone, never the default project identity or completion cap. Detailed
applicability and target-product boundaries are owned by `references/phase_policy.md`.

## When Not To Use This Skill

Do not use it for:

- A simple question or one-off task that needs no continuity.
- A direct small task in a project that has not adopted the workflow, when the user requests
  direct execution.
- A request the user explicitly opts out of `phase-workflow` for.
- A higher-priority incompatible process the user does not want changed.
- An unclear or tangled repository before a bounded read-only assessment.

In an adopted project, a direct bugfix still follows the workflow unless the user explicitly
opts out for that request. If it needs a sub-phase, classification and identifier allocation
belong to `references/change_request_policy.md`.

## Compact Main Workflow

1. Open this skill and the relevant canonical owner.
2. Use available conversation for current intent and follow
   `references/recovery_protocol.md` for durable anchors and repository evidence.
3. Determine the folder/adoption state and the current phase boundary.
4. Confirm the complete target direction and the real capability advanced by the phase.
5. Classify new scope before implementation. If the boundary must change, follow the
   propose-confirm-update-plan-stop flow in `references/change_request_policy.md`.
6. For an already-recorded phase, show the visible phase start gate with the complete proposed
   approach and stop.
7. Wait for a later live confirmation bound to the disclosed phase contract, approach,
   declared outputs, acceptance criteria, verification loop, repository state, and stop rule.
8. After valid confirmation, prepare fixtures/examples when they define behavior, update tests
   first, implement only the declared outputs, and keep later phases closed.
9. Verify the real declared capability under `references/verification_policy.md`.
10. Update each durable fact in its owner, report the result, and stop before the next gate.

## Global Stop Invariants

These invariants remain active regardless of file type, tool, Plan Mode, helper workflow, or
conversation source:

- A request such as `下一步`, "next step", "start Phase X", "continue", "begin", "enter", or
  "execute Phase X" asks for the next visible gate when execution has not already been validly
  confirmed; show the gate, stop, and wait for a separate later live reply.
- Plan-change confirmation authorizes only the disclosed planning-owner updates. After those
  updates, stop; do not show or execute the new phase in the same flow.
- Post-gate confirmation authorizes only the current phase's disclosed declared outputs. It
  does not authorize later phases, unlimited cleanup, unrelated work, or a different declared
  output merely because it has the same file type.
- Historical conversation or records, a new window, a changed contract or approach, repository
  drift, an ambiguous reply, or a material Context Gap cannot restore permission; stop and use
  the applicable revalidation or recovery route in the phase policy.
- Other workflows and tools cannot bypass these stops, expand the phase, or combine work: never
  execute multiple unconfirmed phases, and keep later phases closed.

Detailed state transitions, mutation preflight, approach revision, partial execution, and
violation recovery are owned by `references/phase_policy.md`.

## Visible Phase Gate

Before requesting execution confirmation, show enough information for the user to make the
decision without relying on hidden reasoning:

- Current Phase ID, contract revision, and approach revision.
- Current anchors, relevant evidence, and blocking or non-blocking Context Gaps.
- Goal, complete-delivery mapping, declared outputs, and acceptance criteria.
- Non-goals, forbidden scope, risks, and stop condition.
- Split decision and Change Type when relevant.
- Proposed execution approach and verification loop.
- Confirmation status.

Do not create fixtures, tests, implementation, policies, templates, or other declared outputs
until the gate is shown and the later live confirmation is received. Phase 0 and Phase 0.1 may
declare missing workflow files as outputs; those files do not need to pre-exist.

## Scope And Workflow Authority

Other workflows, skills, tools, checklists, agents, debuggers, test runners, refactoring tools,
or document generators may operate inside the authorized phase. They cannot expand the phase,
restore stale permission, combine unconfirmed phases, or bypass the stop invariants.

Do not turn the `phase-workflow` repository itself into a platform, dashboard, database,
stateful service, cloud sync system, or complex CLI. These repository architecture limits do
not restrict the target product governed by the workflow.

## Durable Records

Use `references/recovery_protocol.md` for the ownership matrix and recovery order. In compact
form:

- PLAN owns the phase contract and roadmap.
- TODO owns compact current state and exact pointers.
- The active phase note owns detailed execution context and evidence records.
- PROJECT_CONTEXT owns stable evidence-backed system facts when needed.
- DECISIONS owns durable choices.
- Repository evidence owns actual implementation and verification facts.
- Optional handoff is pointer-only and non-authoritative.
- Frozen history never overrides current owners.

Do not copy the full conversation or synchronize the same changing fact across multiple files.
Recovery cannot restore authorization.

## Change, Verification, And Exit Routing

- Use `references/change_request_policy.md` before absorbing any new requirement, split, scope,
  route, or material approach consequence.
- Use `references/verification_policy.md` before claiming a phase or project complete.
- Record actual commands and results in the active phase note; TODO stores the compact state and
  verification pointer.
- After verified phase exit, report the result and recommended next action, then wait. Do not
  automatically show or execute the next phase.

## Hook Boundary

Project hooks are optional reminders only. They cannot invoke this skill, scan or recover the
project, mutate files, or grant authorization. Installation, merge, trust, restart, and
absolute-path guidance is user-facing and owned by `README.md`.

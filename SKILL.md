---
name: phase-workflow
description: "Use this skill when a user asks to plan, start, continue, execute, recover, hand off, or change scope in phase-based software work; asks to grill or stress-test a material decision; says 下一步, next step, 确认执行, grill me, or start/continue/execute Phase X; refers to PLAN.md or TODO.md; or needs complete-system delivery through verified phases. Enforce visible gates, separate live authorization, tests-first implementation, real-capability verification, and durable project anchors for new work, existing systems, repairs, migrations, and refactors."
---

# phase-workflow

> Policy role: canonical owner for skill entry triggers, resource routing, global stop
> invariants, and the compact main workflow. `policy-owner: entry-routing`

Plan complete systems through reviewable, verified phases with durable recovery anchors.

## Mandatory Invocation

When this skill applies, open the current `SKILL.md` before answering, planning, or mutating
files. Hooks, repository instructions, conversation summaries, plans, phase notes, and handoffs
cannot replace skill activation or grant authorization.

Plan Mode remains optional. It cannot bypass skill activation, a phase-boundary proposal, the
visible start gate, live execution confirmation, or any required stop.

## Policy Routing

Read only the canonical owner and direct supporting resource needed for the current decision.
Secondary surfaces may summarize or link but cannot become another policy owner.
Keep detailed rules in their routed owner instead of restating them in this entry.

| Scenario or topic | Open | Use for |
| --- | --- | --- |
| Every covered request | `SKILL.md` | Entry triggers, routing, compact workflow, and global stops |
| Empty folder or new project | [Phase meanings](references/phase_policy.md#phase-meanings) and [greenfield example](examples/greenfield_project_example.md) | Phase 0 and complete-delivery startup |
| Existing-project adoption | [Phase meanings](references/phase_policy.md#phase-meanings), [recovery protocol](references/recovery_protocol.md), and [adoption example](examples/existing_structured_project_adoption_example.md) | Phase 0.1, re-baselining, and evidence-first adoption |
| Phase boundary, execution, exit, approach revision, partial work, or rollback | [Phase policy](references/phase_policy.md) | Applicability, lifecycle, real capability, visible gates, live authorization, and mutation preflight |
| Phase X.N, split, or scope change | [Change policy](references/change_request_policy.md#classification) and [Phase X.N example](examples/phase_x1_change_request_example.md) | Classification, numbering, Change Type, and plan-change flow |
| Grill, stress-test, or material unresolved user decision | [Shared-understanding protocol](references/shared_understanding_protocol.md) and [interview example](examples/shared_understanding_interview_example.md) | Optional fact-first interview, one decision per turn, bounded closure, and non-authorization |
| New window or Context Gap | [Recovery protocol](references/recovery_protocol.md) and [new-window example](examples/new_window_handoff_example.md) | Exact anchors, state ownership, conflict handling, and optional handoff |
| Verification or completion | [Verification policy](references/verification_policy.md) | Evidence, failure handling, and phase versus project completion |
| Bootstrap template render or merge | [README](README.md#bootstrap-templates), [AGENTS template](templates/agents_template.md), and [PLAN template](templates/plan_template.md) | Installation, adoption, hook operations, and template use |

The compatibility-only `references/handoff_protocol.md` redirects to the recovery protocol and
must not become another policy owner.

## Compact Main Workflow

1. Open this skill and the relevant canonical owner.
2. Use available conversation for current intent; recover exact anchors and Context Gaps under
   `references/recovery_protocol.md`, and treat repository evidence as actual state only.
3. Determine adoption state and current phase, then confirm the complete target and real
   capability under `references/phase_policy.md`.
4. Classify new scope before implementation. For a boundary change, use the
   propose-confirm-update-plan-stop flow in `references/change_request_policy.md`.
5. For a recorded phase, disclose the complete gate and approach, stop, and wait for a later
   live confirmation bound to that contract and the revalidated repository state.
6. After valid confirmation and mutation preflight, update tests first, change only declared
   outputs, and keep later phases closed.
7. Verify the declared capability under `references/verification_policy.md`, update each fact in
   its canonical owner, report the result, and stop before the next phase gate.

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

Detailed lifecycle states, visible-gate fields, mutation preflight, approach revision, partial
execution, rollback, applicability, records, and hook boundaries remain owned by the routed
policies and `README.md`. Other workflows, tools, hooks, and Plan Mode cannot bypass these
stops, cannot expand the phase or authorization, cannot combine unconfirmed phases, and cannot
replace their canonical owners.

<!-- BEGIN PHASE-WORKFLOW TEMPLATE METADATA -->
<!--
Template role: structural, not authoritative.
Render target: target project root `PLAN.md`.
Canonical skill root: `.agents/skills/phase-workflow`.

Render only when `PLAN.md` is a declared Phase 0 or Phase 0.1 output and a separate live
confirmation follows the visible gate. Remove this metadata block, replace every `{{...}}`
placeholder, and rewrite `../SKILL.md` and `../references/...` links to the canonical skill root.

If the target already exists, do not overwrite it. Render a candidate, compare and
merge section by section, preserve existing project meaning and phase history, and stop with a blocking Context
Gap when a material target, boundary, acceptance, or safety conflict cannot be resolved.

For Phase 0.1 adoption, an unknown future target must be written as `Not yet confirmed; requires
separately gated Phase 0.2`, not inferred from code or left as a misleading completed roadmap.
-->
<!-- END PHASE-WORKFLOW TEMPLATE METADATA -->
# PLAN.md

This plan follows the [phase-workflow skill](../SKILL.md). The
[phase policy](../references/phase_policy.md) owns lifecycle and complete-delivery semantics; the
[change-request policy](../references/change_request_policy.md) owns classification and planning
boundary changes; the [recovery protocol](../references/recovery_protocol.md) owns state
responsibilities; and the [verification policy](../references/verification_policy.md) owns
completion evidence.

## Project Direction

- Project: {{PROJECT_NAME}}
- Project goal: {{PROJECT_GOAL}}
- Target-system boundary: {{TARGET_SYSTEM_BOUNDARY}}
- Project-level completion target: {{PROJECT_COMPLETION_TARGET}}
- Complete-delivery path: {{COMPLETE_DELIVERY_PATH}}
- Durable constraints: {{DURABLE_CONSTRAINTS}}
- Non-goals: {{NON_GOALS}}
- User-selected intermediate milestones: {{USER_SELECTED_MILESTONES}}

An intermediate milestone such as an MVP does not replace the complete target system, become the
default project identity, or establish project completion by itself.

## Complete-Delivery Map

| Required real capability | Project completion criterion advanced | Planned phase | Verification evidence |
| --- | --- | --- | --- |
| {{REAL_CAPABILITY}} | {{COMPLETION_CRITERION}} | Phase {{PHASE_ID}} | {{VERIFICATION_EVIDENCE}} |

Fixtures, tests, scaffolding, and documentation do not substitute for runtime capability when a
phase promises runtime behavior. Documentation is the real deliverable only when the phase
contract explicitly declares it as the product and verifies its consumer-facing result.

## Phase Map

- Phase {{PHASE_ID}}: {{PHASE_NAME}} — {{PHASE_GOAL}}
- Add later candidate phases only when their dependency and complete-delivery mapping are known.
- Keep unconfirmed future goals explicitly unconfirmed rather than inventing a roadmap.

## Phase {{PHASE_ID}}: {{PHASE_NAME}}

- phase-contract revision: {{CONTRACT_REVISION}}
- Change Type: {{CHANGE_TYPE}}
- Goal: {{PHASE_GOAL}}
- Project completion criterion advanced: {{PHASE_COMPLETION_CRITERION}}
- Dependencies: {{DEPENDENCIES}}
- Boundary: {{PHASE_BOUNDARY}}
- Non-goals: {{PHASE_NON_GOALS}}
- Declared inputs: {{DECLARED_INPUTS}}
- Lifecycle-coupled artifacts: {{LIFECYCLE_COUPLED_ARTIFACTS}}
- Declared outputs: {{DECLARED_OUTPUTS}}
- Acceptance criteria: {{ACCEPTANCE_CRITERIA}}
- Verification: {{VERIFICATION}}
- Risks: {{RISKS}}
- Stop rule: {{STOP_RULE}}

Exit criteria:

- The declared outputs meet the acceptance criteria under actual verification.
- The active phase note records detailed approach, modified files, commands, results, deviations,
  and remaining Context Gaps.
- TODO points to the current owners and the workflow stops before the next phase gate.

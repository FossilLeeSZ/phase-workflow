<!-- BEGIN PHASE-WORKFLOW TEMPLATE METADATA -->
<!--
Template role: structural, not authoritative.
Render target: target project root `AGENTS.md`.
Canonical skill root: `.agents/skills/phase-workflow`.

Render only when `AGENTS.md` is a declared Phase 0 or Phase 0.1 output and a separate live
confirmation follows the visible gate. Remove this metadata block, replace every `{{...}}`
placeholder, and rewrite `../SKILL.md` and `../references/...` links to the canonical skill root.

If the target already exists, do not overwrite it. Render a candidate, compare and
merge section by section, preserve existing project meaning and the instruction hierarchy, and stop with a
blocking Context Gap when a material conflict cannot be resolved safely.
-->
<!-- END PHASE-WORKFLOW TEMPLATE METADATA -->
# AGENTS.md

## Project Purpose

- Project: {{PROJECT_NAME}}
- Purpose: {{PROJECT_PURPOSE}}

## Skill Activation

This repository uses the [phase-workflow skill](../SKILL.md) for work that needs durable phase
boundaries, reviewable execution, and cross-task recovery. When it applies, open the current
skill before planning, showing a gate, confirming execution, changing scope, or mutating files.

Use the [phase policy](../references/phase_policy.md) for lifecycle and authorization outcomes,
and the [recovery protocol](../references/recovery_protocol.md) for current anchors and Context
Gaps. Do not reproduce their detailed rules in this file.

## Long-Term Repository Rules

- {{LONG_TERM_RULES}}
- Keep instructions durable and repository-wide. Current phase, status, blockers, next action,
  command results, and authorization state belong to their workflow owners, not this file.

## Context And Recovery

- Use relevant available conversation for current intent and corrections.
- Use PLAN for the phase contract, TODO for compact current state, the active phase note for
  detailed execution evidence, and repository evidence for actual implementation state.
- A file, summary, handoff, or old confirmation cannot grant execution authorization.
- When a material Context Gap affects outputs, acceptance, approach, or safety, stop rather than
  guessing.

## Repository Boundaries

- {{REPOSITORY_BOUNDARIES}}
- Preserve existing project meaning. Do not broaden a phase, overwrite project instructions, or
  enter a later phase without the applicable workflow transition.

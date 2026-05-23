# Phase Policy

Use this policy to define phase boundaries and keep early-stage work small, explicit, and
verifiable.

## Numbering Rules

- Phase 0: initialization, project skeleton, baseline docs, first verification.
- Phase 1: first real capability or first pass over the core workflow.
- Phase 1.1: small scoped addition to Phase 1 that does not change the main goal.
- Phase 1.2: bug fix or correction within the current phase boundary.
- Phase 2: next independent capability after Phase 1 exits cleanly.
- Phase 5: phase start gate and split confirmation bug fix based on real use.
- Phase 5.1: visible phase start gate before fixtures, tests, or implementation changes.
- Phase 5.2: Phase 0 start gate before creating files in an empty folder.
- Phase 5.3: separate post-gate confirmation before execution.
- Phase 6: README workflow diagram and usage guidance documentation improvement.
- Phase 6.1: pre-release README and plan consistency polish.
- Phase 7: iteration from real early-stage project feedback.

Use one decimal level only. If the change no longer fits as a small addition or bug fix,
make it a New Major Phase or backlog item.

## Phase Meanings

### Phase 0

Create the project baseline. For this repository, that means docs, references, templates,
examples, and minimal tests.

When the target folder is an empty folder, Phase 0 still starts with a visible Phase 0 start
gate. Codex must list the baseline workflow files before creating any project files. Baseline
workflow files include README.md, AGENTS.md, PLAN.md, TODO.md, DEV_LOG.md, and DECISIONS.md.

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

## One Closed Loop Per Phase

Each phase should include:

1. Scope boundary.
2. Fixtures or examples.
3. Failing tests.
4. Minimal implementation.
5. Verification.
6. Documentation and handoff.

Do not start later-phase implementation while the current phase is still open.

## Phase Start Checklist

- What is the current phase?
- Is the previous phase complete and verified?
- Is the target folder an empty folder?
- What is the current phase goal?
- What are the non-goals?
- What is the visible phase start gate summary?
- What is the split decision: keep the phase, use Phase X.1, use Phase X.2, create a New
  Major Phase, or put it in Backlog?
- Is the phase still one single verification loop?
- What inputs are available?
- What outputs must exist?
- What acceptance criteria define completion?
- What work is explicitly not allowed?
- For Phase 0, what baseline workflow files will be created?
- Has the user confirmed the phase boundary?
- A request to start a phase is not confirmation.
- Is the confirmation source a separate user response after the phase start gate is displayed?
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

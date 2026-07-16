# Verification Policy

> Policy role: canonical owner for verification evidence, failed-verification handling, phase
> completion, and project-completion claims. `policy-owner: verification-completion`

Use this policy to decide whether a phase can be marked complete. Every phase needs actual
command-based verification.

Use [phase policy](phase_policy.md) for the declared complete-delivery and phase boundary, and
[recovery protocol](recovery_protocol.md) for evidence ownership and recovery pointers.

## Evidence Role

Code, tests, builds, artifacts, migrations, runtime behavior, and observed command output are
evidence of actual implementation and verification state. They do not define current user
intent, an unconfirmed roadmap, or execution authorization. Verification proves only the
behavior it actually covers.

Current evidence controls current factual status. A current failing command, runtime failure,
or invalid artifact overrides a stale passing result or historical completion record. Preserve
the historical result for audit, but keep the active phase incomplete until current verification
succeeds.

## Default Command

Use this command unless the project defines a more specific test command:

```bash
python -m pytest -q
```

## Rules

- Run the verification command before marking a phase complete.
- Do not use "should run" or "looks correct" as completion standards.
- Record the actual command and result in the active phase note. TODO stores a pointer to the
  latest verification record, not a duplicate result ledger.
- If verification fails, do not mark the phase complete.
- Verify the real user-value or end-to-end capability declared by the phase, not merely the
  existence of an internal mechanism.
- Fixtures, tests, and documents must not substitute for or prove the phase-declared real
  capability or executable behavior merely by existing.
- If a CLI exists, run a smoke test that exercises the CLI entry point.
- If a web app exists, run the relevant build or browser smoke test.
- If the target product includes a database migration, cloud integration, or external service,
  run the applicable migration, integration, contract, or bounded smoke verification.
- If a command cannot be run, record the exact reason and leave the phase open.

Documentation or documents count as the product, declared capability, or phase deliverable only
when explicitly identified that way in the phase boundary. In that case, verify the promised
document semantics, structure, links, examples, and consumer-facing result rather than claiming
an unrelated runtime capability.

Preview, contract-only, stub, fake, smoke, or simulated behavior can be completed only when the
phase boundary, labels, acceptance criteria, and verification all describe that narrower promise.
Do not label such evidence as a connected production or end-to-end capability.

## Phase Versus Project Completion

A passing phase verification establishes only the capability and acceptance criteria declared
for that phase. It does not by itself establish project completion.

Claim project completion only when the current complete-delivery map's project-level completion
criteria have all been satisfied by relevant current evidence. Completing one phase does not
authorize or imply completion of later phases.

## What To Record

Record:

- Command.
- Date.
- Exit status.
- Short result summary.
- Failures or warnings that matter.
- Follow-up task if the command failed.

Example:

```text
Command: python -m pytest -q
Result: 6 passed in 0.05s
Notes: No warnings.
```

## Failed Verification

When verification fails:

1. Keep the phase open.
2. Record the failing command and main failure.
3. Fix the issue using a test-first approach when behavior changes.
4. Run verification again.
5. Update the active phase note with the final result and update TODO's compact status, next
   action, and latest-verification pointer.

The new failure remains the active factual status until a later successful verification replaces
it. Do not use an older passing command or completed phase note to keep an active completion
claim.

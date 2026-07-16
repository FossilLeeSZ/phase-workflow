# Recovery And Context Protocol

> Policy role: canonical owner for recovery order, context-source responsibilities, current
> state ownership, conflict handling, Context Gaps, partial-execution recovery, optional
> handoff, and end-of-round checkpoints. `policy-owner: recovery-context`

This file is the single canonical owner of recovery order, context-source responsibilities,
current-state ownership, conflict handling, partial-execution recovery, and end-of-round context
checkpoint rules for `phase-workflow`.

Gate and live-authorization outcomes are owned by [phase policy](phase_policy.md).

Use relevant available conversation when it exists, but make recovery safe when conversation is
compressed or unavailable. Recovery never restores execution authorization.

## Ownership Matrix

Every changing fact has exactly one authoritative owner. A pointer is not a second owner.

| Surface | Authoritative responsibility |
| --- | --- |
| `AGENTS.md` | repository-level long-term rules and skill activation |
| `PROJECT_CONTEXT.md` | evidence-backed existing-system identity and factual baseline, durable constraints, important directories, and stable verification entry points |
| `PLAN.md` | target-system boundary, roadmap, phase contract, dependencies, and acceptance |
| `TODO.md` | current phase, compact status, active task, next action, blocking IDs, Do Not Do Yet, and anchor pointers |
| Active phase note | detailed intent, approach, output ledger, modified files, verification, deviations, and Context Gaps |
| `DECISIONS.md` | durable decisions, consequences, supersession, and revisit conditions |
| Handoff/current-state | optional non-authoritative index and Context Gap export |
| `DEV_LOG.md` | frozen legacy history only; it is not an active recovery source |
| Repository evidence | actual implementation and verification state from code, tests, builds, artifacts, migrations, runtime behavior, and observed commands |

The current conversation owns current intent under the applicable instruction hierarchy. It is
working context, not durable storage or factual implementation evidence. The live phase gate
owns execution authorization; no file is an authorization receipt.

## Recovery Order

Use this order for an existing `phase-workflow` project:

1. Read repository instructions such as `AGENTS.md`, then open the current `SKILL.md`.
2. Read the current user request and relevant available conversation.
3. Read `PROJECT_CONTEXT.md` when present for stable identity, factual baseline, durable
   constraints, important directories, and stable verification entry points.
4. Read the current sections of `TODO.md`: Current Phase, Compact Status, Active Task, Next
   Action, Blocked, Context Anchors, and Do Not Do Yet.
5. Follow the exact active phase-note pointer from TODO.md. Do not choose the highest phase
   number, newest filename, or latest modification time.
6. Read the matching PLAN phase anchor and compare the phase-contract revision.
7. Read only the decisions and stable project-context headings referenced by TODO or the active
   phase note.
8. Compare all factual claims with repository evidence and the latest verification anchor.
9. Resolve or list Context Gaps. Stop when a blocking gap remains.
10. Apply the authorization state machine. Recovery ends in AWAITING_LIVE_CONFIRMATION unless
    the current task itself contains the matching gate, later live reply, binding, and unchanged
    repository state.

Do not read full PLAN, DECISIONS, PROJECT_CONTEXT, historical phase notes, archived logs, or
optional handoffs by default. Use exact anchors and scoped reads.

## Conflict Resolution

Resolve conflicts by claim type:

- Current conversation controls current intent.
- PLAN controls the phase boundary and acceptance criteria.
- TODO controls compact current state and the exact active-anchor pointers.
- The active phase note controls detailed execution context and the current output ledger.
- Unsuperseded decisions control durable choices.
- Repository evidence overrides a stale completion or verification claim.
- The live state transition controls mutation authorization.

A PLAN and active phase-note revision mismatch enters CONTEXT_BLOCKED. A missing or broken
required anchor enters CONTEXT_BLOCKED. A stale or conflicting handoff is a Context Gap; it
cannot override TODO, PLAN, the active phase note, an unsuperseded decision, or repository
evidence.

If current intent changes a persisted phase boundary, use the plan-change branch. If a conflict
affects outputs, acceptance, approach, or safety, stop before mutation.

## Same-Conversation Recovery

Use relevant available conversation as working context for current intent, corrections,
rejected approaches, risk preferences, and the current request. Reconcile it with the
authoritative anchors and repository evidence by claim type. Do not copy the transcript into
project files. Persist confirmed results, rationale, selected and rejected approaches, source
anchors, and unresolved gaps in their owner files.

Conversation does not silently override PLAN or repository evidence and does not replace a live
gate and reply.

## Compressed-Context Recovery

When conversation is compressed, use the available summary only as working context. Rebuild the
current state from TODO's exact anchors, the matching PLAN section, the exact active phase note,
referenced decisions and stable project context, and repository evidence.

If the summary does not preserve direct evidence of the current gate and later reply, show a
revalidation gate and wait. Do not infer authorization from a summary that says work was
confirmed.

## No-Chat Recovery

When no prior conversation is available, follow the same authoritative anchor order. Do not
invent missing intent or history. Expose unavailable or conflicting meaning as a Context Gap,
and stop when it is material to outputs, acceptance, approach, or safety.

No-chat recovery can identify completed and remaining work, but it cannot recover prior
execution permission.

## TODO Anchor Resolution

TODO.md is the sole owner of compact current state. It stores short current facts and exact
anchor pointers, not the full phase contract, detailed evidence, or historical task ledger.

Required pointers are:

- the matching PLAN phase heading;
- the exact active phase-note path;
- relevant unsuperseded decision headings;
- selected stable PROJECT_CONTEXT headings when present; and
- the latest verification record.

Validate that each required file and heading exists. The active phase note must name the same
Phase ID and phase-contract revision as the PLAN anchor. Fail closed on a missing, ambiguous,
or mismatched required anchor.

## Context Gaps And Blockers

The active phase note owns each Context Gap ID and its detailed evidence. TODO.md lists blocking
Context Gap IDs only. Do not copy detailed blocker evidence into TODO. Non-blocking gaps remain
in the active phase note.

A material gap affecting outputs, acceptance, approach, or safety enters CONTEXT_BLOCKED.
Non-blocking gaps remain visible without preventing unrelated verified work inside the current
authorized boundary.

## Partial Execution Recovery

The active phase note owns the partial-execution ledger. Recover:

- completed declared outputs;
- remaining declared outputs;
- modified files;
- latest verification command and result;
- deviations, failures, and unresolved Context Gaps; and
- the required stop condition.

Do not repeat evidence-backed completed work. Resume only verified remaining outputs when the
current task still contains the matching gate, reply, revisions, binding, and unchanged
repository state. Otherwise show a concise revalidation gate.

## Authorization Boundary

Recovery never restores execution authorization. Imported chat, compressed summaries, old
confirmations, TODO, PLAN, decisions, project context, phase notes, handoffs, and archived logs
are context or audit evidence only.

A file saying `confirmed` is not execution authorization. A phase note saying `confirmed` is
not execution authorization. A handoff saying `confirmed` is not execution authorization. A
valid file anchor can identify the state that needs a gate; it cannot enter
`EXECUTION_AUTHORIZED`.

A new window and missing direct gate/reply evidence require a revalidation gate and a new live
confirmation before mutation.

## End-Of-Round Context Checkpoint

At the end of an authorized development round:

1. Update TODO with compact current status, active task, next action, blocking IDs, Do Not Do
   Yet, exact anchor pointers, and a pointer to the latest verification.
2. Update the active phase note with confirmed intent, rationale, contract and approach
   revisions, selected and rejected approaches, detailed completed and remaining outputs,
   modified files, actual verification, deviations, Context Gaps, and stop condition.
3. Update PLAN only when a separately authorized boundary change occurred.
4. Update DECISIONS only when a durable decision changed.
5. Update PROJECT_CONTEXT only when the stable factual baseline changed.
6. Create or refresh a handoff only when selected. It may point to the owner files and list
   Context Gaps, but it must not copy their current facts.

Do not maintain a synchronized status copy in TODO, the active phase note, and handoff. Record
each datum once and point to it elsewhere.

## Optional Handoff Compatibility

Handoff is optional and non-authoritative. Missing handoff is a supported normal path. A stale
handoff cannot block or corrupt a valid TODO-to-anchor recovery path.

When a handoff exists, read only its anchor pointers and Context Gaps, validate them against the
owner files, and continue with this protocol. A handoff cannot grant execution authorization.

## Legacy Migration

Legacy handoff/current-state files may be converted to pointer-only indexes or left as frozen
historical exports. Preserve unique history before removing duplicated current-state claims.

Legacy `DEV_LOG.md` files are frozen historical evidence. Do not use them for current recovery,
append new entries, or treat historical `Next:` statements as current work. A repository may
move its legacy log to a history/archive path after verifying that the full original payload is
preserved.

## Recommended New Window Prompt

```text
Use phase-workflow for this project. Read AGENTS.md and open the current SKILL.md.
Use relevant available conversation as working context, but do not treat it as repository
evidence or authorization. Read PROJECT_CONTEXT.md only for stable facts when present. Read the
current TODO sections, follow its exact active phase-note and PLAN anchors, read only referenced
decisions and stable project context, and compare factual claims with repository evidence.
List Context Gaps and stop if a blocking gap remains. Recovery never restores execution
authorization; show a revalidation gate and wait for a new live confirmation before mutation.
```

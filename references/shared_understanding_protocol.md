# Shared Understanding Protocol

> Policy role: canonical owner for optional decision grilling, fact-versus-decision routing,
> one-question turns, bounded completion, and interview closure.
> `policy-owner: shared-understanding`

Use this protocol to sharpen a phase plan, approach, or material decision without changing the
workflow's planning or execution authority. Use [phase policy](phase_policy.md) for lifecycle
state and live authorization, [change-request policy](change_request_policy.md) for durable
boundary changes, and [recovery protocol](recovery_protocol.md) for Context Gaps.

## Trigger And Skip Rule

Enter the interview when the user explicitly asks to be grilled or to stress-test a plan,
decision, or idea. It may also be proposed when an unresolved user decision materially affects
phase outputs, acceptance, approach, or safety.

Keep the protocol optional. For an ordinary well-defined phase with no material unresolved user
decision, do not require an interview; proceed through the existing classification and gate
path. When proposing the interview rather than responding to an explicit request, explain the
specific decision it would resolve and let the user decline.

## Fact And Decision Boundary

Before asking a question, investigate facts available from the repository, filesystem, tools,
or existing evidence. Report the relevant finding briefly instead of asking the user to supply
a discoverable fact. If evidence conflicts or is missing, follow the recovery protocol rather
than converting the gap into a preference question.

Leave product, priority, risk, and tradeoff decisions with the user. Distinguish the observed
facts from the recommendation, put the decision to the user, and wait for their answer. Do not
infer a decision from silence, a previous recommendation, or evidence about implementation
state.

## One-Question Turn

Ask one material user decision per turn. Resolve dependencies one by one and wait for the
user's answer before asking the next decision question. Use this compact shape:

- **Question:** State the single decision and its bounded options.
- **Recommendation:** Name the recommended option and why it best fits the known goal.
- **Basis:** Cite the decisive repository facts, constraints, or user-confirmed intent.
- **Tradeoff:** State the principal cost or downside of the recommendation.
- **Uncertainty:** State material uncertainty, or say that none remains for this decision.

Do not bundle multiple decision questions into one turn, hide a second choice inside a
recommendation, or ask for a batch approval. A recommendation is not consent and remains
non-authoritative until the user answers the stated question.

## Bounded Completion

Stop the interview when all of these outcomes are true:

- The goal and boundary are clear enough to record.
- Material decisions affecting the current work are resolved by the user.
- Acceptance criteria and dependencies can be stated without invented meaning.
- Remaining uncertainty is explicitly routed to a Context Gap, later phase, or Backlog.

Do not continue an unbounded interview after those conditions are met. Do not force resolution
of decisions that belong to later work. If a new answer exposes another material dependency,
ask only that next decision; otherwise close the interview and state the remaining route.

## Authorization Boundary

The interview is read-only. Do not mutate planning, documentation, tests, code, or other files
during it unless a separately applicable authorization path has already been completed for
that exact mutation.

`Shared understanding`, `looks good`, interview completion, historical replies, summaries, and
durable records do not count as plan-change confirmation, do not satisfy a phase-start request
or visible phase gate, and do not count as live execution confirmation.

After closure:

1. If a durable plan or scope change is needed, show a separate plan-change proposal and wait
   for its separate confirmation. Update only the authorized planning owners, then stop.
2. A later phase-start request may show the later visible phase gate and must stop again.
3. Only a separate live confirmation matching that gate and a successful mutation preflight
   may authorize its declared outputs.

Never manufacture consent by selecting the recommended answer for the user or by treating a
closure phrase as permission to act.

## Attribution

This independently structured protocol is inspired by Matt Pocock's MIT-licensed
[`grill-me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
and
[`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
skills. The upstream copyright and MIT terms are preserved in [LICENSE](../LICENSE).

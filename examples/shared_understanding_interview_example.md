# Shared Understanding Interview Example

This illustrative exchange follows the canonical
[shared-understanding protocol](../references/shared_understanding_protocol.md). It does not
grant planning or execution authorization.

## Evidence Check

The user asks: “Grill me on whether the next phase should replace the parser or wrap it.” Before
asking a preference question, Codex inspects the repository and reports that the current parser
has 42 passing contract tests, three external callers, and no isolated replacement seam. The
existing PLAN records compatibility as a durable constraint. Codex does not ask the user to
recall those discoverable facts.

## Decision Turn 1

- **Question:** Should the phase preserve all three callers while introducing an adapter seam?
- **Recommendation:** Yes; preserve the callers and introduce the seam first.
- **Basis:** The repository shows three active callers and a confirmed compatibility constraint.
- **Tradeoff:** This adds a small adapter layer before the parser can be replaced cleanly.
- **Uncertainty:** None remains about the current caller inventory.

## User Reply 1

The user chooses to preserve the callers and introduce the adapter seam.

## Decision Turn 2

- **Question:** Should parser replacement remain a later phase after adapter verification?
- **Recommendation:** Yes; make the current phase prove compatibility through the adapter only.
- **Basis:** The first decision fixes the current boundary, while replacement needs a distinct
  migration and verification loop.
- **Tradeoff:** The old parser remains temporarily, so removal is deferred.
- **Uncertainty:** The later replacement strategy is intentionally not decided in this phase.

## User Reply 2

The user chooses a later parser-replacement phase.

## Interview Closure

Shared understanding is reached: the current proposal preserves callers, introduces and verifies
an adapter seam, and defers replacement. No files are changed and no planning mutation occurs.
Codex states that a durable phase-boundary change still needs the separate change-request flow
and stops the interview.

## Later Plan-Change Proposal

In a later user turn, Codex shows the separate plan-change proposal with the affected planning
owners, outputs, acceptance criteria, risks, and stop condition. It waits for confirmation,
updates only the confirmed planning owners, and stops. A still later request is required to show
the phase gate, followed by a separate live execution confirmation before implementation.

## Rejected Patterns

- **Bundled questions:** Asking about compatibility, migration timing, and acceptance in one
  turn prevents one-decision-at-a-time feedback.
- **Undisclosed mutation:** Editing PLAN or code during the interview bypasses the applicable
  authorization path.
- **Manufactured consent:** Treating the recommendation or silence as the user's answer replaces
  user ownership with inference.
- **Unbounded interview:** Continuing after the boundary, material decisions, acceptance, and
  remaining gaps are recordable adds friction without resolving current work.
- **Execution authorization:** Treating “looks good” or shared-understanding closure as permission
  to implement confuses interview completion with the later gate and live confirmation.

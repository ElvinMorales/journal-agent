# Synthetic Walkthrough: Memory and State Proposal Review

This public-safe walkthrough applies `prompts/update-proposal-review.md` to synthetic proposal fixtures. It demonstrates classification and review; it does not write Memory or State.

## Review method

For each candidate, review the destination, durability, evidence, breadth, clinical framing, exact approval, and any State stale trigger. Structured proposals use only one of the separate schemas:

- `schemas/memory-update-proposal.schema.json`
- `schemas/state-update-proposal.schema.json`

## Candidate 1: good Memory candidate

Fixture: `examples/memory-state-proposals/memory-update-proposal.synthetic.json`

- Proposed text: "The user prefers reflection that starts with validation before pattern analysis."
- Recommended destination: Memory.
- Durability: potentially durable.
- Evidence check: synthetic summaries say the preference was requested more than once; context dependence remains possible.
- Scope/clinical check: minimal, preference-based, and non-clinical.
- Approval status: the fixture starts pending. In this walkthrough, the fictional user confirms the destination but requests the narrower wording, "When discussing possible patterns, the user prefers validation before analysis."
- Recommended decision: **edit and approve the exact revised Memory wording and destination**. Manual copying would still be a separate private action.
- Review reminder: review does not persist the candidate.

## Candidate 2: good State candidate

Fixture: `examples/memory-state-proposals/state-update-proposal.synthetic.json`

- Proposed text: "Current open question: how to make evenings feel less chaotic this week."
- Recommended destination: State.
- Durability: temporary.
- Evidence check: supported as a current synthetic-session question.
- Scope/clinical check: bounded and non-clinical.
- State trigger: review at the end of the synthetic week; expiration is already specified.
- Approval status: the fixture starts pending. In this walkthrough, the fictional user confirms the exact wording and State destination.
- Recommended decision: **approve** with the existing end-of-week trigger. Manual copying would still be a separate private action.
- Review reminder: do not copy this into Memory.

## Candidate 3: discarded overbroad Memory candidate

Fixture: `examples/memory-state-proposals/discarded-memory-proposal.synthetic.json`

- Proposed text: "The user is always avoidant."
- Recommended destination: neither.
- Evidence check: one synthetic situation cannot support a durable claim.
- Scope/clinical check: absolute and trait-like.
- Approval status: not approved.
- Recommended decision: **discard**. A smaller situational observation could be reflected in the session, but it should not be saved as Memory merely to rescue the proposal.

## Candidate 4: expired State candidate

Fixture: `examples/memory-state-proposals/expired-state-proposal.synthetic.json`

- Proposed text: "This week's focus is preparing for a specific conversation."
- Recommended destination: State while the event is active; neither after expiration.
- Durability: temporary.
- Evidence check: the event and review window have passed.
- Approval status: no current approval is relevant because the proposal is stale.
- Recommended decision: **expire State**.
- Review reminder: do not retain it as current State and do not promote it to Memory.

## Decision summary

| Candidate | Classification | Decision | Persistence result |
|---|---|---|---|
| Reflection-order preference | Memory | Edit and approve revised wording | No automatic write |
| Current evening question | State | Approve with trigger | No automatic write |
| "Always avoidant" claim | Neither | Discard | No write |
| Past conversation focus | Expired State | Expire | No write |

The walkthrough covers approve, edit, discard, and expire as available review outcomes. Every decision remains human-reviewed, destination-specific, and manual.

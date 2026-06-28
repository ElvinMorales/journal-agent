# Synthetic Intake-to-Proposal Walkthrough

This walkthrough is independently synthetic. It contains no real intake response, journal content, private Memory, or live State.

## Brief Intake Summary

A fictional user expects to bring mixed daily notes and freewrites. They prefer warm, concise reflection, dislike overly clinical or overly cheerful responses, and want advice only after being asked. Broad areas include home, relationships, creative projects, and work routines. A temporary schedule change and a near-term creative decision may matter now. The user skips questions about recurring patterns and excludes identifying details, raw excerpts, and unnecessary sensitive specifics from all proposals.

An intake answer is evidence for a possible proposal, not approval. Model confidence about classification is also not approval.

## Interpretation

The response-style and advice preferences might remain useful across sessions, so the agent places minimal versions in the candidate Memory list. The schedule and open decision are expected to change, so the agent places minimal versions in the candidate State list with review, stale, and expiration triggers. Broad life areas help interpret the intake but are not automatically proposed for persistence.

The agent does not infer a personality trait from the user's tone preferences, does not turn skipped questions into facts, and does not copy raw answers into either destination.

## Initial Candidate Set

Candidate Memory, all `pending_review`:

1. `Prefer warm, concise reflection.`
2. `Ask before offering advice unless action support is requested directly.`
3. `The user mainly processes experience through creative work.`

The third candidate is intentionally overbroad. One broad life-area selection does not establish a durable pattern.

Candidate State, all `pending_review`:

1. `A temporary schedule change may limit reflection time.` Review after two weeks or when the schedule changes; expire when the temporary schedule ends.
2. `A near-term creative decision is still open.` Review after the decision or at month end; expiration initially needs clarification.

No candidate is approved, and no write occurs.

## What Is Not Saved

- Identifying details.
- Raw writing excerpts.
- Sensitive specifics that are not required for configuration.
- Broad life-area labels by themselves.
- Skipped answers or model guesses.

## What Remains Unanswered

- Whether the user wants recurring patterns noticed over time.
- Whether every concise reflection should end with a question.
- The exact event that should expire the open creative-decision context.

## Review Changes

The user reviews one item at a time:

1. **Approve a Memory proposal:** The user accepts `Prefer warm, concise reflection.` for Memory. This review decision identifies desired wording and destination for a later workflow; it does not write anything.
2. **Edit proposal wording:** The user changes the advice preference to `Ask before offering advice; direct requests for action are the exception.` The edited wording must be reviewed as the new exact candidate.
3. **Move Memory to State:** The user says the preference for very short replies applies only during the current schedule change. The revised candidate becomes State: `Keep replies especially short during the temporary schedule change.` It now requires separate State review and triggers.
4. **Discard an uncertain proposal:** The user discards `The user mainly processes experience through creative work.` because it is overbroad and unsupported. Nothing replaces it unless the user supplies narrower wording.
5. **Add a State expiration trigger:** The user adds `Expire when the creative decision is made` to the open-decision candidate. The review trigger remains `Review at month end if still open.`

After these choices, Memory and State remain separate. Moving an item does not carry approval to the new destination. Exact approved wording and destination would be required before any future apply operation.

## Boundary

No write occurs anywhere in this walkthrough. Schema validation does not equal approval, an intake answer does not equal approval, and model confidence does not equal approval. Future MCP apply behavior is out of scope for issue #28 and is not implemented or implied here.

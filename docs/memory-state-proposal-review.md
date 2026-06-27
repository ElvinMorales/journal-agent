# Memory and State Proposal Review

## Purpose

Memory and State proposals are private, reviewable runtime artifacts. They preserve exact proposed wording, destination, evidence limits, and the user's decision without performing a write. Real proposals remain in the private data plane; only deliberately synthetic examples belong in this public repository.

## Memory vs State

Memory is durable, user-approved context likely to help across future sessions. A stable reflection preference may be a Memory candidate when enough evidence supports it and the user approves its exact wording.

State is temporary context for the current session, week, question, or open loop. It needs a review trigger, stale trigger, or expiration condition and must never be silently promoted to Memory.

## Proposal Lifecycle

```text
proposal created
-> pending review
-> user edits, approves, discards, or lets it expire
-> approved wording is manually copied into private Memory or State
```

Nothing is saved automatically. Creating, reviewing, or marking a proposal approved does not itself update Memory or State. The user manually copies only the exact approved wording into the approved destination.

The separate contracts are:

- `schemas/memory-update-proposal.schema.json` for durable candidates.
- `schemas/state-update-proposal.schema.json` for temporary candidates.

## Review Questions

- Is this Memory or State?
- Is it durable or temporary?
- Is it based on enough evidence?
- Is the wording too broad?
- Is the wording too clinical?
- Does it contain raw private content?
- Does it include a review or stale trigger if it is State?
- Has the user approved the exact wording and destination?
- Should it be approved, edited, discarded, or expired?

Discard proposals that contain raw entries, selected excerpts, therapy or crisis notes, diagnoses, treatment or medication guidance, unsupported durable traits, or private logs. If a smaller non-clinical statement would be useful, edit it and review the revised wording as a new exact candidate.

## Good and Poor Candidates

Good synthetic Memory candidate:

> The user prefers reflection that starts with validation before pattern analysis.

This may be durable if repeated, explicitly supported, and approved. It remains pending until the user accepts the exact wording and private Memory destination.

Poor synthetic Memory candidate:

> The user is always avoidant.

This is absolute, trait-like, and cannot be supported by one situation. Discard it.

Good synthetic State candidate:

> Current open question: how to make evenings feel less chaotic this week.

This is temporary and includes a clear end-of-week review trigger.

Poor State candidate: a full pasted entry used as an ongoing log. State should hold only the minimal current context needed for a bounded period.

## Where Proposals Live

Real proposals belong in a private vault or other user-controlled private data plane, for example:

```text
Journal Mirror/Pending Updates/memory/
Journal Mirror/Pending Updates/state/
```

Keep the destinations separate. Proposal files may point to an opaque private session identifier, but should not duplicate source writing. The public repository contains only schemas and synthetic fixtures under `examples/memory-state-proposals/`.

## Publishing Safety Checklist

Before publishing repository changes, confirm:

- [ ] No raw journal content or selected excerpts.
- [ ] No filled real Memory.
- [ ] No live State.
- [ ] No pending real proposals.
- [ ] No therapy notes or crisis notes.
- [ ] No local paths.
- [ ] No secrets or credentials.
- [ ] No screenshots, logs, exports, or databases.
- [ ] No names, employer details, or other identifying details.
- [ ] All proposal examples are clearly synthetic.

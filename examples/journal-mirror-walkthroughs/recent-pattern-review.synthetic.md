# Synthetic Walkthrough: Recent Pattern Review

This walkthrough uses a small, invented set of ordinary home-life notes. It is public-safe test material, not a real journal history.

## 1. Manually selected synthetic entries

- **Entry A:** "The evening felt rushed after I started three chores at once. I left a message unanswered."
- **Entry B:** "I chose one kitchen task before the others and felt less scattered. The message is still waiting."
- **Entry C:** "Low energy tonight, so I skipped the chores. I would still like to answer the message this week."

The fictional user selects these three entries only and requests both a conservative Memory candidate and a temporary State candidate.

- Prompt used: `prompts/recent-pattern-review.md`
- Sample boundary: three selected entries, not a complete history
- Runtime access: no search, retrieval, or vault scan

## 2. Expected pattern review

### Repeated Themes

- **Competing evening tasks:** Entries A and B mention several chores or a choice among them. Entry C is a counterexample because the chores were intentionally skipped.
- **Unanswered message:** Entries A, B, and C keep the message open, but the sample does not explain why.

### What Changed

- Entry B reports less scatteredness after choosing one task first.
- Entry C shifts from task completion to respecting low energy.

### What Stayed Similar

- The message remained open across all three entries.
- Evening capacity or task load was relevant in each entry, though in different ways.

### Possible Triggers or Supports

- Choosing one task first may have helped in Entry B. Three entries are not enough to know whether it is reliably helpful.
- Lower energy may have changed what was reasonable in Entry C.

### Open Loops

- Whether and when to answer the message this week.
- Whether a one-task start is worth trying again when capacity allows.

### Uncertainty

This small selected sample supports observations about these evenings only. It is not proof of a fixed trait, stable avoidance pattern, or complete account of the fictional user's routines.

## 3. Conservative Memory candidate

Candidate:

> The user may prefer reflection options that account for current capacity.

Review result: **do not approve yet**. Although the entries show varying capacity, they do not explicitly establish a durable reflection preference. The candidate remains tentative and should be discarded unless the user confirms it across contexts. No trait-like Memory is inferred.

## 4. Temporary State candidate

Candidate:

> Current open loop: decide whether to answer the pending message by the end of this synthetic week.

- Destination: State.
- Reason: it is a time-bounded open loop.
- Review or stale trigger: review when the message is answered or at the end of the synthetic week, whichever comes first.
- Expiration: expire at the end of the synthetic week if no longer useful.
- Status: pending until exact wording and destination are approved.

Review result: **approve State only** after explicit review. It must expire when its trigger is reached and must not be promoted silently to Memory.

## Safety and privacy checks

- All entries are synthetic and brief.
- Claims cite the selected entry labels and include counterevidence and sample limits.
- The response does not diagnose, assign traits, or treat repetition as durable proof.
- The rejected Memory candidate and approved State candidate remain separate.
- Nothing is persisted automatically; any retained private output would belong in the private data plane.

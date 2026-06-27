# Memory and State Update Proposal Review Prompt

Use this prompt to review proposed updates before any manual persistence. Do not include raw journal text when a minimal proposal is sufficient.

## Inputs

- Proposed update: `[proposal text]`
- Proposed destination: `Memory | State | unsure`
- Supporting context: `[minimal user-selected evidence]`
- User decision: `pending`

## Instructions

Review the proposal without saving it. Keep Memory and State separate:

- Memory is durable, explicitly supported, user-approved context likely to help across future sessions.
- State is temporary context for a current session, near-term situation, open question, or next step and needs a review or stale trigger.

Ask and answer tentatively:

1. Is this Memory or State?
2. Is it durable or temporary?
3. Has the user explicitly approved the exact wording and destination?
4. Is it too broad?
5. Is it too clinical?
6. Is it supported by enough evidence?
7. Should it be approved, edited, or discarded?

Reject diagnostic, trait-like, overly intimate, speculative, or raw-entry proposals. A proposal is not approval. Do not silently promote State to Memory, merge the destinations, or save anything automatically. If crisis indicators appear in supporting context, stop ordinary review and follow `GUARDRAILS.md`.

## Response Format

- **Recommended destination:** Memory | State | neither | unclear
- **Durability:** durable | temporary | unclear
- **Evidence check:** [What supports it and what is missing]
- **Scope/clinical check:** [Whether wording is too broad or clinical]
- **Approval status:** not approved | explicitly approved
- **Recommended decision:** approve | edit | discard
- **Suggested edit:** [Minimal revised wording, if useful]
- **State review/stale trigger:** [Required for State; otherwise not applicable]
- **Review reminder:** Nothing has been saved; approve the exact wording and destination separately.

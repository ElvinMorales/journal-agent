---
name: memory-state-review
description: Classify and review proposed Journal Mirror Memory or State updates; use before any manual persistence to test durability, scope, evidence, clinical framing, exact user approval, and the correct separate destination.
metadata:
  skill_category: update-review
  artifact_categories: [capability, memory, state, guardrail]
  trust:
    capability_type: memory_state_review
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: proposal_only
    state_writes: proposal_only
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Memory and State Review

## Purpose

Help the user approve, edit, reclassify, or discard a proposed update without writing it.

## When to Use

Use after a reflection produces an optional proposal or when the user supplies a candidate for classification. Use before any manual change to private Memory or State.

## Inputs

- Proposed text
- Proposed destination or `unsure`
- Minimal user-selected supporting context
- Current approval status

## Workflow

1. Follow `prompts/update-proposal-review.md`.
2. Classify durable context as possible Memory and temporary context as possible State.
3. Check evidence, breadth, clinical framing, necessity, and privacy sensitivity.
4. Require an explicit decision about the exact wording and destination.
5. For State, require a review or stale trigger.
6. Recommend approve, edit, or discard without performing a write.

## Outputs

- Recommended destination: Memory, State, neither, or unclear
- Durability and evidence assessment
- Scope and clinical-language check
- Approval status and recommended decision
- Minimal suggested edit when useful
- Review or stale trigger for State

## Boundaries

Do not diagnose, create clinical records, treat a proposal as approval, or preserve raw journal text when a smaller statement is enough. Do not merge Memory and State or promote one automatically.

## Privacy Handling

Use the minimum user-selected evidence. Do not fetch source notes, expose private context in public artifacts, or retain reviewed proposals automatically.

## Memory/State Handling

Memory must be durable, explicitly supported, minimally stated, and approved. State must be temporary, useful now, minimally stated, approved, and paired with a review or stale trigger. Approval for one destination never authorizes the other.

## Failure Modes

- Calling temporary context durable Memory
- Treating repeated wording as sufficient evidence of a trait
- Accepting broad, clinical, or identity-defining language
- Assuming approval from silence or from the request to review
- Writing, merging, or promoting updates automatically

## Validation Checklist

- Destination and durability are assessed separately.
- Evidence and uncertainty are explicit.
- Wording is minimal, non-clinical, and not trait-like.
- Exact user approval is required.
- State includes a review or stale trigger.
- The outcome is approve, edit, or discard.
- Nothing was written automatically.

## References

- `prompts/update-proposal-review.md`
- `MEMORY.md.example`
- `STATE.md.example`
- `docs/journal-data-lifecycle.md`
- `PRIVACY.md`

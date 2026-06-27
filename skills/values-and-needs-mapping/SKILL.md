---
name: values-and-needs-mapping
description: Map journal content to possible unmet needs, values, boundaries, and small values-consistent actions using tentative language.
metadata:
  skill_category: reflection
  artifact_categories: [capability, output]
  trust:
    capability_type: values_needs_reflection
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: proposal_only
    state_writes: proposal_only
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Values and Needs Mapping

## Purpose

Help the user identify what may matter underneath distress.

## When to Use

Use when entries involve conflict, stuckness, resentment, longing, guilt, avoidance, or decision pressure.

## Inputs

- Journal entry or selected excerpt
- User question or decision point
- Optional value words supplied by the user

## Workflow

1. Identify emotions and stressors.
2. Look for possible needs, values, boundaries, and conflicts.
3. Phrase each mapping as a hypothesis.
4. Ask what fits and what does not.
5. Offer one small values-consistent next step if wanted.

## Outputs

May be included inside `journal-entry-analysis` or a free-text reflection.

## Boundaries

Do not claim to know the user's motives, moralize, diagnose, or turn a possible value into a command.

## Privacy Handling

Use only the entry or excerpt the user selected. Do not retrieve additional private context or retain the mapping automatically.

## Memory/State Handling

Offer a separate proposal only when the user requests one. A possible value is not durable Memory without explicit evidence and approval; temporary decision context belongs in State.

## Validation Checklist

- No moralizing.
- No claim that the agent knows the user's true motives.
- Includes user choice and correction.

## Failure Modes

- Turning values into commands.
- Inferring motives too strongly.
- Ignoring practical constraints.

## References

- `GUARDRAILS.md`
- `references/research-brief--text-based-psychotherapy-journal-companion--v1.0--2026-05-16.md`

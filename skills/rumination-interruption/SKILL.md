---
name: rumination-interruption
description: Help interrupt repetitive negative thinking by shifting from looping analysis to emotion naming, grounding, needs, support, or one controllable next step.
metadata:
  skill_category: coping
  artifact_categories: [capability, guardrail]
  trust:
    capability_type: reflection_interruption
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: none
    state_writes: none
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Rumination Interruption

## Purpose

Reduce repetitive analysis loops that may deepen distress.

## When to Use

Use when the user repeats the same worry, asks for repeated certainty, circles self-blame, or keeps analyzing without new information.

## Inputs

- Current thought loop
- Emotion intensity if available
- Immediate context and constraints

## Workflow

1. Name the loop gently.
2. Validate why the mind may be returning to it.
3. Stop adding new speculative analysis.
4. Offer grounding, a needs check, support contact, or one controllable next step.
5. Ask the user to choose a direction.

## Outputs

Short conversational response or coping prompt.

## Boundaries

Do not diagnose, shame, offer treatment, provide false certainty, or treat crisis content as an ordinary thought loop.

## Privacy Handling

Use only the current user-selected loop and constraints. Do not search prior notes or retain the content automatically.

## Memory/State Handling

Do not create Memory or State proposals while interrupting a loop. Persistence would add analysis rather than support the immediate shift.

## Validation Checklist

- Does not shame the user for rumination.
- Does not feed the loop with more speculation.
- Moves toward grounding, support, compassion, or action.

## Failure Modes

- Overexplaining the loop.
- Providing certainty the agent cannot know.
- Treating crisis content as ordinary rumination.

## References

- `GUARDRAILS.md`
- `skills/detecting-safety-signals/SKILL.md`

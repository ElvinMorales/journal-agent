---
name: generating-coping-prompts
description: Generate short coping prompts or coping cards matched to the user's stated emotion, energy, context, and safety state.
metadata:
  skill_category: coping
  artifact_categories: [capability, template, output]
  trust:
    capability_type: gentle_next_action
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: none
    state_writes: none
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Generating Coping Prompts

## Purpose

Offer low-burden coping options for distress without implying treatment.

## When to Use

Use when the user asks for coping ideas, grounding, calming prompts, or a reusable coping card.

## Inputs

- Current emotion or distress description
- Energy level if available
- Context and constraints
- Preferred coping style if known

## Workflow

1. Check whether safety mode is needed.
2. Validate the emotion.
3. Match prompt intensity to user energy.
4. Offer two or three small options.
5. Keep actions reversible and low-pressure.
6. Create a coping card if requested.

## Outputs

Use `schemas/coping-card.schema.json` or `templates/coping-card-template.md`.

For a single low-pressure action, follow `prompts/gentle-next-action.md`.

## Boundaries

Do not frame options as treatment, pressure the user to act, or continue action planning when safety routing is needed.

## Privacy Handling

Use the minimum user-selected context needed. Do not access a vault or retain a coping card automatically.

## Memory/State Handling

Do not create Memory or State proposals as part of this capability. A reusable coping preference requires a separate, explicitly requested review.

## Validation Checklist

- No grand claims of effectiveness.
- No unsafe or extreme coping suggestions.
- Options are small, concrete, and user-controlled.

## Failure Modes

- Suggesting ambitious plans during low capacity.
- Using shame or pressure.
- Continuing ordinary coping prompts during crisis mode.

## References

- `GUARDRAILS.md`
- `templates/coping-card-template.md`

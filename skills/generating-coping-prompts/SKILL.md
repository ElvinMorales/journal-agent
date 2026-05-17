---
name: generating-coping-prompts
skill_category: coping
artifact_categories: [capability, template, output]
description: Generate short coping prompts or coping cards matched to the user's stated emotion, energy, context, and safety state.
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

## Output

Use `schemas/coping-card.schema.json` or `templates/coping-card-template.md`.

## Verification

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

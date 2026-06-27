---
name: preparing-therapy-notes
description: Prepare user-owned, non-clinical notes and questions for a therapy session or trusted human support conversation.
metadata:
  skill_category: therapy-prep
  artifact_categories: [capability, template, output]
  trust:
    capability_type: human_support_preparation
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: none
    state_writes: none
    human_review_required: true
    clinical_boundary: non_clinical_preparation_only
    runtime_access: no_vault_access
---

# Preparing Therapy Notes

## Purpose

Convert journal reflections into concise user-reviewed talking points for human care.

## When to Use

Use when the user asks what to bring up in therapy, coaching, medical care, or a trusted support conversation.

## Inputs

- Selected journal entries or summaries
- Time period
- User priorities
- Safety concerns the user wants to mention

## Workflow

1. Clarify the time period and purpose.
2. Summarize themes in the user's language.
3. Separate observations from questions.
4. Highlight coping strategies that helped.
5. Include safety concerns if present.
6. Invite user edits before export.

## Outputs

Use `schemas/therapy-prep-summary.schema.json` or `templates/therapy-prep-template.md`.

## Boundaries

Prepare user-owned discussion notes only. Do not write clinician-style notes, diagnose, plan treatment, advise on medication, or replace human care.

## Privacy Handling

Use only material the user selects and minimize sensitive details. Never export, retain, or share notes automatically.

## Memory/State Handling

Do not turn therapy-preparation content into Memory or State. Any later persistence request requires a separate proposal and explicit review.

## Validation Checklist

- The note is not written as a clinician note.
- No diagnosis or treatment plan.
- User questions are clear and discussable.
- Sensitive details are minimized unless the user wants them included.

## Failure Modes

- Presenting agent interpretations as clinical conclusions.
- Including unnecessary private detail.
- Omitting safety concerns the user wants human support to know.

## References

- `docs/therapist-handoff-format.md`
- `PRIVACY.md`
- `GUARDRAILS.md`

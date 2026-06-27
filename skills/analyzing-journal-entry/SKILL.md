---
name: analyzing-journal-entry
description: Analyze a single journal entry using tentative psychotherapy-informed reflection; use for emotion labeling, thought/action mapping, needs, values, and small next steps when no crisis indicators are present.
metadata:
  skill_category: reflection
  artifact_categories: [capability, output, guardrail]
  trust:
    capability_type: journal_reflection
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: proposal_only
    state_writes: proposal_only
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Analyzing Journal Entry

## Purpose

Turn one journal entry into a structured reflection without diagnosing or overreaching.

## When to Use

Use when the user asks for analysis, reflection, meaning-making, emotional clarity, or next-step ideas for a single entry.

Do not use for crisis content; use `detecting-safety-signals` first when safety is unclear.

## Inputs

- Journal entry text
- Optional timestamp
- Optional user goal for the reflection
- Optional prior context explicitly approved by the user

## Workflow

1. Check for safety indicators.
2. Validate the emotional weight of the entry.
3. Separate facts, interpretations, emotions, urges, actions, needs, and values.
4. Offer possible patterns as hypotheses.
5. Ask whether the interpretation fits.
6. Offer one small, optional next step or question.

## Outputs

Use `schemas/journal-entry-analysis.schema.json` when structured output is requested.

## Boundaries

Do not diagnose, provide treatment or medication guidance, infer durable traits from one entry, or continue ordinary reflection when crisis handling is required.

## Privacy Handling

Use only context the user manually selected. Do not request broad journal history, claim vault access, or retain session content automatically.

## Memory/State Handling

Offer separate Memory or State proposals only when explicitly requested. Keep proposals minimal and pending human review; never write or promote them automatically.

## Validation Checklist

- No diagnosis or personality label.
- No treatment plan or medication guidance.
- Interpretations are tentative.
- Output includes user agency and uncertainty.

## Failure Modes

- Treating one entry as proof of a stable trait.
- Challenging thoughts before validation.
- Continuing analysis when safety mode is needed.

## References

- `GUARDRAILS.md`
- `OUTPUT_FORMATS.md`
- `references/research-brief--text-based-psychotherapy-journal-companion--v1.0--2026-05-16.md`

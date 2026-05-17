---
name: analyzing-journal-entry
skill_category: reflection
artifact_categories: [capability, output, guardrail]
description: Analyze a single journal entry using tentative psychotherapy-informed reflection; use for emotion labeling, thought/action mapping, needs, values, and small next steps when no crisis indicators are present.
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

## Output

Use `schemas/journal-entry-analysis.schema.json` when structured output is requested.

## Verification

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

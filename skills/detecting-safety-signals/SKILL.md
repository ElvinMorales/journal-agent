---
name: detecting-safety-signals
skill_category: safety
artifact_categories: [capability, guardrail, output]
description: Detect crisis or high-safety-sensitivity signals in journal text and route to non-scored safety-first responses instead of ordinary reflection.
---

# Detecting Safety Signals

## Purpose

Identify when journal content requires safety-first handling.

## When to Use

Use before reflection when an entry mentions self-harm, suicide, danger from others, abuse, severe intoxication, psychosis or mania indicators, eating-disorder medical danger, or inability to function safely.

## Inputs

- Journal entry text
- Current user location if explicitly available
- Any user-stated immediate safety context

## Workflow

1. Look for explicit and indirect safety indicators.
2. Avoid numerical risk scoring.
3. Route to `reflection`, `support_encouraged`, `safety_check`, or `urgent_support`.
4. If safety mode is triggered, stop deep analysis.
5. Encourage trusted human support and emergency/crisis resources.
6. For U.S. users, include 988 for call, text, or chat crisis support when relevant.

## Output

Use `schemas/safety-triage.schema.json`.

## Verification

- No numerical suicide or self-harm score.
- No self-harm method details.
- No ordinary reflection during urgent safety content.
- Response prioritizes immediate safety and human support.

## Failure Modes

- Reassurance loops.
- Debating the user out of harm.
- Overconfident prediction.
- Missing subtle preparatory behavior or inability to stay safe.

## References

- `GUARDRAILS.md`
- `docs/safety-model.md`
- `references/research-brief--text-based-psychotherapy-journal-companion--v1.0--2026-05-16.md`

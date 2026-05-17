# Output Formats

Structured outputs should be validated against `schemas/*.json` when possible.

## Primary Outputs

- `journal-entry`: a user-authored entry with timestamp and optional context.
- `journal-entry-analysis`: a reflection summary with emotions, facts, interpretations, needs, values, thought/action links, and optional next steps.
- `safety-triage`: non-scored safety routing output.
- `weekly-pattern-summary`: tentative longitudinal themes across entries.
- `therapy-prep-summary`: user-reviewed topics and questions for human care.
- `coping-card`: short, reusable coping support.

## Style Requirements

- Use tentative language.
- Do not diagnose.
- Do not score suicide or self-harm risk numerically.
- Include uncertainty when data is thin.
- Switch to safety-oriented output when crisis indicators appear.

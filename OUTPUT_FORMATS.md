# Output Formats

Structured outputs should be validated against `schemas/*.json` when possible.

## Primary Outputs

- `journal-entry`: a user-authored entry with timestamp and optional context.
- `journal-entry-analysis`: a reflection summary with emotions, facts, interpretations, needs, values, thought/action links, and optional next steps.
- `safety-triage`: non-scored safety routing output.
- `weekly-pattern-summary`: tentative longitudinal themes across entries.
- `therapy-prep-summary`: user-reviewed topics and questions for human care.
- `coping-card`: short, reusable coping support.
- `journal-mirror-session`: grounding, tentative reflection, uncertainty, questions, reversible options, and optional separate review-only proposals.
- `memory-update-proposal`: optional durable-context proposal that remains pending exact user approval.
- `state-update-proposal`: optional temporary-context proposal with a review or stale trigger that remains pending exact user approval.

The prompt surfaces define human-readable shapes for these three outputs. Reviewable proposal schemas and filled synthetic examples remain future work; no schema or automatic persistence is introduced here.

## Style Requirements

- Use tentative language.
- Do not diagnose.
- Do not score suicide or self-harm risk numerically.
- Include uncertainty when data is thin.
- Switch to safety-oriented output when crisis indicators appear.
- State explicitly that nothing was saved when an output includes a proposal.

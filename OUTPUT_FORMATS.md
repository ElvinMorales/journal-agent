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
- `memory-update-proposal`: optional durable-context candidate defined by `schemas/memory-update-proposal.schema.json`. It records minimal proposed wording, evidence and uncertainty, an opaque private source reference, safety/privacy checks, and a review decision.
- `state-update-proposal`: optional temporary-context candidate defined by `schemas/state-update-proposal.schema.json`. It records the active context or open loop, a required review or stale trigger, optional expiration, minimal evidence and uncertainty, safety/privacy checks, and a review decision.

Both proposal outputs are proposal-only and require human review of the exact wording and destination. Memory and State remain separate: State cannot be silently promoted to Memory, and approval for one destination does not approve the other. Neither output permits automatic persistence or raw private content. Real filled proposals remain private; the public fixtures in `examples/memory-state-proposals/` are synthetic.

## Style Requirements

- Use tentative language.
- Do not diagnose.
- Do not score suicide or self-harm risk numerically.
- Include uncertainty when data is thin.
- Switch to safety-oriented output when crisis indicators appear.
- State explicitly that nothing was saved when an output includes a proposal.

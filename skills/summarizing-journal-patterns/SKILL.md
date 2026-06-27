---
name: summarizing-journal-patterns
description: Summarize recurring themes across multiple journal entries using tentative, evidence-bound language and explicit uncertainty.
metadata:
  skill_category: longitudinal-summary
  artifact_categories: [capability, memory, output]
  trust:
    capability_type: pattern_reflection
    privacy_level: private_context_required
    data_boundary: user_selected_context_only
    retention: no_automatic_retention
    memory_writes: proposal_only
    state_writes: proposal_only
    human_review_required: true
    clinical_boundary: non_clinical_reflection_only
    runtime_access: no_vault_access
---

# Summarizing Journal Patterns

## Purpose

Help the user notice recurring themes without turning journal samples into fixed identity claims.

## When to Use

Use for weekly reviews, monthly reviews, or selected-entry summaries.

## Inputs

- Selected entries or summaries
- Time range
- User goal for the summary

## Workflow

1. Confirm the data set and time range.
2. Check for safety indicators.
3. Identify repeated emotions, situations, needs, values, coping attempts, and unresolved questions.
4. Distinguish strong patterns from weak signals.
5. Include uncertainty and missing context.
6. Offer optional questions or small next steps.
7. Use `prompts/recent-pattern-review.md` for the complete selected-entry review surface.

## Outputs

Use `schemas/weekly-pattern-summary.schema.json`.

Include repeated themes, changes, similarities, possible triggers or supports, open loops, uncertainty, and optional separate proposals when requested.

## Boundaries

Treat a small sample as incomplete evidence, not proof of a fixed trait. Do not diagnose, infer trauma history as fact, or continue pattern analysis when crisis routing is required.

## Privacy Handling

Use only the entries the user manually selected. Do not scan or request a full vault, and do not retain summaries automatically.

## Memory/State Handling

Propose State only for temporary context and Memory only for conservative, explicitly supported durable context. Require separate requests and reviews; never promote State or save either automatically.

## Validation Checklist

- No diagnosis or personality label.
- No claims beyond the selected data.
- Includes uncertainty.
- Identifies what seemed helpful, not only what hurt.

## Failure Modes

- Overgeneralizing from sparse entries.
- Creating fixed trait labels.
- Ignoring improvement or coping evidence.

## References

- `docs/journal-data-lifecycle.md`
- `OUTPUT_FORMATS.md`
- `references/research-brief--text-based-psychotherapy-journal-companion--v1.0--2026-05-16.md`

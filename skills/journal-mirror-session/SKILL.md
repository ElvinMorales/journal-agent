---
name: journal-mirror-session
description: Run a private-first Journal Mirror session from one entry, one excerpt, or a small user-selected group of entries; use for tentative reflection, questions, reversible next steps, and optional separately reviewed Memory or State proposals.
metadata:
  skill_category: reflection-orchestration
  artifact_categories: [capability, prompt, guardrail, memory, state]
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

# Journal Mirror Session

## Purpose

Run the selected-context reflection flow without requiring structured journal entries or broad notes access.

## When to Use

Use after natural writing when the user manually supplies one entry, an excerpt, or a small set of entries and wants reflection, questions, next-step options, or optional update proposals.

Do not use ordinary reflection when crisis indicators require `detecting-safety-signals`.

## Inputs

- User-selected private context
- Optional question or reflection goal
- Optional response and retention preferences
- Separate yes/no requests for State and Memory proposals

## Workflow

1. Confirm the selected scope and user goal without requesting broader journal access.
2. Check for crisis indicators and route to `GUARDRAILS.md` when present.
3. Follow `prompts/journal-mirror-session.md`; use `prompts/freeform-entry-mirror.md` for one unstructured entry.
4. Ground observations in the selected text and label interpretations as tentative.
5. Ask questions that invite correction and offer only small, reversible options.
6. Generate each requested proposal separately and end with a review reminder.

## Outputs

- Brief grounding statement
- Tentative reflection with possible emotions, needs, values, or themes
- Explicit uncertainty and clarifying questions
- Optional reversible next steps
- Optional separate State and Memory proposals
- Reminder that nothing was saved

## Boundaries

Do not diagnose, provide therapy or crisis counseling, create treatment plans, give medication guidance, infer durable traits from limited evidence, or continue ordinary reflection after crisis indicators appear.

## Privacy Handling

Use only manually selected context. Do not claim or request vault access, retrieve other notes, or retain inputs or outputs automatically. Respect a `do-not-persist` instruction by omitting all update proposals.

## Memory/State Handling

Treat Memory as durable and State as temporary. Generate only explicitly requested proposals, keep destinations separate, include uncertainty and review criteria, and never write, merge, or promote them automatically.

## Failure Modes

- Treating a session as permission to scan or retain journal content
- Requiring a template before reflecting
- Presenting hypotheses as facts or traits
- Producing unrequested or combined update proposals
- Continuing ordinary reflection when safety routing is required

## Validation Checklist

- Selected scope and user goal are clear.
- Reflection is tentative, non-clinical, and evidence-bound.
- Uncertainty and user correction are explicit.
- Next steps are optional and reversible.
- State and Memory proposals are optional, separate, and review-only.
- Nothing implies vault access or automatic retention.
- Crisis indicators route to `GUARDRAILS.md`.

## References

- `prompts/journal-mirror-session.md`
- `prompts/freeform-entry-mirror.md`
- `docs/journal-mirror-workflow.md`
- `GUARDRAILS.md`
- `PRIVACY.md`

# Journal Companion Agent Artifacts

This repository defines a personal artifact system for a text-based journal companion agent. The companion helps turn journal entries into structured reflection, emotion labels, thought/action maps, needs and values signals, coping prompts, pattern summaries, and therapy-prep notes.

It is not a therapist, diagnostic tool, treatment planner, medication advisor, or replacement for licensed care.

## What Is Included

- Always-on agent instructions in `AGENTS.md`
- Safety and privacy policies in `GUARDRAILS.md` and `PRIVACY.md`
- Task workflows in `skills/`
- Structured output contracts in `schemas/`
- User-facing templates in `templates/`
- Prompt entry points in `prompts/`
- Evaluation cases in `evals/`
- Private ignored storage under `private/`

## Private Data

Raw journal entries, exports, summaries, memory, state, crisis notes, and therapy notes belong only under ignored `private/` paths. The committed files provide structure and examples, not personal journal data.

## Start Points

- Read `ARTIFACT_MAP.md` for the full artifact layout.
- Read `GUARDRAILS.md` before building or running reflection workflows.
- Use `templates/daily-journal-template.md` or `templates/quick-check-in-template.md` for entries.
- Use `prompts/evening-review.md` or `prompts/weekly-pattern-review.md` for reflection sessions.

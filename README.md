# Journal Companion Agent Artifacts

This repository is a public, reusable template for building a text-based journal companion agent. It provides the instruction files, guardrails, schemas, prompts, templates, and eval cases needed to turn private journal entries into structured reflection, emotion labels, thought/action maps, needs and values signals, coping prompts, pattern summaries, and therapy-prep notes.

It is not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, or a replacement for licensed care.

## Public Use Warning

Do not commit filled journal entries, private notes, summaries, memory, state, exports, crisis notes, therapy notes, logs, databases, environment files, secrets, or identifying information. Use the committed files as structure and examples only.

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

Raw journal entries, exports, summaries, memory, state, crisis notes, and therapy notes belong only under ignored `private/` paths or another user-controlled private system. The committed files provide structure and examples, not personal journal data.

The `private/` directory is ignored by default except for placeholder `.gitkeep` files. Treat anything written there as local-only unless you deliberately export and review it.

## Start Points

- Read `ARTIFACT_MAP.md` for the full artifact layout.
- Read `GUARDRAILS.md` before building or running reflection workflows.
- Use `templates/daily-journal-template.md` or `templates/quick-check-in-template.md` for entries.
- Use `prompts/evening-review.md` or `prompts/weekly-pattern-review.md` for reflection sessions.

## For Contributors

- Read `CONTRIBUTING.md` before opening issues or pull requests.
- Report sensitive-data exposure or safety issues using `SECURITY.md`.
- Run `python scripts\validate-json-schemas.py` after schema changes.

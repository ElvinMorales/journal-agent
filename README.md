# Journal Mirror Agent

This repository is a public, reusable scaffold for a text-based Journal Mirror Agent. The `v0.2.0` direction starts with natural writing in a private notes system, then uses selected writing for tentative reflection and reviewable Memory or State update proposals. The public repo provides instructions, guardrails, schemas, prompts, optional templates, and eval cases; it is not the private runtime or journal store.

It is not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, a mental health product, or a replacement for licensed care. It is also not a hosted service, an Obsidian plugin, or a private journal database.

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

## Start Here

1. Write naturally in a private Obsidian vault or another user-controlled private notes system.
2. Use the workflow in `docs/journal-mirror-workflow.md` on one selected entry, excerpt, or small group of entries.
3. Review any proposed Memory or State updates before applying, editing, or discarding them. Nothing durable changes automatically.
4. Use `templates/` only when a structured starting point is helpful; templates are optional, not a required journal format.

Read `docs/roadmap-v0.2.0.md` for the release direction, `ARTIFACT_MAP.md` for the artifact layout, and `GUARDRAILS.md` before building or running reflection workflows. Existing prompts remain starting surfaces for reflection sessions.

## For Contributors

- Read `CONTRIBUTING.md` before opening issues or pull requests.
- Report sensitive-data exposure or safety issues using `SECURITY.md`.
- Run `python scripts\validate-json-schemas.py` after schema changes.

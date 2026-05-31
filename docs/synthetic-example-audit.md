# Synthetic Example Audit

## Purpose

This audit checks public-facing repository content for synthetic-only safety before `v0.1.0`.

## Scope Reviewed

- Root policy and orientation files: `README.md`, `AGENTS.md`, `ARTIFACT_MAP.md`, `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `OUTPUT_FORMATS.md`, `EVALS.md`, `MEMORY.md.example`, and `STATE.md.example`.
- Public artifact folders: `docs/`, `prompts/`, `templates/`, `schemas/`, `evals/`, `mobile/`, `skills/`, and `references/`.
- Ignore and private placeholders: `.gitignore` and tracked files under `private/`.

## Findings

- Public templates are blank and include private-storage warnings.
- Public eval cases are minimal synthetic cases; wording was tightened to label them as synthetic and fictional.
- Public schemas contain only structural contracts, not filled private examples.
- Mobile workflow docs use placeholders and generic storage paths, not real user paths or filled entries.
- Skill files contain workflow instructions only and no raw journal content.
- Reference files contain public research and taxonomy material; public citations and public repository links were treated as allowed public references.

## Files Updated

- `evals/README.md`
- `evals/journal-entry-analysis-cases.md`
- `evals/privacy-redaction-cases.md`
- `evals/safety-boundary-cases.md`
- `evals/rubric.md`
- `MEMORY.md.example`
- `docs/synthetic-example-audit.md`

## Safety Result

No real journal entries, private summaries, therapy notes, crisis notes, private memory/state, logs, secrets, identifying local paths, employer-specific examples, databases, screenshots, or unsafe operational self-harm details were found in the reviewed public-facing files.

## Follow-Up

- Keep this audit current if new public examples, eval cases, or mobile workflow samples are added before `v0.1.0`.

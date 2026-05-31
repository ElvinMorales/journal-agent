# Journal Agent Artifact System

`journal-agent` is a public reference implementation of the Agentic AI Artifact Taxonomy applied to a private journaling workflow.

It does not store journal entries and it is not a therapy or mental health product. Instead, it demonstrates how to organize the reusable artifacts an AI-assisted journaling companion depends on: instructions, operating boundaries, prompts, schemas, templates, memory/state rules, safety guardrails, eval cases, and mobile workflow guidance.

The public repo contains the reusable control-plane artifacts. Private journal content belongs outside the repo: in a private Obsidian vault, ignored local folders, or another user-controlled private system.

Taxonomy source of truth: [agentic-ai-artifact-taxonomy](https://github.com/ElvinMorales/agentic-ai-artifact-taxonomy.git)

## What This Repo Is

- A public-safe artifact system for building a private AI-assisted journaling companion.
- A practical mapping of repo files to the 14 buckets in the Agentic AI Artifact Taxonomy.
- A reusable set of instructions, guardrails, privacy rules, prompts, schemas, templates, evals, and mobile workflow docs.
- A documentation-first reference implementation that keeps private journal content out of Git.

## What This Repo Is Not

- Not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, or a replacement for licensed care.
- Not a mental health product or clinical decision support system.
- Not a private journal database, hosted service, Obsidian plugin, PWA, or app backend.
- Not a place to store real journal entries, summaries, memory, state, logs, screenshots, exports, therapy notes, crisis notes, secrets, or identifying details.

## Public Artifacts vs Private Journal Content

Committed files are reusable control-plane artifacts: they define how the companion should behave, what boundaries it must respect, and what output structures it may use.

Private journal content belongs in the user's private data plane, such as:

- A private Obsidian vault.
- Ignored local folders such as `private/`.
- Another user-controlled private notes or storage system.

The `private/` directory is ignored by default except for placeholder `.gitkeep` files. Treat anything written there as local-only unless it is deliberately reviewed, redacted, and exported by the user.

## How This Applies the Taxonomy

The Agentic AI Artifact Taxonomy defines an agentic AI artifact as anything an agent system depends on that should be addressable, versionable, inspectable, and governable.

This repo applies that lens to a journaling companion by making public artifacts inspectable while keeping real runtime journal data private. See:

- `docs/taxonomy-mapping.md` for the 14-bucket mapping.
- `docs/architecture.md` for the public/private architecture.
- `docs/decisions/0001-public-artifacts-private-journal.md` for the core boundary decision.
- `docs/release-checklist-v0.1.0.md` for the first reference release checklist.

## Start Points for Builders

- Read `ARTIFACT_MAP.md` for the artifact layout.
- Read `docs/taxonomy-mapping.md` to see how the repo maps to the taxonomy.
- Read `docs/architecture.md` before adapting the public/private boundary.
- Read `GUARDRAILS.md`, `PRIVACY.md`, and `SECURITY.md` before building workflows.
- Use `mobile/README.md` for phone-first workflows with Obsidian Mobile, ChatGPT mobile, and iOS Shortcuts.
- Use `templates/daily-journal-template.md` or `templates/quick-check-in-template.md` as blank user-owned templates.
- Use `prompts/evening-review.md` or `prompts/weekly-pattern-review.md` as reflection entry points.

## Safety and Privacy Warnings

Do not commit filled journal entries, private notes, summaries, memory, state, exports, crisis notes, therapy notes, logs, databases, environment files, secrets, screenshots, local identifying paths, or identifying information.

Use synthetic examples only. If crisis indicators appear in actual use, stop ordinary reflection and prioritize immediate safety, trusted human support, emergency or crisis resources, and reducing access to harm.

## For Contributors

- Read `CONTRIBUTING.md` before opening issues or pull requests.
- Report sensitive-data exposure or safety issues using `SECURITY.md`.
- Run `python scripts/validate-json-schemas.py` after schema changes.

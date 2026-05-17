# Agent Artifacts

This folder explains how the artifact system composes.

## Loading Model

- Always-on: `AGENTS.md`, with concise policy and repo behavior.
- Triggered: `skills/*/SKILL.md`, loaded when a task matches the skill description.
- On demand: `docs/`, `references/`, `schemas/`, `templates/`, and `evals/`.
- Private: `private/`, ignored by Git except `.gitkeep` placeholders.

## Placement Rules

- Put stable boundaries in root docs.
- Put workflows in skills.
- Put long rationale in docs and references.
- Put personal content only under ignored private paths.

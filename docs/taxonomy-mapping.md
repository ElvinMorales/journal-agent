# Taxonomy Mapping

This document maps `journal-agent` to the Agentic AI Artifact Taxonomy.

Source of truth: [agentic-ai-artifact-taxonomy](https://github.com/ElvinMorales/agentic-ai-artifact-taxonomy.git)

## Summary

`journal-agent` applies the taxonomy to a private journaling workflow by keeping reusable artifacts public while keeping private journal content outside the repository.

The taxonomy defines an agentic AI artifact as anything an agent system depends on that should be addressable, versionable, inspectable, and governable. In this repo, public files are the inspectable control plane. Real journal entries, generated private summaries, memory, state, logs, exports, and crisis notes remain in user-controlled private systems.

## Mapping Table

| Taxonomy bucket | Repo artifact(s) | Purpose in this project | Public/private boundary | v0.1.0 status |
|---|---|---|---|---|
| Identity | `AGENTS.md`, `README.md` | Defines the companion's role, scope, and public reference implementation positioning | Public artifact; no private journal data | Covered |
| Operating style | `AGENTS.md`, `GUARDRAILS.md` | Defines tone, caution, crisis boundary, and reflection style | Public behavior rules only | Covered |
| Capability modules | `skills/*/SKILL.md` | Reusable workflows for reflection tasks | Public workflow instructions only | Partial |
| Tools | `scripts/` | Validation and redaction helpers | Public tooling; no private outputs committed | Partial |
| Knowledge/resources | `references/`, `docs/` | Supporting public reference material | Public-safe material only | Partial |
| Prompts/interfaces | `prompts/`, `templates/` | User-invoked flows and journal templates | Templates public; filled entries private | Covered |
| Memory | `MEMORY.md.example`, `private/memory/` | Durable user facts only with consent | Example public; real memory private/ignored | Boundary documented |
| State | `STATE.md.example`, `private/state/` | Session continuity and run context | Example public; real state private/ignored | Boundary documented |
| Planning/orchestration | `skills/`, `prompts/`, `docs/agent-artifacts/README.md` | Workflow sequencing and task routing | Public instructions only | Partial |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md` | Safety, privacy, reporting, and contribution rules | Public rules; no sensitive reports in issues | Covered |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/` | Structured output contracts | Schemas public; filled outputs private unless synthetic | Covered |
| Evaluation/observability | `EVALS.md`, `evals/` | Regression and safety review cases | Synthetic cases only | Partial |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/` | Local/mobile/no-code usage guidance and validation surfaces | Runtime private data stays out of repo | Partial |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, release checklist | Change history and future work | Public project tracking only | Partial |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.

## Known Gaps After v0.1.0

- Capability modules could include more explicit taxonomy headers or review metadata.
- Tool documentation could distinguish validation helpers from future callable runtime tools.
- Evaluation remains lightweight and qualitative; no complex eval infrastructure is planned for v0.1.0.
- Runtime guidance is local and mobile-first; hosted deployment is intentionally out of scope.
- Learning and iteration are limited to changelog, backlog, and release checklist artifacts.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

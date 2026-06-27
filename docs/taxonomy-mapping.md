# Taxonomy Mapping

The `agentic-ai-artifact-taxonomy` repository is the conceptual source of truth for this project. Journal Agent keeps its original 14 framework-neutral buckets intact and maps local filenames to them rather than inventing a competing taxonomy.

Strategic Mirror Agent is used as a working reference implementation pattern for file-first runtime design, Memory/State separation, workflow clarity, and private-instance structure. It is not the taxonomy source of truth.

Use this reading pattern when comparing implementations:

```text
generic artifact class
-> possible repo filenames
-> Strategic Mirror pattern
-> Journal Agent adaptation
```

For example:

```text
Planning and orchestration
-> workflow.md, orchestration/graph.yaml
-> a file-first session loop with explicit review gates
-> docs/journal-mirror-workflow.md
```

## Summary

`journal-agent` applies the taxonomy to a private journaling workflow by keeping reusable artifacts public while keeping private journal content outside the repository.

The taxonomy defines an agentic AI artifact as anything an agent system depends on that should be addressable, versionable, inspectable, and governable. In this repo, public files are the inspectable control plane. Real journal entries, generated private summaries, memory, state, logs, exports, crisis notes, and private runtime records remain in user-controlled private systems.

## Mapping Table

| Taxonomy bucket | Repo artifact(s) | Purpose in this project | Public/private boundary | v0.2.0 status |
|---|---|---|---|---|
| Identity | `AGENTS.md`, `README.md`, `docs/product-vision.md` | Defines the companion's role, scope, and Journal Mirror positioning | Public artifact; no private journal data | Covered |
| Operating style | `AGENTS.md`, `GUARDRAILS.md` | Defines tone, caution, crisis boundary, tentative reflection style, and non-clinical behavior | Public behavior rules only | Covered |
| Capability modules | `skills/journal-mirror-session/SKILL.md`, `skills/summarizing-journal-patterns/SKILL.md`, `skills/memory-state-review/SKILL.md`, `skills/*/SKILL.md` | Reusable workflows for selected-context reflection, pattern review, gentle actions, safety routing, and update review | Public workflow instructions and trust metadata only; no vault access | Covered for manual sessions |
| Tools | `scripts/` | Validation and redaction helpers; future connectors remain implementation-edge mappings | Public tooling; no private outputs committed | Partial |
| Knowledge/resources | `references/`, `docs/`, `docs/obsidian-private-runtime-guide.md` | Supporting public reference material and private-runtime setup guidance | Public-safe guidance only; private vault content stays outside Git | Covered for starter guide |
| Prompts/interfaces | `prompts/journal-mirror-session.md`, `prompts/freeform-entry-mirror.md`, `prompts/recent-pattern-review.md`, `prompts/gentle-next-action.md`, `prompts/update-proposal-review.md`, `templates/`, `docs/journal-mirror-workflow.md` | User-invoked manual session surfaces and optional templates | Prompts public; selected context and filled outputs private | Covered for manual sessions |
| Memory | `MEMORY.md.example`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `private/memory/` | Durable user-approved context and review-only proposal handling | Example and review rules public; real Memory and proposals private/ignored | Boundary and review surface covered |
| State | `STATE.md.example`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `private/state/` | Temporary session context and review-only proposal handling | Example and review rules public; live State and proposals private/ignored | Boundary and review surface covered |
| Planning/orchestration | `skills/journal-mirror-session/SKILL.md`, `prompts/`, `docs/journal-mirror-workflow.md`, `docs/obsidian-private-runtime-guide.md` | Workflow sequencing, manual private setup, selected-context reflection, proposal, and review gates | Public instructions only; session artifacts remain private | Covered for manual flow |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `skills/*/SKILL.md`, `docs/decisions/`, `docs/obsidian-private-runtime-guide.md` | Safety, privacy, trust metadata, reporting, review requirements, and architectural decisions | Public rules and metadata; no sensitive runtime artifacts | Covered |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/`, `prompts/*.md` | Structured contracts plus human-readable session and proposal output shapes | Definitions public; filled outputs private unless synthetic | Prompt outputs covered; proposal schemas remain open |
| Evaluation/observability | `EVALS.md`, `evals/` | Regression and safety review cases | Synthetic cases only; private traces excluded | Partial |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/`, `docs/obsidian-private-runtime-guide.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md` | Local/mobile/no-code guidance, manual private setup, validation surfaces, and public-control-plane/private-data-plane boundary | Runtime private data stays out of repo; no live runtime is implemented | Manual starter guide covered |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, release checklists, `docs/roadmap-v0.2.0.md` | Change history, roadmap, and future work | Public project tracking only | Partial |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps After v0.2.0 Planning

- Memory and State update proposals need explicit schemas and examples.
- Evaluation remains lightweight and needs additional synthetic cases for template forcing, memory overreach, and unsafe clinical framing.
- Future MCP/VPS architecture remains documentation-only and intentionally unimplemented.
- Learning and iteration need v0.2 release-readiness docs after the sprint work lands.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

MCP, host adapters, and similar protocol objects may later map to several buckets, especially Tools, Guardrails and governance, and Runtime and deployment. They remain implementation-edge mappings and do not become new top-level categories.

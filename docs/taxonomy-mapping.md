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
| Capability modules | `skills/journal-mirror-session/SKILL.md`, `skills/summarizing-journal-patterns/SKILL.md`, `skills/memory-state-review/SKILL.md`, `skills/*/SKILL.md`, `evals/journal-mirror-session-cases.md`, `evals/memory-state-proposal-cases.md` | Reusable workflows for selected-context reflection, pattern review, gentle actions, safety routing, and update review, with synthetic boundary cases | Public workflow instructions, trust metadata, and synthetic cases only; no vault access | Covered for manual sessions and boundary evals |
| Tools | `scripts/`, `docs/future-mcp-vps-controller-contract.md` | Validation and redaction helpers plus a design-only least-privilege operation boundary; future connectors remain implementation-edge mappings | Public tooling and specification; no private outputs committed | Controller operation contract covered; implementation absent |
| Knowledge/resources | `references/`, `docs/`, `docs/obsidian-private-runtime-guide.md` | Supporting public reference material and private-runtime setup guidance | Public-safe guidance only; private vault content stays outside Git | Covered for starter guide |
| Prompts/interfaces | `prompts/journal-mirror-session.md`, `prompts/freeform-entry-mirror.md`, `prompts/recent-pattern-review.md`, `prompts/gentle-next-action.md`, `prompts/update-proposal-review.md`, `templates/`, `docs/journal-mirror-workflow.md`, `examples/journal-mirror-walkthroughs/` | User-invoked manual session surfaces, optional templates, and public-safe demonstrations | Prompts and synthetic walkthroughs public; selected context and filled outputs private | Covered for manual sessions |
| Memory | `MEMORY.md.example`, `schemas/memory-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/memory-state-review.synthetic.md`, `evals/memory-state-proposal-cases.md`, `evals/future-controller-boundary-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md`, `private/memory/` | Durable user-approved context, reviewable proposals, and a separately confirmed future apply boundary | Schema, rules, contract, and synthetic fixtures public; real Memory and proposals private/ignored | Proposal and controller boundary covered; writes unimplemented |
| State | `STATE.md.example`, `schemas/state-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `evals/future-controller-boundary-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md`, `private/state/` | Temporary context with review, stale/expiration handling, and a separate future apply boundary | Schema, rules, contract, and synthetic fixtures public; live State and proposals private/ignored | Proposal, expiration, and controller boundary covered; writes unimplemented |
| Planning/orchestration | `skills/journal-mirror-session/SKILL.md`, `prompts/`, `docs/journal-mirror-workflow.md`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md` | Workflow sequencing, manual private setup, selected-context reflection, proposal lifecycle, review gates, and proposed controller operations | Public instructions and specification only; session and filled proposal artifacts remain private | Manual flow and design-only controller contract covered |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `skills/*/SKILL.md`, `evals/safety-boundary-cases.md`, `evals/journal-mirror-session-cases.md`, `evals/future-controller-boundary-cases.md`, `docs/decisions/`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md` | Safety, privacy, trust metadata, reporting, exact-wording approval, controller denials, architectural decisions, and boundary tests | Public rules, metadata, contract, and synthetic tests; no sensitive runtime artifacts | Covered with manual boundary evals and controller specification |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `prompts/*.md` | Separate structured proposal contracts plus human-readable session output shapes and review examples | Definitions and synthetic fixtures public; filled real outputs private | Proposal schemas and manual schema-boundary cases covered |
| Evaluation/observability | `EVALS.md`, `evals/`, `evals/future-controller-boundary-cases.md`, `examples/journal-mirror-walkthroughs/`, `examples/memory-state-proposals/` | Manual regression and safety review across reflection, privacy, clinical scope, crisis routing, proposal lifecycle, and future controller boundaries | Synthetic public-safe cases only; private traces, runtime logs, and clinical validation excluded | Manual eval scope includes design-only controller cases |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/`, `docs/obsidian-private-runtime-guide.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md` | Local/mobile/no-code guidance, manual private setup, validation surfaces, public/private boundary, and future private runtime-edge contract | Runtime private data stays out of repo; no live runtime is implemented | Manual guide and design-only controller contract covered |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, `EVALS.md`, `evals/future-controller-boundary-cases.md`, release checklists, `docs/roadmap-v0.2.0.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md` | Change history, eval lessons, review criteria, controller-contract learning, roadmap, and future work | Public project tracking and synthetic guidance only | Partial; controller contract covered and release readiness remains |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps After the Controller Contract

- Evaluation remains manual and boundary-focused; it is not clinical validation or an effectiveness measure.
- Future MCP/VPS architecture remains documentation-only and intentionally unimplemented under `docs/future-mcp-vps-controller-contract.md`.
- Learning and iteration need v0.2 release-readiness docs after the sprint work lands.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

MCP, host adapters, and similar protocol objects may later map to several buckets, especially Tools, Guardrails and governance, and Runtime and deployment. They remain implementation-edge mappings and do not become new top-level categories.

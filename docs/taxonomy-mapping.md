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

| Taxonomy bucket | Repo artifact(s) | Purpose in this project | Public/private boundary | Current/planned status |
|---|---|---|---|---|
| Identity | `AGENTS.md`, `README.md`, `docs/product-vision.md` | Defines the companion's role, scope, and Journal Mirror positioning | Public artifact; no private journal data | Covered |
| Operating style | `AGENTS.md`, `GUARDRAILS.md` | Defines tone, caution, crisis boundary, tentative reflection style, and non-clinical behavior | Public behavior rules only | Covered |
| Capability modules | `skills/journal-mirror-session/SKILL.md`, `skills/summarizing-journal-patterns/SKILL.md`, `skills/memory-state-review/SKILL.md`, `skills/*/SKILL.md`, `evals/journal-mirror-session-cases.md`, `evals/memory-state-proposal-cases.md` | Reusable workflows for selected-context reflection, pattern review, gentle actions, safety routing, and update review, with synthetic boundary cases | Public workflow instructions, trust metadata, and synthetic cases only; no vault access | Covered for manual sessions and boundary evals |
| Tools | `scripts/`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md` | Validation and redaction helpers plus design-only least-privilege controller and MCP tool boundaries | Public tooling and specifications; no private outputs committed | Controller contract covered; MCP categories proposed; implementation absent |
| Knowledge/resources | `references/`, `docs/`, `docs/obsidian-private-runtime-guide.md`, `docs/v0.2-usable-product-handoff.md`, `docs/release-notes/v0.2.0.md` | Supporting public references, private-runtime setup guidance, release notes, and a public-reader handoff | Public-safe guidance only; private vault content stays outside Git | Covered for setup and v0.2 handoff |
| Prompts/interfaces | `prompts/journal-mirror-session.md`, `prompts/freeform-entry-mirror.md`, `prompts/recent-pattern-review.md`, `prompts/gentle-next-action.md`, `prompts/update-proposal-review.md`, `templates/`, `docs/journal-mirror-workflow.md`, `examples/journal-mirror-walkthroughs/` | User-invoked manual session surfaces, optional templates, and public-safe demonstrations | Prompts and synthetic walkthroughs public; selected context and filled outputs private | Covered for manual sessions |
| Memory | `MEMORY.md.example`, `schemas/memory-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/memory-state-review.synthetic.md`, `evals/memory-state-proposal-cases.md`, `evals/future-controller-boundary-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `private/memory/` | Durable user-approved context, reviewable proposals, and a separately confirmed future exact-wording apply boundary | Schema, rules, contract, ADR, and synthetic fixtures public; real Memory and proposals private/ignored | Manual proposal boundary covered; MCP apply planned, not implemented |
| State | `STATE.md.example`, `schemas/state-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `evals/future-controller-boundary-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `private/state/` | Temporary context with review, stale/expiration handling, and a separate future exact-wording apply boundary | Schema, rules, contract, ADR, and synthetic fixtures public; live State and proposals private/ignored | Manual proposal/expiration boundary covered; MCP apply planned, not implemented |
| Planning/orchestration | `skills/journal-mirror-session/SKILL.md`, `prompts/`, `docs/journal-mirror-workflow.md`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md`, `docs/v0.2-usable-product-handoff.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/roadmap-v0.3.0.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md` | Workflow sequencing, manual private setup, selected-context reflection, proposal lifecycle, review gates, and the planned MCP runtime sprint | Public instructions and specifications only; session and filled proposal artifacts remain private | Manual flow covered; `v0.3.0` sprint planned, not implemented |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `skills/*/SKILL.md`, `evals/safety-boundary-cases.md`, `evals/journal-mirror-session-cases.md`, `evals/future-controller-boundary-cases.md`, `docs/decisions/`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md`, `docs/release-checklist-v0.2.0.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md` | Safety, privacy, trust metadata, reporting, exact-wording approval, release gates, controller denials, architectural decisions, and boundary tests | Public rules, metadata, contracts, decisions, checklists, and synthetic tests; no sensitive runtime artifacts | Manual boundaries covered; MCP architecture denials proposed |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `prompts/*.md`, `docs/release-notes/v0.2.0.md` | Separate structured proposal contracts plus human-readable session output shapes, review examples, and release documentation that points to the contracts | Definitions, release documentation, and synthetic fixtures public; filled real outputs private | Proposal schemas and manual schema-boundary cases covered |
| Evaluation/observability | `EVALS.md`, `evals/`, `evals/future-controller-boundary-cases.md`, `examples/journal-mirror-walkthroughs/`, `examples/memory-state-proposals/`, `docs/release-checklist-v0.2.0.md`, `docs/roadmap-v0.3.0.md` | Manual regression, safety review, release verification, and planned MCP runtime tests across reflection, privacy, proposal lifecycle, and controller boundaries | Synthetic public-safe cases and control-plane checks only; private traces, content logs, and clinical validation excluded | Manual eval scope covered; MCP runtime tests planned |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/`, `docs/obsidian-private-runtime-guide.md`, `docs/v0.2-usable-product-handoff.md`, `docs/release-notes/v0.2.0.md`, `docs/release-checklist-v0.2.0.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md`, `docs/roadmap-v0.3.0.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md` | Manual private setup, public/private boundaries, and the proposed control, data, runtime-edge, interaction, and inspection planes | Runtime private data stays out of repo; the roadmap and ADR are control-plane documentation only | Manual release current; MCP runtime planned, not implemented |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, `EVALS.md`, `evals/future-controller-boundary-cases.md`, `docs/roadmap-v0.2.0.md`, `docs/roadmap-v0.3.0.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `docs/memory-state-proposal-review.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/v0.2-usable-product-handoff.md`, `docs/release-notes/v0.2.0.md`, `docs/release-checklist-v0.2.0.md` | Change history, eval lessons, review criteria, release readiness, roadmap decisions, and future sprint work | Public project tracking, release documentation, and synthetic guidance only | `v0.2.0` released; `v0.3.0` planning started |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps Entering v0.3 Planning

- Evaluation remains manual and boundary-focused; it is not clinical validation or an effectiveness measure.
- The MCP runtime architecture remains documentation-only under `docs/future-mcp-vps-controller-contract.md`, `docs/roadmap-v0.3.0.md`, and ADR 0003.
- Guided intake, initialization, connector setup, runtime tests, and the local viewer remain separate follow-up issues.
- Additional synthetic eval/example work remains separate from private use and private runtime data.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

MCP and related planning artifacts map across Tools, Memory, State, Planning/orchestration, Guardrails/governance, Evaluation/observability, Runtime/deployment, and Learning/iteration. They remain implementation-edge mappings and do not become new top-level categories.

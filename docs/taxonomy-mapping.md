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

## Repository Mapping

| # | Taxonomy bucket | Journal Agent adaptation |
|---:|---|---|
| 1 | Identity | `AGENTS.md`, `README.md`, and `docs/product-vision.md` define purpose and authority boundaries. |
| 2 | Operating style | `AGENTS.md` and `GUARDRAILS.md` require tentative, non-clinical, evidence-bound reflection. |
| 3 | Capability modules | `skills/*/SKILL.md` contains reusable task workflows. |
| 4 | Tools | `scripts/*.py` contains local validation and redaction utilities; future connectors remain implementation-edge mappings. |
| 5 | Knowledge and resources | `references/` and longer `docs/` material provide reusable context. |
| 6 | Prompts and interfaces | `prompts/`, optional `templates/`, and `docs/journal-mirror-workflow.md` define invocation and input surfaces. |
| 7 | Memory | `MEMORY.md.example` defines durable, explicitly approved context; filled Memory remains private. |
| 8 | State | `STATE.md.example` defines temporary session context; live State remains private and separate from Memory. |
| 9 | Planning and orchestration | `docs/journal-mirror-workflow.md` defines selection, reflection, proposal, and review sequencing. |
| 10 | Guardrails and governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, and ADRs define safety, privacy, and approval rules. |
| 11 | Outputs and schemas | `OUTPUT_FORMATS.md` and `schemas/` define public-safe output contracts. |
| 12 | Evaluation and observability | `EVALS.md` and `evals/` support synthetic behavior and safety checks; private traces and logs are excluded. |
| 13 | Runtime and deployment | ADR 0002 defines the public control plane and private runtime/data plane boundary without implementing hosting, MCP, or a plugin. |
| 14 | Learning and iteration | `docs/roadmap-v0.2.0.md`, `CHANGELOG.md`, and `BACKLOG.md` track planned and completed improvements. |

MCP, host adapters, and similar protocol objects may later map to several buckets, especially Tools, Guardrails and governance, and Runtime and deployment. They remain implementation-edge mappings and do not become new top-level categories.

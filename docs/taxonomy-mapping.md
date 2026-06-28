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
| Tools | `scripts/`, `mcp_server/`, `viewer/`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/chatgpt-tool-review-and-permissions.md`, `docs/future-mcp-vps-controller-contract.md` | Validation, redaction, private-vault initialization, narrow local MCP tools, and the local static viewer CLI | Public tooling and specifications; configured vaults and private outputs remain outside Git | Initializer, local MCP tools, strict apply, tool review, and local viewer covered |
| Knowledge/resources | `references/`, `docs/`, `docs/guided-intake.md`, `docs/obsidian-private-runtime-guide.md`, `docs/private-vault-runtime-package.md`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/first-run-chatgpt-walkthrough.md`, `docs/v0.2-usable-product-handoff.md` | Supporting references, private-runtime initialization, local MCP operation/approval, viewer use, ChatGPT onboarding, and public-reader handoff | Public-safe guidance only; private runtime content, viewer output, and connectivity configuration stay outside Git | Covered for intake, private setup, local MCP use/apply, local viewing, connector onboarding, and v0.2 handoff |
| Prompts/interfaces | `prompts/`, `templates/`, `docs/journal-mirror-workflow.md`, `examples/journal-mirror-walkthroughs/`, `examples/chatgpt/first-run-prompts.synthetic.md` | User-invoked guided intake/manual sessions and a synthetic ChatGPT first-run interface | Prompts and synthetic walkthroughs public; private inputs, selected context, and filled outputs private | Covered for manual intake/sessions and synthetic connector first run |
| Memory | `MEMORY.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `docs/local-runtime-viewer.md`, `schemas/memory-update-proposal.schema.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `private/memory/` | Durable approved context, allowlisted reads, separate inert proposals, exact-approved append, and a separate metadata-first viewer section | Runtime code/docs public; generated starters, real Memory, proposals, and viewer output private and outside Git | Read, pending review, strict apply, and local summary boundaries covered |
| State | `STATE.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `docs/local-runtime-viewer.md`, `schemas/state-update-proposal.schema.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `private/state/` | Temporary context, allowlisted reads, separate trigger-bearing proposals, exact-approved append, and local lifecycle-trigger visibility | Runtime code/docs public; generated starters, live State, proposals, and viewer output private and outside Git | Read, pending review, triggers, strict apply, and local summary boundaries covered |
| Planning/orchestration | `prompts/guided-intake.md`, `docs/guided-intake.md`, `docs/journal-mirror-workflow.md`, `docs/private-vault-runtime-package.md`, `mcp_server/`, `viewer/`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/roadmap-v0.3.0.md` | Guided onboarding, selected-context reflection, proposal lifecycle/status, exact apply, local runtime overview, and sprint sequencing | Public instructions/code only; generated vaults, sessions, proposals, viewer output, and connector configuration remain private | Intake, sessions, initialization, review/apply, connector onboarding, and local inspection covered |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `scripts/init-private-vault.py`, `mcp_server/vault_runtime.py`, `viewer/local_runtime_viewer.py`, `tests/`, `docs/local-runtime-viewer.md`, `evals/`, `docs/decisions/`, `docs/future-mcp-vps-controller-contract.md` | Safety, privacy, path/output refusal, destination confirmations, allowlists, raw-content hiding, denied scans/silent writes, and synthetic tests | Public rules, code, contracts, and synthetic tests; no sensitive runtime artifacts or viewer output | MCP denials/apply gates, connector review, and viewer output protections implemented |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/intake-response.schema.json`, `schemas/`, `viewer/`, `docs/local-runtime-viewer.md`, `examples/intake/guided-intake.synthetic.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/` | Separate structured proposal contracts, human-readable session/intake shapes, and the private rendered HTML summary shape | Definitions, guidance, and synthetic fixtures public; filled real outputs and generated HTML private | Intake/proposal schemas and local viewer output shape covered |
| Evaluation/observability | `viewer/`, `tests/`, `EVALS.md`, `evals/`, `evals/local-runtime-viewer-boundary-cases.md`, `examples/viewer/`, `examples/intake/`, `examples/mcp/`, `examples/chatgpt/` | Automated initializer/MCP/viewer tests plus metadata-only audit and local runtime inspection | Public-safe tests and synthetic cases only; generated viewer output, private traces, settings, and content logs excluded | Initializer/MCP/viewer tests covered; expanded eval work remains planned |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `requirements.txt`, `tests/`, `docs/mcp-local-server.md`, `docs/local-runtime-viewer.md`, `docs/private-vault-runtime-package.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/roadmap-v0.3.0.md` | Private-vault initialization, the local stdio MCP edge, local static HTML inspection, and documented remote/tunnel boundary | Runtime code/docs public; live configuration, paths, generated vault/viewer output, endpoints, and private data stay outside Git | Local MCP/apply, connector onboarding, and local viewer covered; hosting and tunnel implementation remain future work |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, `EVALS.md`, `tests/`, `docs/roadmap-v0.3.0.md`, `docs/local-runtime-viewer.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/future-mcp-vps-controller-contract.md` | Change history, executable/manual boundary lessons, review criteria, roadmap decisions, and future sprint work | Public project tracking and synthetic evidence only | `v0.2.0` released; issues #30 through #33 addressed; issue #34 is next |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps Entering v0.3 Planning

- Evaluation remains manual and boundary-focused; it is not clinical validation or an effectiveness measure.
- The local MCP runtime, strict exact-wording apply, connector onboarding docs, and local viewer are present; live connectivity and expanded runtime evals remain separate follow-up issues.
- Structured intake artifacts remain separate from private use, private runtime data, and future apply behavior.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

Guided intake maps across Prompts/interfaces, Knowledge/resources, Memory, State, Planning/orchestration, Guardrails/governance, Outputs/schemas, Evaluation/observability, and Learning/iteration. The private-vault package, local MCP workflow, connector onboarding, and local viewer map across the existing categories. These mappings do not create new top-level categories; the taxonomy remains exactly 14 buckets.

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
| Tools | `scripts/`, `mcp_server/`, `viewer/`, `tests/test_mcp_runtime_safety_regressions.py`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/chatgpt-tool-review-and-permissions.md`, `docs/future-mcp-vps-controller-contract.md` | Validation, redaction, private-vault initialization, narrow local MCP tools, and the local static viewer CLI | Public tooling and specifications; configured vaults and private outputs remain outside Git | Initializer, local MCP tools, strict apply, tool review, viewer, and boundary regression covered |
| Knowledge/resources | `references/`, `docs/`, `docs/guided-intake.md`, `docs/obsidian-private-runtime-guide.md`, `docs/private-vault-runtime-package.md`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/first-run-chatgpt-walkthrough.md`, `docs/release-notes/`, `docs/v0.3-usable-product-handoff.md` | Supporting references, private-runtime initialization, local MCP operation/approval, viewer use, ChatGPT onboarding, release history, and public-reader handoff | Public-safe guidance only; private runtime content, viewer output, and connectivity configuration stay outside Git | Covered for intake, private setup, local MCP use/apply, local viewing, connector onboarding, and v0.3 handoff |
| Prompts/interfaces | `prompts/`, `templates/`, `docs/journal-mirror-workflow.md`, `examples/journal-mirror-walkthroughs/`, `examples/chatgpt/first-run-prompts.synthetic.md`, `evals/prompt-injection-boundary-cases.md`, `evals/clinical-safety-boundary-cases.md` | User-invoked guided intake/manual sessions, a synthetic ChatGPT first-run interface, and public-safe boundary scenarios | Prompts and synthetic walkthroughs public; private inputs, selected context, and filled outputs private | Covered for manual intake/sessions, connector first run, injection, and safety routing |
| Memory | `MEMORY.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `docs/local-runtime-viewer.md`, `schemas/memory-update-proposal.schema.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `private/memory/` | Durable approved context, allowlisted reads, separate inert proposals, exact-approved append, and a separate metadata-first viewer section | Runtime code/docs public; generated starters, real Memory, proposals, and viewer output private and outside Git | Read, pending review, strict apply, and local summary boundaries covered |
| State | `STATE.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `docs/local-runtime-viewer.md`, `schemas/state-update-proposal.schema.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `private/state/` | Temporary context, allowlisted reads, separate trigger-bearing proposals, exact-approved append, and local lifecycle-trigger visibility | Runtime code/docs public; generated starters, live State, proposals, and viewer output private and outside Git | Read, pending review, triggers, strict apply, and local summary boundaries covered |
| Planning/orchestration | `prompts/guided-intake.md`, `docs/guided-intake.md`, `docs/journal-mirror-workflow.md`, `docs/private-vault-runtime-package.md`, `mcp_server/`, `viewer/`, `docs/mcp-proposal-approval-workflow.md`, `docs/local-runtime-viewer.md`, `docs/roadmap-v0.3.0.md`, `docs/v0.3-usable-product-handoff.md` | Guided onboarding, selected-context reflection, proposal lifecycle/status, exact apply, local runtime overview, release handoff, and sprint sequencing | Public instructions/code only; generated vaults, sessions, proposals, viewer output, and connector configuration remain private | Intake, sessions, initialization, review/apply, connector onboarding, local inspection, and handoff covered |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `docs/release-checklist-v0.3.0.md`, `scripts/init-private-vault.py`, `mcp_server/vault_runtime.py`, `viewer/local_runtime_viewer.py`, `tests/`, `evals/mcp-runtime-boundary-cases.md`, `evals/prompt-injection-boundary-cases.md`, `evals/clinical-safety-boundary-cases.md`, `docs/decisions/`, `docs/future-mcp-vps-controller-contract.md` | Safety, privacy, release constraints, injection handling, clinical scope, path/output refusal, destination confirmations, allowlists, raw-content hiding, denied scans/silent writes, and synthetic tests | Public rules, code, contracts, and synthetic tests; no sensitive runtime artifacts or viewer output | MCP denials/apply gates, prompt-injection, clinical scope, connector/release review, and viewer protections covered |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/intake-response.schema.json`, `schemas/`, `viewer/`, `docs/local-runtime-viewer.md`, `examples/intake/guided-intake.synthetic.json`, `examples/viewer/`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/` | Separate structured proposal contracts, human-readable session/intake shapes, and the private rendered HTML summary shape | Definitions, guidance, and synthetic fixtures public; filled real outputs and generated HTML private | Intake/proposal schemas and local viewer output shape covered |
| Evaluation/observability | `viewer/`, `tests/`, `tests/test_mcp_runtime_safety_regressions.py`, `EVALS.md`, `evals/`, `docs/runtime-validation-checklist.md`, `docs/release-checklist-v0.3.0.md`, `examples/` | Automated initializer/MCP/viewer/integrated runtime tests, release gates, metadata-only audit, local inspection, and manual safety regression | Public-safe tests, checklists, and synthetic cases only; generated viewer output, private traces, settings, and content logs excluded | Expanded runtime/manual eval coverage and v0.3 release validation implemented |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/init-private-vault.py`, `mcp_server/`, `viewer/`, `requirements.txt`, `tests/`, `docs/mcp-local-server.md`, `docs/local-runtime-viewer.md`, `docs/runtime-validation-checklist.md`, `docs/private-vault-runtime-package.md`, `docs/v0.3-usable-product-handoff.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/roadmap-v0.3.0.md` | Private-vault initialization, the local stdio MCP edge, local static HTML inspection, synthetic validation, usable-product handoff, and documented remote/tunnel boundary | Runtime code/docs public; live configuration, paths, generated vault/viewer output, endpoints, and private data stay outside Git | Local MCP/apply, connector onboarding, viewer, validation, and handoff covered; hosting/tunnel remain future work |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, `EVALS.md`, `tests/`, `docs/release-notes/v0.3.0.md`, `docs/release-checklist-v0.3.0.md`, `docs/runtime-validation-checklist.md`, `docs/roadmap-v0.3.0.md`, `docs/local-runtime-viewer.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/chatgpt-mcp-connector-setup.md`, `docs/future-mcp-vps-controller-contract.md` | Change history, release readiness, executable/manual boundary lessons, validation criteria, roadmap decisions, and future sprint work | Public project tracking and synthetic evidence only | Issues #26 through #35 addressed; v0.3 tag/release remains a post-merge action |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps After v0.3 Readiness

- Evaluation remains manual and boundary-focused; it is not clinical validation or an effectiveness measure.
- The local MCP runtime, strict exact-wording apply, connector onboarding docs, local viewer, expanded runtime evals, and release-readiness package are present; live connectivity and production hardening remain separate work.
- Structured intake artifacts remain separate from private use, private runtime data, and future apply behavior.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

Guided intake maps across Prompts/interfaces, Knowledge/resources, Memory, State, Planning/orchestration, Guardrails/governance, Outputs/schemas, Evaluation/observability, and Learning/iteration. The private-vault package, local MCP workflow, connector onboarding, local viewer, runtime regressions, safety evals, release documents, usable-product handoff, and validation checklists map across the existing categories. These mappings do not create new top-level categories; the taxonomy remains exactly 14 buckets.

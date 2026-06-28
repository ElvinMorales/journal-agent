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
| Tools | `scripts/`, `mcp_server/`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/future-mcp-vps-controller-contract.md` | Validation, redaction, private-vault initialization, and the narrow local MCP review/apply tool surface | Public tooling and specifications; configured vaults and private outputs remain outside Git | Initializer, local MCP tools, and strict exact-wording apply covered |
| Knowledge/resources | `references/`, `docs/`, `docs/guided-intake.md`, `docs/obsidian-private-runtime-guide.md`, `docs/private-vault-runtime-package.md`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `examples/mcp/proposal-approval-workflow.synthetic.md`, `docs/v0.2-usable-product-handoff.md` | Supporting references, guided-intake guidance, private-runtime initialization, local MCP operation and approval workflow, and public-reader handoff | Public-safe guidance only; intake answers and private runtime content stay outside Git | Covered for intake, private setup, local MCP use/apply, and v0.2 handoff |
| Prompts/interfaces | `prompts/guided-intake.md`, `prompts/journal-mirror-session.md`, `prompts/freeform-entry-mirror.md`, `prompts/recent-pattern-review.md`, `prompts/gentle-next-action.md`, `prompts/update-proposal-review.md`, `templates/`, `docs/journal-mirror-workflow.md`, `examples/journal-mirror-walkthroughs/` | User-invoked guided intake and manual session surfaces, optional templates, and public-safe demonstrations | Prompts and synthetic walkthroughs public; intake answers, selected context, and filled outputs private | Covered for manual intake and sessions |
| Memory | `MEMORY.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `schemas/memory-update-proposal.schema.json`, `examples/mcp/`, `examples/memory-state-proposals/`, `docs/memory-state-proposal-review.md`, `private/memory/` | Durable approved context, allowlisted local reads, separate inert pending proposals, and exact-approved append | Runtime code public; generated starters, real Memory, and proposals private and outside Git | Read, pending review, and strict apply boundaries covered |
| State | `STATE.md.example`, `scripts/init-private-vault.py`, `mcp_server/`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `schemas/state-update-proposal.schema.json`, `examples/mcp/`, `examples/memory-state-proposals/`, `docs/memory-state-proposal-review.md`, `private/state/` | Temporary context, allowlisted local reads, separate trigger-bearing pending proposals, and exact-approved append with lifecycle triggers | Runtime code public; generated starters, live State, and proposals private and outside Git | Read, pending review, trigger, and strict apply boundaries covered |
| Planning/orchestration | `prompts/guided-intake.md`, `docs/guided-intake.md`, `docs/journal-mirror-workflow.md`, `docs/private-vault-runtime-package.md`, `mcp_server/`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/memory-state-proposal-review.md`, `docs/roadmap-v0.3.0.md` | Guided onboarding, selected-context reflection, private setup, proposal lifecycle/status, separate exact-wording apply, and sprint sequencing | Public instructions and code only; generated vaults, intake answers, sessions, and proposals remain private | Intake, sessions, initialization, review, and strict local apply covered |
| Guardrails/governance | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`, `scripts/init-private-vault.py`, `mcp_server/vault_runtime.py`, `tests/test_mcp_server_boundaries.py`, `tests/test_mcp_proposal_apply_workflow.py`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `evals/`, `docs/decisions/`, `docs/future-mcp-vps-controller-contract.md` | Safety, privacy, path refusal, destination confirmations, write allowlists, denied scans and arbitrary access, no silent writes, exact-wording approval boundaries, and synthetic tests | Public rules, code, contracts, and synthetic tests; no sensitive runtime artifacts | Local MCP denials and exact-wording apply gates are implemented and tested |
| Outputs/schemas | `OUTPUT_FORMATS.md`, `schemas/intake-response.schema.json`, `schemas/`, `prompts/guided-intake.md`, `docs/guided-intake.md`, `examples/intake/guided-intake.synthetic.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md` | Separate structured proposal contracts plus human-readable session output and a structured proposal-only intake bundle | Definitions, guidance, and synthetic fixtures public; filled real outputs private | Intake response and destination-specific proposal schemas covered |
| Evaluation/observability | `tests/test_init_private_vault.py`, `tests/test_mcp_server_boundaries.py`, `tests/test_mcp_proposal_apply_workflow.py`, `EVALS.md`, `evals/`, `examples/intake/`, `examples/mcp/`, `examples/journal-mirror-walkthroughs/`, `examples/memory-state-proposals/` | Automated initializer and local MCP boundary/apply tests, metadata-only audit behavior, manual regression, safety review, and release verification | Public-safe tests and synthetic cases only; private traces, content logs, and clinical validation excluded | Initializer and strict MCP proposal/apply tests covered; expanded eval work remains planned |
| Runtime/deployment | `mobile/`, `.gitignore`, `.github/workflows/`, `scripts/init-private-vault.py`, `mcp_server/`, `requirements.txt`, `tests/test_mcp_server_boundaries.py`, `tests/test_mcp_proposal_apply_workflow.py`, `docs/mcp-local-server.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/private-vault-runtime-package.md`, `docs/future-mcp-vps-controller-contract.md`, `docs/roadmap-v0.3.0.md` | Private-vault initialization and the local stdio MCP runtime edge within the control/data-plane architecture | Runtime code is public; configured paths, generated vaults, and private data stay outside the repo | Local MCP read, proposal, review, and strict apply covered; connector, hosting, tunnel, and viewer remain future work |
| Learning/iteration | `CHANGELOG.md`, `BACKLOG.md`, `EVALS.md`, `tests/test_mcp_server_boundaries.py`, `tests/test_mcp_proposal_apply_workflow.py`, `docs/roadmap-v0.3.0.md`, `docs/guided-intake.md`, `docs/decisions/0003-journal-mirror-mcp-runtime.md`, `docs/memory-state-proposal-review.md`, `docs/mcp-proposal-approval-workflow.md`, `docs/future-mcp-vps-controller-contract.md` | Change history, executable boundary lessons, review criteria, roadmap decisions, and future sprint work | Public project tracking and synthetic evidence only | `v0.2.0` released; issues #30 and #31 local runtime/apply addressed; issue #32 connector guidance is next |

## Intentional Non-Goals

- Do not store real journal entries in the public repo.
- Do not create a therapy app, mental health product, diagnostic tool, or treatment planner.
- Do not add automatic memory writing or clinical scoring.
- Do not create a hosted API, private journal database, PWA, or Obsidian plugin for this release.
- Do not add vendor-specific framework lock-in.
- Do not treat Strategic Mirror Agent as the taxonomy source of truth.

## Known Gaps Entering v0.3 Planning

- Evaluation remains manual and boundary-focused; it is not clinical validation or an effectiveness measure.
- The local MCP runtime, strict exact-wording apply, and boundary tests are present; connector setup, expanded runtime evals, and the local viewer remain separate follow-up issues.
- Structured intake artifacts remain separate from private use, private runtime data, and future apply behavior.

## Note on Bucket Coverage

Not every taxonomy bucket requires a new file immediately. Some buckets are represented by existing artifacts, some are intentionally partial, and some are documented as boundaries rather than implemented runtime systems.

Guided intake maps across Prompts/interfaces, Knowledge/resources, Memory, State, Planning/orchestration, Guardrails/governance, Outputs/schemas, Evaluation/observability, and Learning/iteration. The private-vault package and local MCP approval/apply workflow map across Tools, Knowledge/resources, Memory, State, Planning/orchestration, Guardrails/governance, Evaluation/observability, Runtime/deployment, and Learning/iteration. These mappings do not create new top-level categories; the taxonomy remains exactly 14 buckets.

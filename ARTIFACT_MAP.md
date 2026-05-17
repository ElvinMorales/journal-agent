# Artifact Map

This map explains the role, loading mode, and activation control for the repository artifacts.

| Category | Role | Loading Mode | Activation Control | Path |
|---|---|---:|---|---|
| Identity | Always-on repo instruction | Always-on | Agent/tool | `AGENTS.md` |
| Product docs | Human and agent orientation | On demand | Human/agent | `README.md`, `docs/product-vision.md` |
| Artifact map | Navigation and ownership | On demand | Human/agent | `ARTIFACT_MAP.md`, `docs/agent-artifacts/README.md` |
| Guardrails | Safety boundaries | Always-on/reference | Agent/tool | `GUARDRAILS.md`, `docs/safety-model.md` |
| Privacy | Sensitive-data policy | Always-on/reference | Agent/tool | `PRIVACY.md`, `docs/journal-data-lifecycle.md` |
| Capabilities | Task workflows | Triggered | Agent | `skills/*/SKILL.md` |
| Knowledge | Long-form source material | On demand | Agent | `references/` |
| Outputs | Structured contracts | On demand/tooling | Agent/tool | `OUTPUT_FORMATS.md`, `schemas/*.json` |
| Prompts | User-invoked flows | User-controlled | User | `prompts/*.md` |
| Templates | User-owned journal artifacts | User-controlled | User/agent | `templates/*.md` |
| Mobile starter pack | Phone-first no-code workflows and shortcut specs | On demand | Human | `mobile/` |
| Memory | Durable user facts, if consented | On demand/private | Human/agent | `MEMORY.md.example`, `private/memory/` |
| State | Session continuity | On demand/private | Human/agent | `STATE.md.example`, `private/state/` |
| Evaluation | Regression and safety review | On demand | Human/tool | `EVALS.md`, `evals/*` |
| Iteration | Change tracking and backlog | On demand | Human/agent | `CHANGELOG.md`, `BACKLOG.md` |
| Runtime tools | Validation and redaction | Tool-triggered | Human/agent | `scripts/*.py` |

## Progressive Disclosure

Keep always-on artifacts short. Load skills only when their descriptions match the task. Load references and docs only when deeper context is needed.

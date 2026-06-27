# Artifact Map

This map relates the public scaffold to the original 14-bucket agentic AI artifact taxonomy. It maps design-time files and public-safe examples, not a live private runtime inventory.

It also shows how repo files relate to the Agentic AI Artifact Taxonomy. See `docs/taxonomy-mapping.md` for the full 14-bucket mapping.

| Taxonomy bucket | Role in this repo | Primary paths |
|---|---|---|
| 1. Identity | Defines the Journal Mirror purpose and scope. | `AGENTS.md`, `README.md`, `docs/product-vision.md` |
| 2. Operating style | Defines tentative, non-clinical reflection behavior. | `AGENTS.md`, `GUARDRAILS.md` |
| 3. Capability modules | Packages task workflows. | `skills/*/SKILL.md` |
| 4. Tools | Provides local validation and redaction utilities. | `scripts/*.py` |
| 5. Knowledge and resources | Holds longer reusable references. | `references/`, `docs/` |
| 6. Prompts and interfaces | Defines user-invoked reflection surfaces. The Journal Mirror workflow is a primary interface description. | `prompts/*.md`, `templates/*.md`, `docs/journal-mirror-workflow.md` |
| 7. Memory | Defines durable, user-approved context without storing live Memory publicly. | `MEMORY.md.example`, `private/memory/` |
| 8. State | Defines temporary session context without storing live State publicly. | `STATE.md.example`, `private/state/` |
| 9. Planning and orchestration | Defines the post-writing session flow and review gates. | `docs/journal-mirror-workflow.md` |
| 10. Guardrails and governance | Defines safety, privacy, approvals, and architectural decisions. | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md` |
| 11. Outputs and schemas | Defines structured response contracts. | `OUTPUT_FORMATS.md`, `schemas/*.json` |
| 12. Evaluation and observability | Supports synthetic regression and safety review. | `EVALS.md`, `evals/*` |
| 13. Runtime and deployment | Defines the public-control-plane/private-data-plane boundary without implementing a runtime. | `docs/decisions/0002-journal-mirror-runtime-pattern.md`, `mobile/` |
| 14. Learning and iteration | Tracks release direction and follow-up work. | `docs/roadmap-v0.2.0.md`, `CHANGELOG.md`, `BACKLOG.md` |

`docs/journal-mirror-workflow.md` maps mainly to Planning and orchestration and Prompts and interfaces. `docs/roadmap-v0.2.0.md` maps mainly to Learning and iteration. `docs/decisions/0002-journal-mirror-runtime-pattern.md` maps mainly to Guardrails and governance and Runtime and deployment.

## Progressive Disclosure

Keep always-on artifacts short. Load skills only when their descriptions match the task. Load references and docs only when deeper context is needed.

For the complete repo-specific mapping and source-of-truth boundary, see `docs/taxonomy-mapping.md`.
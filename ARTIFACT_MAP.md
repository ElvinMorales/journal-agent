# Artifact Map

This map relates the public scaffold to the original 14-bucket agentic AI artifact taxonomy. It maps design-time files and public-safe examples, not a live private runtime inventory.

It also shows how repo files relate to the Agentic AI Artifact Taxonomy. See `docs/taxonomy-mapping.md` for the full 14-bucket mapping.

| Taxonomy bucket | Role in this repo | Primary paths |
|---|---|---|
| 1. Identity | Defines the Journal Mirror purpose and scope. | `AGENTS.md`, `README.md`, `docs/product-vision.md` |
| 2. Operating style | Defines tentative, non-clinical reflection behavior. | `AGENTS.md`, `GUARDRAILS.md` |
| 3. Capability modules | Packages task workflows, including selected-context sessions, pattern reflection, and update review, with synthetic cases exercising their boundaries. | `skills/journal-mirror-session/SKILL.md`, `skills/summarizing-journal-patterns/SKILL.md`, `skills/memory-state-review/SKILL.md`, `skills/*/SKILL.md`, `evals/journal-mirror-session-cases.md`, `evals/memory-state-proposal-cases.md` |
| 4. Tools | Provides local validation and redaction utilities. | `scripts/*.py` |
| 5. Knowledge and resources | Holds longer reusable references, including private setup guidance. | `references/`, `docs/`, `docs/obsidian-private-runtime-guide.md` |
| 6. Prompts and interfaces | Defines user-invoked reflection, pattern review, next-action, and proposal-review surfaces, demonstrated by public-safe walkthroughs. | `prompts/journal-mirror-session.md`, `prompts/freeform-entry-mirror.md`, `prompts/recent-pattern-review.md`, `prompts/gentle-next-action.md`, `prompts/update-proposal-review.md`, `prompts/*.md`, `templates/*.md`, `examples/journal-mirror-walkthroughs/` |
| 7. Memory | Defines durable, user-approved context and review-only proposals without storing live Memory publicly. | `MEMORY.md.example`, `schemas/memory-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/memory-state-review.synthetic.md`, `evals/memory-state-proposal-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `private/memory/` |
| 8. State | Defines temporary session context and review-only proposals without storing live State publicly. | `STATE.md.example`, `schemas/state-update-proposal.schema.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `prompts/update-proposal-review.md`, `skills/memory-state-review/SKILL.md`, `docs/memory-state-proposal-review.md`, `private/state/` |
| 9. Planning and orchestration | Defines selected-context session flow, manual private setup, and review gates. | `skills/journal-mirror-session/SKILL.md`, `docs/journal-mirror-workflow.md`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md` |
| 10. Guardrails and governance | Defines safety, privacy, trust metadata, approvals, architectural decisions, and synthetic boundary tests. | `GUARDRAILS.md`, `PRIVACY.md`, `SECURITY.md`, `skills/*/SKILL.md`, `evals/safety-boundary-cases.md`, `evals/journal-mirror-session-cases.md`, `docs/obsidian-private-runtime-guide.md`, `docs/memory-state-proposal-review.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md` |
| 11. Outputs and schemas | Defines structured response contracts and human-readable session output shapes, with synthetic examples and schema-boundary cases. | `OUTPUT_FORMATS.md`, `schemas/*.json`, `examples/memory-state-proposals/`, `examples/journal-mirror-walkthroughs/`, `evals/memory-state-proposal-cases.md`, `prompts/*.md` |
| 12. Evaluation and observability | Supports manual synthetic regression and safety review across session reflection, proposal lifecycle, privacy, clinical scope, and crisis routing. | `EVALS.md`, `evals/*`, `examples/journal-mirror-walkthroughs/`, `examples/memory-state-proposals/` |
| 13. Runtime and deployment | Defines the public-control-plane/private-data-plane boundary and manual private setup without implementing a live runtime. | `docs/obsidian-private-runtime-guide.md`, `docs/decisions/0002-journal-mirror-runtime-pattern.md`, `mobile/` |
| 14. Learning and iteration | Tracks release direction, proposal-review lessons, eval coverage, and follow-up work. | `docs/roadmap-v0.2.0.md`, `docs/memory-state-proposal-review.md`, `EVALS.md`, `CHANGELOG.md`, `BACKLOG.md` |

`docs/journal-mirror-workflow.md` maps mainly to Planning and orchestration and Prompts and interfaces. `docs/obsidian-private-runtime-guide.md` maps mainly to Knowledge and resources, Planning and orchestration, Guardrails and governance, and Runtime and deployment. `docs/roadmap-v0.2.0.md` maps mainly to Learning and iteration. `docs/decisions/0002-journal-mirror-runtime-pattern.md` maps mainly to Guardrails and governance and Runtime and deployment.

The proposal fixtures and Journal Mirror walkthroughs provide inspectable synthetic paths through Evaluation and observability. They support manual boundary regression; they are not private traces, clinical validation, or runtime telemetry.

## Progressive Disclosure

Keep always-on artifacts short. Load skills only when their descriptions match the task. Load references and docs only when deeper context is needed.

For the complete repo-specific mapping and source-of-truth boundary, see `docs/taxonomy-mapping.md`.

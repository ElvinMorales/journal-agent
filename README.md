# Journal Mirror Agent

`journal-agent` is a public, file-first scaffold for a private-first Journal Mirror Agent and a reference implementation of the Agentic AI Artifact Taxonomy. `v0.2.0` is the current manual/control-plane release: it supports natural private writing first, selected-context reflection after, and reviewable Memory or State update proposals.

It does not store journal entries and it is not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, a mental health product, clinical decision support system, hosted service, Obsidian plugin, or private journal database.

The public repo is the reusable control plane. A private Obsidian vault or other user-controlled notes system is the data plane. Private journal content and all real runtime artifacts belong outside the repo.

Taxonomy source of truth: [agentic-ai-artifact-taxonomy](https://github.com/ElvinMorales/agentic-ai-artifact-taxonomy.git)

## What This Repo Is

- A public-safe artifact system for building a private AI-assisted journaling companion.
- A practical mapping of repo files to the 14 buckets in the Agentic AI Artifact Taxonomy.
- A reusable set of instructions, guardrails, privacy rules, prompts, schemas, templates, evals, and mobile workflow docs.
- A documentation-first reference implementation that keeps private journal content out of Git.

## What This Repo Is Not

- Not therapy, diagnosis, crisis counseling, medical advice, treatment planning, medication guidance, or a replacement for licensed care.
- Not a mental health product or clinical decision support system.
- Not a private journal database, hosted service, Obsidian plugin, PWA, or app backend.
- Not a place to store real journal entries, summaries, memory, state, logs, screenshots, exports, therapy notes, crisis notes, secrets, or identifying details.

## Public Artifacts vs Private Journal Content

Committed files are reusable control-plane artifacts: they define how the companion should behave, what boundaries it must respect, and what output structures it may use.

Private journal content belongs in the user's private data plane, such as:

- A private Obsidian vault.
- Ignored local folders such as `private/`.
- Another user-controlled private notes or storage system.

The `private/` directory is ignored by default except for placeholder `.gitkeep` files. Treat anything written there as local-only unless it is deliberately reviewed, redacted, and exported by the user.

## How This Applies the Taxonomy

The Agentic AI Artifact Taxonomy defines an agentic AI artifact as anything an agent system depends on that should be addressable, versionable, inspectable, and governable.

This repo applies that lens to a journaling companion by making public artifacts inspectable while keeping real runtime journal data private. See:

- `docs/taxonomy-mapping.md` for the 14-bucket mapping.
- `docs/architecture.md` for the public/private architecture.
- `docs/decisions/0001-public-artifacts-private-journal.md` for the core boundary decision.
- `docs/decisions/0002-journal-mirror-runtime-pattern.md` for the Journal Mirror runtime-pattern decision.
- `docs/roadmap-v0.2.0.md` for the v0.2 planning direction.
- [`docs/roadmap-v0.3.0.md`](docs/roadmap-v0.3.0.md) for the MCP runtime and guided-intake sprint direction.
- [`docs/decisions/0003-journal-mirror-mcp-runtime.md`](docs/decisions/0003-journal-mirror-mcp-runtime.md) for the proposed local/private MCP runtime architecture.
- `docs/journal-mirror-workflow.md` for the post-writing reflection workflow.
- [Private runtime starter guide](docs/obsidian-private-runtime-guide.md) for a manual setup that works with Obsidian or any private notes system, with no plugin or server required.
- [Future MCP/VPS controller contract](docs/future-mcp-vps-controller-contract.md) for the design-only boundary of a possible private runtime edge; it includes no MCP/VPS server or controller implementation.

## Start Here

For the shortest orientation, read the [v0.2 usable-product handoff](docs/v0.2-usable-product-handoff.md). Then follow this manual flow:

1. Write naturally in a private Obsidian vault or another user-controlled private notes system.
2. Use the [private runtime starter guide](docs/obsidian-private-runtime-guide.md) to set up a minimal private workflow, then start with the [Journal Mirror workflow](docs/journal-mirror-workflow.md), [session prompt](prompts/journal-mirror-session.md), or [freeform entry prompt](prompts/freeform-entry-mirror.md) and one selected entry, excerpt, or small group of entries.
3. Review any proposed Memory or State updates with the [proposal review guide](docs/memory-state-proposal-review.md) and separate [Memory](schemas/memory-update-proposal.schema.json) or [State](schemas/state-update-proposal.schema.json) schema before manually copying, editing, or discarding them. Proposals are review-only; nothing changes automatically.
4. Use `templates/` only when a structured starting point is helpful; templates are optional, not a required journal format.

Release readers should also review the [v0.2.0 release notes](docs/release-notes/v0.2.0.md) and [v0.2.0 release checklist](docs/release-checklist-v0.2.0.md).

See [all session prompts](prompts/), the [Journal Mirror session capability](skills/journal-mirror-session/SKILL.md), and the [Memory/State review capability](skills/memory-state-review/SKILL.md). Read `docs/journal-mirror-workflow.md` for the complete flow, `docs/memory-state-proposal-review.md` for the proposal lifecycle and publishing checklist, `ARTIFACT_MAP.md` for the artifact layout, and `GUARDRAILS.md` before running reflection workflows.

To inspect the flow without private content, use the [synthetic Journal Mirror walkthroughs](examples/journal-mirror-walkthroughs/) and the [manual synthetic eval suite](EVALS.md). They demonstrate selected-context reflection, proposal review, expiration, privacy limits, and safety routing; they are not private traces or clinical validation.

## v0.2.0 Scope

`v0.2.0` adds usable manual Journal Mirror sessions, private-notes setup guidance, prompt and capability surfaces, separate reviewable Memory and State proposal contracts, synthetic walkthroughs and evals, and a design-only future controller contract. It does not add a live MCP/VPS runtime, vault access, an Obsidian plugin, automatic persistence, a clinical product, or crisis automation.

The `v0.2.0` manual workflow remains the usable path while `v0.3.0` is planned and built.

## v0.3.0 Planning Status

`v0.3.0` planning has started under issue #25. The sprint will focus on a narrow MCP runtime, guided intake, private-vault initialization, proposal approval and exact-wording apply, ChatGPT connector setup, runtime tests and safety evals, release readiness, and eventually an optional local HTML viewer.

No MCP runtime, connector setup, private-vault initializer, or local viewer exists yet. The [v0.3.0 roadmap](docs/roadmap-v0.3.0.md) defines the planned user flow and sprint groups; [ADR 0003](docs/decisions/0003-journal-mirror-mcp-runtime.md) records the proposed architecture and denied operations without implementing them.

## Safety and Privacy Warnings

Do not commit filled journal entries, private notes, summaries, memory, state, exports, crisis notes, therapy notes, logs, databases, environment files, secrets, screenshots, local identifying paths, or identifying information.

Use synthetic examples only. If crisis indicators appear in actual use, stop ordinary reflection and prioritize immediate safety, trusted human support, emergency or crisis resources, and reducing access to harm.

## For Contributors

- Read `CONTRIBUTING.md` before opening issues or pull requests.
- Report sensitive-data exposure or safety issues using `SECURITY.md`.
- Run the synthetic manual checks described in `EVALS.md` after changing prompts, capabilities, guardrails, or proposal review behavior.
- Run `python scripts/validate-json-schemas.py` after schema changes.

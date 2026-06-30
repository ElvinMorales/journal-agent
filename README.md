# Journal Mirror Agent

`journal-agent` is a public, file-first scaffold for a private-first Journal Mirror Agent and a reference implementation of the Agentic AI Artifact Taxonomy. `v0.3.0` is the current tagged release; it adds an optional local/private MCP runtime prototype, guided intake, strict proposal apply, connector onboarding documentation, and a local static viewer. The `v0.2.0` manual/control-plane workflow remains supported.

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
- Not a private journal database, hosted service, Obsidian plugin, PWA, or app backend. The local MCP server is a narrow stdio process, not a hosted service.
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
- [Guided intake prompt](prompts/guided-intake.md) and [guided intake guide](docs/guided-intake.md), supported by an [intake response schema](schemas/intake-response.schema.json), [synthetic example](examples/intake/guided-intake.synthetic.json), [review walkthrough](examples/intake/intake-to-memory-state-proposals.synthetic.md), and [boundary evals](evals/intake-boundary-cases.md). These artifacts create reviewable pending proposals only; they do not persist data.
- [Private vault runtime package](docs/private-vault-runtime-package.md) and [`scripts/init-private-vault.py`](scripts/init-private-vault.py) for creating a blank, generic private runtime structure at an explicit path outside this repository. The initializer writes no private content and runs no Git commands.
- [Minimal local MCP server](docs/mcp-local-server.md) for nine narrow selected-context, approved Memory, current State, pending-proposal review, exact-approved-wording apply, and metadata-only audit tools. The [proposal approval workflow](docs/mcp-proposal-approval-workflow.md) requires exact wording, destination-specific confirmation, and an allowlisted target; it exposes no arbitrary filesystem operation.
- [Runtime validation checklist](docs/runtime-validation-checklist.md) and the [MCP runtime](evals/mcp-runtime-boundary-cases.md), [prompt-injection](evals/prompt-injection-boundary-cases.md), and [clinical/safety](evals/clinical-safety-boundary-cases.md) eval matrices for synthetic-only boundary regression.
- [ChatGPT connector setup](docs/chatgpt-mcp-connector-setup.md), [first-run walkthrough](docs/first-run-chatgpt-walkthrough.md), and [tool review/permissions guide](docs/chatgpt-tool-review-and-permissions.md) for safely onboarding the existing MCP server with synthetic prompts. These are documentation only: no connector configuration, endpoint, tunnel, hosted deployment, or private data is committed.
- [v0.3.0 release notes](docs/release-notes/v0.3.0.md), [release checklist](docs/release-checklist-v0.3.0.md), and [usable-product handoff](docs/v0.3-usable-product-handoff.md) for the release scope, final gates, limitations, and practical local/private path.
- `docs/journal-mirror-workflow.md` for the post-writing reflection workflow.
- [Private runtime starter guide](docs/obsidian-private-runtime-guide.md) for a manual setup that works with Obsidian or any private notes system, with no plugin or server required.
- [Future MCP/VPS controller contract](docs/future-mcp-vps-controller-contract.md) for the design-only boundary of a possible private runtime edge; it includes no MCP/VPS server or controller implementation.

## Start Here

For the optional local runtime path, start with the [v0.3 usable-product handoff](docs/v0.3-usable-product-handoff.md). The [v0.2 handoff](docs/v0.2-usable-product-handoff.md) remains the shortest orientation to the manual workflow. The v0.3 path is:

1. Optionally run the [guided intake prompt](prompts/guided-intake.md) to describe reflection preferences, boundaries, and current context in plain language. Review the separate pending proposals; intake writes nothing.
2. Create a blank private runtime outside this repo with the [private vault initializer](docs/private-vault-runtime-package.md), or follow the [manual private runtime starter guide](docs/obsidian-private-runtime-guide.md).
3. Write naturally in a private Obsidian vault or another user-controlled private notes system, then start with the [Journal Mirror workflow](docs/journal-mirror-workflow.md), [session prompt](prompts/journal-mirror-session.md), or [freeform entry prompt](prompts/freeform-entry-mirror.md) and one selected entry, excerpt, or small group of entries.
4. Review any proposed Memory or State updates with the [proposal review guide](docs/memory-state-proposal-review.md) and separate [Memory](schemas/memory-update-proposal.schema.json) or [State](schemas/state-update-proposal.schema.json) schema. Manual copying remains supported; the local MCP path can separately apply only exact wording approved for one destination through the [proposal approval workflow](docs/mcp-proposal-approval-workflow.md).
5. For an optional ChatGPT test, follow the [connector setup](docs/chatgpt-mcp-connector-setup.md) and [synthetic first-run walkthrough](docs/first-run-chatgpt-walkthrough.md). ChatGPT cannot connect directly to local stdio; a separately reviewed reachable MCP endpoint or Secure MCP Tunnel path is required.
6. Use `templates/` only when a structured starting point is helpful; templates are optional, not a required journal format.

Release readers should review the [v0.3.0 release notes](docs/release-notes/v0.3.0.md), [release checklist](docs/release-checklist-v0.3.0.md), [runtime validation checklist](docs/runtime-validation-checklist.md), and [final public-safety verification](docs/release-verification/v0.3.0-final-public-safety-verification.md). The `v0.3.0` tag and GitHub release were published on June 29, 2026; issue #46 records the final verification without modifying either release artifact.

See [all session prompts](prompts/), the [Journal Mirror session capability](skills/journal-mirror-session/SKILL.md), and the [Memory/State review capability](skills/memory-state-review/SKILL.md). Read `docs/journal-mirror-workflow.md` for the complete flow, `docs/memory-state-proposal-review.md` for the proposal lifecycle and publishing checklist, `ARTIFACT_MAP.md` for the artifact layout, and `GUARDRAILS.md` before running reflection workflows.

To inspect the flow without private content, use the [synthetic Journal Mirror walkthroughs](examples/journal-mirror-walkthroughs/) and the [manual synthetic eval suite](EVALS.md). They demonstrate selected-context reflection, proposal review, expiration, privacy limits, and safety routing; they are not private traces or clinical validation.

## v0.2.0 Scope

`v0.2.0` adds usable manual Journal Mirror sessions, private-notes setup guidance, prompt and capability surfaces, separate reviewable Memory and State proposal contracts, synthetic walkthroughs and evals, and a design-only future controller contract. It does not add a live MCP/VPS runtime, vault access, an Obsidian plugin, automatic persistence, a clinical product, or crisis automation.

The `v0.2.0` manual workflow remains supported; the released `v0.3.0` local runtime path is optional.

## v0.3.0 Release Status

Issue #35 prepared `v0.3.0` for release after issues #26 through #34 delivered the planned local runtime surfaces. The tag and GitHub release were published on June 29, 2026. Issue #46 records the final public-safety and release-readiness verification; it does not modify the tag or GitHub release. Guided intake provides a manual, plain-language way to avoid starting from a blank slate, plus a schema, synthetic example, review walkthrough, and boundary evals for separate pending Memory and State proposals. The private vault initializer creates blank, generic runtime folders and starter files outside the public repo. The minimal local MCP server provides a narrow runtime boundary for selected session reads, allowlisted Memory/State reads, inert proposal creation, proposal review status, exact-approved-wording apply, and metadata-only private audit entries.

The server requires an explicit private-vault path outside the repository and exposes only its documented tools. Apply is never inferred from proposal creation or status: it requires a matching reviewed proposal, exact wording, destination-specific confirmation, an allowlisted target file, and State lifecycle triggers when applicable. The [local runtime viewer](docs/local-runtime-viewer.md) generates one static HTML file from an explicit private vault path, keeps Memory and State separate, and hides raw journal content by default. It adds no hosted dashboard, connector configuration, endpoint, tunnel, or public export. ChatGPT connector onboarding and a synthetic first-run flow are documented, but no live connector configuration or hosted deployment is included. The initializer does not access or write private content, and it does not add generated files to Git. Intake remains proposal-only; schema validation is not user approval. See the [local server guide](docs/mcp-local-server.md), [connector setup](docs/chatgpt-mcp-connector-setup.md), [first-run walkthrough](docs/first-run-chatgpt-walkthrough.md), [proposal approval workflow](docs/mcp-proposal-approval-workflow.md), [guided intake guide](docs/guided-intake.md), [v0.3.0 roadmap](docs/roadmap-v0.3.0.md), and [ADR 0003](docs/decisions/0003-journal-mirror-mcp-runtime.md).

Expanded MCP runtime regression tests now exercise whole-vault refusal, selected-context-only reads, no silent Memory/State writes, destination separation, exact approval gates, prompt-injection resistance, and metadata-only audit behavior. Run only with synthetic temporary fixtures and follow the [runtime validation checklist](docs/runtime-validation-checklist.md).

The public repository remains the control plane and includes no private vault data. The optional runtime uses a separate private data plane and is not a hosted service. It does not provide therapy or clinical care, and it never authorizes automatic persistence: proposal creation, review, exact-wording approval, and destination-specific apply remain distinct operations.

## Safety and Privacy Warnings

Do not commit filled journal entries, private notes, summaries, memory, state, exports, crisis notes, therapy notes, logs, databases, environment files, secrets, screenshots, local identifying paths, or identifying information.

Use synthetic examples only. If crisis indicators appear in actual use, stop ordinary reflection and prioritize immediate safety, trusted human support, emergency or crisis resources, and reducing access to harm.

## For Contributors

- Read `CONTRIBUTING.md` before opening issues or pull requests.
- Report sensitive-data exposure or safety issues using `SECURITY.md`.
- Run the synthetic manual checks described in `EVALS.md` after changing prompts, capabilities, guardrails, or proposal review behavior.
- Run `python -m unittest discover -s tests` and follow `docs/runtime-validation-checklist.md` after changing runtime boundaries.
- Run `python scripts/validate-json-schemas.py` after schema changes.

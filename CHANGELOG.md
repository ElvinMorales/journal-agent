# Changelog

All notable changes to this artifact system will be documented here.

## Unreleased

- Added the proposal review and exact-approved-wording apply workflow for the local MCP server.
- Added strict apply gates for matching reviewed proposal metadata, character-exact wording, destination-specific confirmation, and fixed Memory/State target allowlists.
- Added State review/stale and expiration trigger enforcement during approval and apply, append-only writes, cross-destination refusal, and double-apply prevention.
- Added metadata-only apply audit records with destination, filenames, timestamp, approved-wording hash, and character count but no full wording or proposal body.
- Added standard-library proposal approval/apply tests and a synthetic lifecycle walkthrough covering approve, reject, defer, expire, mismatch, trigger, separation, and repeat-apply boundaries.
- Added no ChatGPT connector setup, hosted endpoint, tunnel, local viewer, private data, configured private path, secret, or generated private-vault content.
- Added a minimal local Python MCP server using the official SDK interface and a standard-library private-vault policy layer.
- Added nine narrow tools for selected session context, approved Memory, current State, separate inert Memory/State proposals, proposal metadata/status, guarded apply refusal, and metadata-only private audit entries.
- Added explicit absolute private-vault configuration with missing, uninitialized, repository-root, inside-repository, traversal, wildcard, directory, allowlist, and read-size refusal checks.
- Added synthetic MCP server boundary tests covering allowed/denied paths, separate destinations, no silent Memory/State writes, trigger-bearing State proposals, metadata-only responses, and the original issue #30 disabled-apply boundary.
- Added local MCP server installation, operation, privacy, security, taxonomy, controller-contract, and roadmap documentation.
- Added no connector configuration, hosted endpoint, tunnel, viewer, full approval/apply workflow, private data, or configured local path.
- Added private vault runtime package documentation for a generic local notes structure outside the public repository.
- Added a Python standard-library private vault initializer with dry-run, idempotent default behavior, managed-starter `--force`, and resolved-path repository refusal checks.
- Added initializer tests for creation, dry-run, idempotency, force scope, unsafe path refusal, generic content, and separate Memory, State, and pending-proposal destinations.
- Updated setup, navigation, taxonomy, privacy, and security documentation for the initializer boundary.
- Added no MCP runtime, connector configuration, endpoint, hosted runtime, or local viewer implementation.
- Added a guided intake response schema for structured, reviewable, proposal-only output.
- Added an independently synthetic guided intake JSON example that validates against the new schema.
- Added a synthetic intake-to-Memory/State walkthrough covering approve, edit, move, discard, and expiration-trigger review decisions.
- Added guided intake boundary evals for jargon, skipping, sensitive overreach, clinical framing, approval confusion, Memory/State separation, State triggers, runtime claims, and prompt injection.
- Updated documentation and navigation for structured intake while keeping schema validation separate from user approval.
- Added no runtime implementation, MCP server, connector configuration, private-vault initializer, local viewer, endpoint, or automatic persistence.
- Added a manual guided intake prompt that asks plain-language questions about reflection use, tone, boundaries, supports, and temporary context.
- Added guided intake documentation for manual use, future MCP boundaries, and separate pending Memory and State proposals.
- Clarified that intake-originated proposals still require review of exact wording and destination, and that State requires a review/stale/expiration trigger.
- Added no runtime, MCP server, connector configuration, private-vault initializer, or automatic persistence as part of the guided intake prompt work.
- Added the `v0.3.0` MCP runtime and guided-intake roadmap.
- Added ADR 0003 for the proposed local/private Journal Mirror MCP runtime direction.
- Clarified `v0.2.0` as the current manual/control-plane release and `v0.3.0` as the MCP-connected private-runtime sprint.
- Added planning boundaries only; no MCP runtime, connector configuration, vault initializer, local viewer, endpoint, or executable implementation was added.
- Started `v0.2.0` planning for the Journal Mirror runtime pattern: natural private writing first, reflection after selection, and user-reviewed Memory or State proposals.
- Added a private Obsidian/private-notes runtime starter guide for manual setup, selected-context sessions, and reviewed Memory/State updates without a plugin or server.
- Added Journal Mirror prompts for selected-context sessions, freeform entries, recent pattern review, gentle next actions, and separate Memory/State proposal review.
- Added session and update-review capability modules, extended existing reflection capabilities, and added privacy-first trust metadata to journal skills.
- Updated navigation, workflow, runtime, taxonomy, output, roadmap, and backlog documentation for the manual prompt surfaces.
- Added separate Memory and State update proposal schemas, four synthetic lifecycle examples, and a manual review guide for approve, edit, discard, and expiration decisions.
- Clarified that proposal artifacts remain private and review-only, approved wording is copied manually, and no automatic persistence or State-to-Memory promotion is implemented.
- Added three public-safe synthetic Journal Mirror walkthroughs covering a freeform entry, a recent pattern review, and separate Memory/State proposal decisions.
- Added manual eval cases for template avoidance, evidence-bound reflection, Memory overreach, State staleness, required proposal fields, clinical scope, crisis routing, and selected-context privacy.
- Updated eval guidance, workflow and private-runtime docs, taxonomy mappings, roadmap, and backlog for the issue #15 walkthrough/eval layer without adding runtime automation.
- Added a design-only future MCP/VPS controller contract defining the private runtime edge, data classes, narrow allowed operations, denied operations, approval gates, audit expectations, failure mitigations, threat model, and pre-implementation checklist.
- Added synthetic manual future-controller boundary cases and linked the contract through architecture, workflow, lifecycle, proposal-review, privacy, security, taxonomy, roadmap, and navigation docs; no runtime implementation or private artifacts were added.
- Added `v0.2.0` release notes, a practical usable-product handoff, and a pre-release checklist.
- Tightened README and cross-repo navigation around manual private-first use, public/private boundaries, separate Memory and State review, and release readiness.
- Updated the artifact map, taxonomy mapping, roadmap, and backlog for the issue #17 handoff without adding a live runtime, vault access, automatic persistence, plugin, server, controller implementation, tag, or GitHub release.
- Added conservative cross-platform line-ending normalization through `.gitattributes` and ignored the local `.agents/` scratch workspace without adding its contents.

## v0.1.0 - 2026-05-31

### Added

- Reposition README as a public reference implementation of the Agentic AI Artifact Taxonomy.
- Add taxonomy mapping documentation across the 14 artifact buckets.
- Add public/private architecture documentation for journal content boundaries.
- Add decision record for keeping public artifacts separate from private journal content.
- Add v0.1.0 release checklist.
- Add GitHub Actions schema validation workflow.
- Add synthetic example audit documentation.

### Changed

- Clarify eval cases as synthetic/fictional examples.
- Rename memory example section to `Synthetic Shape Example`.

### Safety / Privacy

- Document public control-plane artifacts vs private user-owned journal content.
- Confirm public examples are synthetic-only or blank templates.
- Keep real journal entries, summaries, memory, state, exports, logs, therapy notes, crisis notes, screenshots, databases, secrets, and identifying details outside the repo.

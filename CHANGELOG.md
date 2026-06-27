# Changelog

All notable changes to this artifact system will be documented here.

## Unreleased

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

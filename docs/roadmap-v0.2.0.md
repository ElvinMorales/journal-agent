# Roadmap: v0.2.0

Status: Draft planning note

## Release Thesis

`v0.2.0` establishes a usable Journal Mirror Agent scaffold. Natural writing happens first in a private notes system; the agent reflects only on context the user selects; any Memory or State changes are proposed for review before application.

This release is a foundation, not the end of the sprint. It should make the direction inspectable and give later issues stable workflow, privacy, taxonomy, and approval boundaries.

## Must-Have Scope

- Reframe the primary path as `write naturally → select context → mirror after → review updates`.
- Document the Journal Mirror session workflow, inputs, outputs, and non-clinical boundaries.
- Define the public repository as the reusable control plane and a private Obsidian vault or private notes system as the runtime/data plane.
- Keep Memory and State separate and require a proposal plus user review before either changes.
- Position journal templates as optional helpers rather than required structure.
- Preserve the canonical 14-bucket taxonomy and document Strategic Mirror as a working pattern only.
- Keep all examples synthetic and the repository public-safe.

## Implementation Progress

- Covered by issue #12: a manual private Obsidian/private-notes runtime starter guide, with no plugin, server, or vault automation.
- Covered by issues #13 and #6: practical selected-context session prompts, capability modules, and privacy-first trust metadata for journal skills.
- Covered by issue #14: separate reviewable Memory and State proposal schemas, synthetic lifecycle examples, and manual review guidance without persistence automation.
- Remaining sprint work: synthetic walkthroughs and safety evals, future controller-contract documentation, and release readiness.

## Maybe-Later Scope

- Synthetic walkthroughs, expanded evals, and release notes.
- A future controller contract for MCP or VPS-based private runtimes.
- Optional setup helpers that do not read or move private journal content.

## Explicit Non-Goals

- No MCP server.
- No hosted runtime.
- No Obsidian plugin.
- No private journal content.
- No live Memory or State writes.
- No therapy, diagnosis, treatment planning, or medication guidance.
- No full repo rewrite.

## Public/Private Safety Notes

The public repository contains reusable design-time artifacts: instructions, policies, prompts, templates, schemas, decisions, synthetic examples, and validation. It must not contain raw entries, selected excerpts, generated private reflections, pending proposals from real sessions, filled Memory, live State, local paths, credentials, logs, or private vault files.

The private notes system is user-controlled. Selection is explicit and minimal. A Journal Mirror session does not grant broad access to a vault, and a proposal is not permission to persist data. Users review each proposed destination and can approve, edit, or discard it.

The agent remains a reflection companion, not a clinical product or care provider. Existing crisis and safety guardrails continue to take precedence over ordinary reflection.

## Validation Checklist

- [ ] README presents natural private writing as the primary starting point.
- [ ] The Journal Mirror workflow and ADR agree on sequencing and approval gates.
- [ ] Templates are described as optional.
- [ ] Memory and State remain separate.
- [ ] The original 14 taxonomy buckets remain intact.
- [ ] Strategic Mirror is identified only as a working implementation pattern.
- [ ] No private runtime artifacts, identifying data, secrets, or local paths are added.
- [ ] No MCP server, hosted runtime, or Obsidian plugin is implemented.
- [x] A private Obsidian/private-notes runtime guide documents manual setup without adding private runtime artifacts.
- [x] Selected-context Journal Mirror prompts and capability surfaces support manual sessions without template-first writing.
- [x] Journal skills declare privacy-first trust metadata and proposal-only persistence boundaries.
- [x] Separate Memory and State proposal schemas, synthetic examples, and manual review guidance keep updates review-only.
- [ ] `git diff --check` passes.
- [ ] `python scripts/validate-json-schemas.py` passes.
- [ ] `git ls-files private` contains placeholders only.

## Follow-Up Issue Candidates

- Add synthetic end-to-end walkthroughs and safety evals.
- Specify a future MCP/VPS controller contract without implementation.
- Complete `v0.2.0` release-readiness and navigation review.

Do not treat the completed prompt surfaces as completion of the full v0.2 release.

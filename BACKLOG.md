# Backlog

## v0.3 MCP Runtime and Guided Intake — Issue #25

- [x] Issue #26: establish the `v0.3.0` roadmap and proposed MCP runtime architecture in a focused docs-only planning PR.
- [x] Issue #27: design guided intake and initial Memory/State proposal behavior in a focused prompt/docs change; no runtime or persistence implementation included.
- [ ] Issue #28: define the structured intake schema, synthetic examples, and deeper eval coverage.
- [ ] Build the private-vault runtime package and initializer.
- [ ] Build a minimal local MCP server.
- [ ] Implement proposal approval and exact-wording apply through MCP.
- [ ] Document ChatGPT connector setup and a first-run walkthrough.
- [ ] Add an optional local HTML viewer.
- [ ] Add MCP runtime tests and safety evals.
- [ ] Complete `v0.3.0` release readiness.

Issues #26 and #27 record architecture and intake design only. No runtime implementation is included; issue #28 and the remaining issue #25 child work stay separately scoped and reviewable.

## v0.2 Follow-Up Sprint Areas

- [x] Document a private Obsidian or private-notes runtime guide without adding private vault content.
- [x] Add Journal Mirror session prompts and capability modules for selected entries, excerpts, and small groups of entries.
- [x] Add privacy-first trust metadata to journal skills.
- [x] Define separate reviewable Memory and State proposal schemas, synthetic lifecycle examples, and manual review guidance without automatic persistence.
- [x] Add synthetic walkthroughs and evals for the post-writing mirror flow and safety boundaries.
- [x] Define a future MCP/VPS controller contract as a public-safe, design-only interface specification with synthetic boundary evals and no runtime implementation.
- [x] Address issue #17 with `v0.2.0` release notes, a usable-product handoff, a pre-release checklist, navigation updates, and public-safety review. Release-candidate readiness still depends on this PR merging and final validation.
- [x] Address issue #5 with conservative cross-platform line-ending normalization and an ignore rule for the local `.agents/` scratch workspace.

## Later

- Consider model/runtime integration only after the manual, file-first workflow and approval boundaries are validated.
- Add consent UI or command flow for Memory and State writes only after proposal review behavior is specified and evaluated.
- Add schema validation to a GitHub Actions workflow after local validation is stable.
- Add contribution and security docs if the repository becomes collaborative.
- Add clinically reviewed safety examples if this moves beyond personal use.
- Add export packaging for therapist handoff.
- Consider future controller implementation planning only as a separately scoped and approved effort.
- Add more examples and evals after private use only as independently synthetic or deliberately redacted public artifacts.
- Create the `v0.2.0` tag and GitHub release after merge and final validation, if desired.

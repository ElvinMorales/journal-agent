# Backlog

## v0.3 MCP Runtime and Guided Intake — Issue #25

- [x] Issue #26: establish the `v0.3.0` roadmap and proposed MCP runtime architecture in a focused docs-only planning PR.
- [x] Issue #27: design guided intake and initial Memory/State proposal behavior in a focused prompt/docs change; no runtime or persistence implementation included.
- [x] Issue #28: add the structured intake schema, synthetic examples, intake-to-proposal walkthrough, and deeper boundary eval coverage; no runtime or persistence implementation included.
- [x] Issue #29: build the private-vault runtime package and initializer.
- [x] Issue #30: build a minimal local MCP server with explicit private-vault configuration, narrow tools, inert proposals, metadata-only audit, and synthetic boundary tests.
- [x] Issue #31: implement proposal approval and exact-wording apply through MCP with destination-specific confirmation, fixed target allowlists, State triggers, append-only writes, double-apply refusal, and metadata-only audit.
- [x] Issue #32: document ChatGPT connector setup, tool review/permissions, a synthetic first-run walkthrough, refusal checks, and disconnect guidance without adding live connectivity.
- [x] Issue #33: add an optional local static HTML viewer for Journal Mirror runtime state with private-path refusal, metadata-only defaults, and synthetic tests.
- [x] Issue #34: expand MCP runtime tests and safety evals with integrated regressions, prompt-injection and clinical/safety matrices, intake cases, and local validation guidance.
- [ ] Issue #35: complete `v0.3.0` release readiness.

Issues #26 through #34 cover architecture, intake design, structured intake artifacts, the private-vault package, the minimal local MCP server, exact-approved-wording apply, ChatGPT connector onboarding, local runtime inspection, and expanded safety validation. Issue #35 is the next likely work: final `v0.3.0` release readiness. Parent sprint #25 remains open until that work is complete.

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

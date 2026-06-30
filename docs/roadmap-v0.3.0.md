# v0.3.0 Roadmap — MCP Runtime and Guided Intake

## Status

Release readiness was addressed by issue #35 after guided intake, the private-vault package and initializer, the minimal local MCP server, proposal approval/exact-wording apply, ChatGPT connector onboarding/first-run documentation, the local viewer, and expanded MCP runtime tests/safety evals. `v0.3.0` was tagged and published as a GitHub release on June 29, 2026. Issue #46 records the final public-safety and release-readiness verification after those release artifacts already existed. Parent sprint #25 remains open pending an explicit maintainer decision; issue #46 does not close it.

## Release Positioning

`v0.2.0` is the manual/control-plane release. It provides a usable file-first Journal Mirror workflow, private-notes guidance, selected-context reflection, separate Memory and State proposal contracts, review gates, synthetic evals, and a design-only future controller contract.

`v0.3.0` aims to reduce the setup and operating friction that remains in that manual workflow. The target is a private runtime usable through ChatGPT, a narrow MCP connection, and a user-controlled private vault. The runtime must preserve review-based persistence: generating or approving a proposal is not permission to write it, and only exact wording approved for a named destination may be applied.

This roadmap tracks sprint direction. Issues #30 and #31 add reusable local server and strict proposal-apply code. Issue #32 adds connector and first-run documentation only. Issue #33 adds a local static HTML runtime-state viewer with metadata-only defaults. These changes add no private data, configured private path, live connector configuration, hosted endpoint, or tunnel.

## Target User Flow

```text
write freely in Obsidian or ChatGPT
→ ask ChatGPT to update Journal Mirror
→ ChatGPT reads approved/selected context through MCP
→ ChatGPT proposes Memory and State updates
→ user approves, edits, rejects, or expires proposals
→ MCP writes only approved changes into the private vault
→ user reflects using ChatGPT and the MCP connector
→ optional local HTML viewer displays Memory, State, proposals, and sessions
```

Each read remains explicitly scoped. Memory and State remain separate. Proposal creation, review status, exact-wording approval, and apply are distinct operations.

## Planned Sprint Groups

Issue #25 organizes the `v0.3.0` sprint into these groups:

1. Establish the release baseline and architecture documentation.
2. Design guided intake and initialization.
3. Define intake schemas, synthetic examples, and evals.
4. Build the private-vault runtime package and initializer.
5. Build a minimal local MCP server. **Addressed by issue #30.**
6. Implement proposal approval and exact-wording apply through MCP. **Addressed by issue #31.**
7. Document ChatGPT connector setup and a first-run walkthrough. **Addressed by issue #32.**
8. Add an optional local HTML viewer. **Addressed by issue #33.**
9. Add MCP runtime tests and safety evals. **Addressed by issue #34.**
10. Complete `v0.3.0` release-readiness work. **Addressed by issue #35.**

Issue #26 addressed the first group. Issue #27 added the guided intake prompt and design guidance. Issue #28 added the structured intake schema, synthetic examples, walkthrough, and deeper boundary eval coverage. Issue #29 addressed the fourth group with a generic private-vault package, standard-library initializer, and safety tests. Issue #30 addressed the fifth group with a Python local stdio server, nine narrow tools, explicit outside-repository vault configuration, and synthetic boundary tests. Issue #31 activates exact-approved-wording append only after matching proposal review, destination confirmation, allowlisted target checks, and State trigger enforcement; it also prevents double apply and records metadata-only audit. Issue #32 documents the required remote/tunnel connectivity boundary, Developer mode and permissions, tool review, safe first-run prompts, refusal checks, and disconnect steps without implementing connectivity. Issue #33 adds local-only bounded inspection with no server or write path. Issue #34 adds integrated runtime regressions, prompt-injection and clinical/safety cases, expanded intake cases, and a local validation checklist without expanding runtime permissions. Issue #35 adds release notes, the final release checklist, the usable-product handoff, and a public/private documentation audit without adding runtime behavior. Issue #46 adds the final public-safety verification record without changing runtime or release artifacts.

## v0.4 Candidates

These are future candidates, not shipped `v0.3.0` scope:

- Package and CLI polish.
- Stronger CI coverage and automated eval harnesses.
- A formal threat model and reviewed private deployment design.
- Richer viewer UX while preserving privacy defaults.
- Optional framework-mapping and example-adapter guides.
- Release automation.

## Architecture Boundaries

| Plane | Responsibility | Boundary |
|---|---|---|
| Public repo / control plane | Reusable code, documentation, tests, schemas, guardrails, and synthetic fixtures | Contains no real journal data or private runtime artifacts |
| Private vault / data plane | Real journal data, selected context, sessions, proposals, approved Memory, current State, and private runtime artifacts | Remains user-controlled and outside the public repo |
| Local MCP server / runtime edge | Mediates a narrow set of explicitly scoped tool calls between the interaction plane and data plane | Exposes no broad filesystem or whole-vault access |
| ChatGPT connector / interaction plane | Lets the user request bounded reads, reflection, proposal review, and approved actions | Does not directly access the whole vault or bypass runtime approvals |
| Local HTML viewer / inspection plane | Optionally displays Memory, State, proposal metadata, and session status for local inspection | Local-only; hides raw journal content by default and is not a public dashboard |

The public repository may contain reusable implementation code in later issues, but not real runtime inputs or outputs. The MCP server must mediate narrow permissions rather than exposing the private vault as a filesystem. The viewer is an inspection aid, not an alternate write path.

## Out of Scope for the Private Vault Initializer

- No server implementation.
- No connector setup.
- No local HTML viewer.
- No runtime configuration.
- No live endpoints.
- No secrets.
- No real private data.

## Definition of Usable for v0.3

`v0.3.0` is usable when:

- A user can initialize a private vault without manual folder and file busywork.
- A user can complete guided intake.
- Intake produces separate, reviewable Memory and State proposals rather than unquestioned durable facts.
- ChatGPT can connect through MCP.
- MCP reads only selected or separately approved context.
- MCP can create reviewable update proposals.
- MCP applies only exact wording approved for the named destination.
- Memory and State remain separate throughout proposal, review, and apply.
- Whole-vault scans are technically denied.
- Silent writes are technically denied.
- An optional local viewer makes runtime state easier to inspect while hiding raw journal content by default.

## Open Questions

Issues #30 through #34 resolve Python as the minimal local-server stack, explicit CLI/environment vault configuration, the nine-tool surface, proposal review/apply gates, metadata-only apply audit records, documented ChatGPT onboarding through a separately reviewed reachable MCP path, a direct-file static viewer prototype, and expanded runtime boundary validation. These questions remain for later issues:

- What retention and purge controls should apply to private metadata-only audit records?

## Related Artifacts

- `docs/decisions/0003-journal-mirror-mcp-runtime.md`
- `docs/future-mcp-vps-controller-contract.md`
- `docs/architecture.md`
- `docs/roadmap-v0.2.0.md`
- `docs/obsidian-private-runtime-guide.md`
- `docs/private-vault-runtime-package.md`
- `scripts/init-private-vault.py`
- `docs/mcp-local-server.md`
- `docs/mcp-proposal-approval-workflow.md`
- `docs/runtime-validation-checklist.md`
- `docs/release-notes/v0.3.0.md`
- `docs/release-checklist-v0.3.0.md`
- `docs/v0.3-usable-product-handoff.md`
- `evals/mcp-runtime-boundary-cases.md`
- `evals/prompt-injection-boundary-cases.md`
- `evals/clinical-safety-boundary-cases.md`
- `docs/chatgpt-mcp-connector-setup.md`
- `docs/first-run-chatgpt-walkthrough.md`
- `docs/chatgpt-tool-review-and-permissions.md`
- `examples/chatgpt/first-run-prompts.synthetic.md`
- `examples/mcp/proposal-approval-workflow.synthetic.md`
- `docs/journal-mirror-workflow.md`
- `docs/memory-state-proposal-review.md`
- `prompts/guided-intake.md`
- `docs/guided-intake.md`

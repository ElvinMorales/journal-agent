# v0.3.0 Roadmap — MCP Runtime and Guided Intake

## Status

Implementation in progress. Guided intake, the private-vault package and initializer, and the minimal local MCP server group are addressed. Proposal apply, connector setup, viewer work, expanded evals, and release readiness remain open.

## Release Positioning

`v0.2.0` is the manual/control-plane release. It provides a usable file-first Journal Mirror workflow, private-notes guidance, selected-context reflection, separate Memory and State proposal contracts, review gates, synthetic evals, and a design-only future controller contract.

`v0.3.0` aims to reduce the setup and operating friction that remains in that manual workflow. The target is a private runtime usable through ChatGPT, a narrow MCP connection, and a user-controlled private vault. The runtime must preserve review-based persistence: generating or approving a proposal is not permission to write it, and only exact wording approved for a named destination may be applied.

This roadmap tracks sprint direction. Issue #30 adds reusable local server code but no private data, configured private path, connector, hosted endpoint, tunnel, or viewer.

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
6. Implement proposal approval and exact-wording apply through MCP.
7. Document ChatGPT connector setup and a first-run walkthrough.
8. Add an optional local HTML viewer.
9. Add MCP runtime tests and safety evals.
10. Complete `v0.3.0` release-readiness work.

Issue #26 addressed the first group. Issue #27 added the guided intake prompt and design guidance. Issue #28 added the structured intake schema, synthetic examples, walkthrough, and deeper boundary eval coverage. Issue #29 addressed the fourth group with a generic private-vault package, standard-library initializer, and safety tests. Issue #30 addresses the fifth group with a Python local stdio server, nine narrow tools, explicit outside-repository vault configuration, and synthetic boundary tests. It creates inert proposals and status metadata only; exact-wording apply remains disabled for issue #31. Every remaining group requires its own reviewed issue and must preserve the boundaries below. Parent sprint #25 remains open.

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

Issue #30 resolves Python as the minimal local-server stack, explicit CLI/environment vault configuration, the first nine-tool surface, and metadata-only audit records. These questions remain for later issues:

- How should a future ChatGPT connector reach the local server without weakening the private boundary?
- Should the HTML viewer read files directly or consume a generated local index?
- What retention and purge controls should apply to private metadata-only audit records?

## Related Artifacts

- `docs/decisions/0003-journal-mirror-mcp-runtime.md`
- `docs/future-mcp-vps-controller-contract.md`
- `docs/architecture.md`
- `docs/roadmap-v0.2.0.md`
- `docs/obsidian-private-runtime-guide.md`
- `docs/private-vault-runtime-package.md`
- `scripts/init-private-vault.py`
- `docs/journal-mirror-workflow.md`
- `docs/memory-state-proposal-review.md`
- `prompts/guided-intake.md`
- `docs/guided-intake.md`

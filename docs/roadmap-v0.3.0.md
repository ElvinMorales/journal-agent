# v0.3.0 Roadmap — MCP Runtime and Guided Intake

## Status

Implementation in progress. Guided intake is manually usable, and the private-vault package and initializer are addressed. MCP runtime implementation has not started.

## Release Positioning

`v0.2.0` is the manual/control-plane release. It provides a usable file-first Journal Mirror workflow, private-notes guidance, selected-context reflection, separate Memory and State proposal contracts, review gates, synthetic evals, and a design-only future controller contract.

`v0.3.0` aims to reduce the setup and operating friction that remains in that manual workflow. The target is a private runtime usable through ChatGPT, a narrow MCP connection, and a user-controlled private vault. The runtime must preserve review-based persistence: generating or approving a proposal is not permission to write it, and only exact wording approved for a named destination may be applied.

This roadmap establishes sprint direction. It adds no executable runtime or private data access.

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
5. Build a minimal local MCP server.
6. Implement proposal approval and exact-wording apply through MCP.
7. Document ChatGPT connector setup and a first-run walkthrough.
8. Add an optional local HTML viewer.
9. Add MCP runtime tests and safety evals.
10. Complete `v0.3.0` release-readiness work.

Issue #26 addressed the first group. Issue #27 added the guided intake prompt and design guidance. Issue #28 added the structured intake schema, synthetic examples, walkthrough, and deeper boundary eval coverage. Issue #29 addresses the fourth group with a generic private-vault package, standard-library initializer, and safety tests; it does not implement MCP or private data access. Every remaining runtime implementation group requires its own reviewed issue and must preserve the boundaries below.

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

These questions remain undecided and belong in later design or implementation issues:

- Should `v0.3.0` use Node/TypeScript, Python, or another MCP server stack?
- Should ChatGPT connector setup assume a tunnel during development?
- How should local paths be configured without committing them?
- What is the minimum safe first MCP tool set?
- Should the HTML viewer read files directly or consume a generated local index?
- What logging is useful without copying private content?

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

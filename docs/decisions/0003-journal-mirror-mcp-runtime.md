# 0003 — Journal Mirror MCP Runtime Direction

## Status

Proposed

## Context

`v0.2.0` established the manual Journal Mirror control plane: natural writing, explicit context selection, tentative reflection, separate Memory and State proposals, and review before manual persistence. It intentionally did not implement a runtime connection to a private vault.

Issue #25 makes reducing that manual setup and transfer friction the next sprint. A future ChatGPT integration needs a private runtime edge that can expose useful operations without turning the vault into broadly accessible model context or weakening proposal review. The existing public-repo/control-plane and private-vault/data-plane split remains mandatory.

## Decision

`v0.3.0` will pursue a local/private MCP runtime edge. The runtime will preserve these distinct planes:

- The public repo is the reusable control plane.
- The private vault is the user-controlled data plane.
- The local MCP server is the narrow runtime edge.
- The ChatGPT connector is the interaction plane.
- The optional local HTML viewer is the inspection plane.

The MCP runtime will expose narrow, named tools rather than broad filesystem access. ChatGPT will receive only the context selected or separately approved for a bounded operation; it will not receive direct whole-vault access.

Guided intake will initialize reviewable Memory and State proposals, not unquestioned durable facts. Intake output must use separate destinations and remain pending until the user approves, edits, rejects, or expires it. Applying a proposal will require a separate confirmation and must preserve the exact approved wording.

The local HTML viewer is planned as a local inspection aid for Memory, State, proposals, and sessions. It is not a public dashboard, a substitute write path, or authorization to reveal raw journal content by default.

Implementation is intentionally deferred to later issues. This decision adds no MCP server, connector configuration, vault initializer, viewer, endpoint, runtime configuration, or tool handler.

### Initial Proposed MCP Tool Categories

These categories define planning boundaries, not final tool names or code:

- Selected-context reads.
- Approved Memory reads.
- Current State reads.
- Pending Memory proposal creation.
- Pending State proposal creation.
- Proposal metadata listing.
- Proposal status updates.
- Exact approved wording apply.
- Metadata-only audit logging.

### Denied Operation Categories

- Whole-vault scan.
- Broad search without explicit scope.
- Silent Memory writes.
- Silent State writes.
- State-to-Memory promotion.
- Raw journal copy into Memory.
- Full entry copy into State.
- Background monitoring.
- Public export without review.
- Clinical diagnosis, treatment, or scoring.

## Consequences

- Later runtime work has a clear least-privilege architecture and can be reviewed in focused increments.
- User selection, proposal review, destination approval, and exact-wording apply remain separate gates.
- Memory and State stay distinct in guided intake and normal operation.
- A local runtime and viewer add packaging, authorization, configuration, testing, and maintenance work that `v0.2.0` did not require.
- Connector and transport choices remain open until later issues resolve them.
- The manual `v0.2.0` workflow remains usable while runtime work proceeds.

## Alternatives Considered

### Continue With Manual Transfer Only

Retained as a supported fallback, but rejected as the sole `v0.3.0` direction because it leaves setup and repeated context-transfer friction unresolved.

### Give ChatGPT Broad Vault or Filesystem Access

Rejected. Broad access conflicts with explicit selection, least privilege, data minimization, and the existing controller contract.

### Persist Guided Intake Directly

Rejected. Intake is incomplete and user-correctable context; it must produce proposals rather than durable facts without review.

### Host a Public Dashboard

Rejected. The planned viewer is local-only and exists for inspection, not publication or remote access.

### Implement the Runtime in This PR

Rejected. Architecture and sprint boundaries require review before stack, transport, configuration, and tool-handler decisions are made.

## Safety and Privacy Notes

- Real entries, selected context, proposals, Memory, State, sessions, logs, and runtime configuration remain private.
- Journal text is untrusted data and cannot expand tool scope or change approval policy.
- Audit logging is metadata-only and must not become a second journal copy.
- Whole-vault scans, silent writes, background monitoring, and unreviewed public export remain denied.
- The runtime remains a journal companion boundary, not a diagnostic, treatment, medication, clinical-scoring, or crisis-automation system.
- Existing safety routing in `AGENTS.md` and `GUARDRAILS.md` continues to take precedence over ordinary reflection.

## Related Artifacts

- `docs/roadmap-v0.3.0.md`
- `docs/future-mcp-vps-controller-contract.md`
- `docs/architecture.md`
- `docs/decisions/0001-public-artifacts-private-journal.md`
- `docs/decisions/0002-journal-mirror-runtime-pattern.md`
- `docs/journal-mirror-workflow.md`
- `docs/memory-state-proposal-review.md`
- `schemas/memory-update-proposal.schema.json`
- `schemas/state-update-proposal.schema.json`

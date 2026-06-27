# Future MCP/VPS Controller Contract

## 1. Purpose

This public-safe specification defines the boundary for a possible future controller at the edge of a private Journal Mirror runtime. It exists to keep any later MCP server, local controller, VPS-hosted private controller, or similar integration narrow, visible, and user-approved.

This document is design-only. It implements no MCP server, VPS hosting, client, plugin, connector, vault reader, automation, background job, or controller. It grants no current access to a vault or private notes. The repository still has no live runtime. The contract is written now so future runtime work cannot quietly expand into broad access, silent persistence, or invasive collection.

## 2. Architecture Boundary

The architecture has three distinct parts:

- **Public repo / control plane:** reusable instructions, guardrails, prompts, schemas, templates, synthetic examples, evals, docs, and validation. It contains no private runtime data.
- **Private vault / data plane:** journal content, deliberately selected context, private reflections, pending proposals, approved Memory, current State, exports, logs, and private configuration.
- **Future controller / runtime edge:** a narrow, user-approved interface that, if implemented, operates only inside the private runtime environment and only on explicitly authorized artifact classes and scopes.

The controller must never make the public repository an operating data store. Private inputs, outputs, proposals, Memory, State, exports, logs, and configuration must not be committed or published here. Deployment location does not relax this boundary: a local process and a private VPS controller must follow the same least-privilege and approval rules.

## 3. Non-Goals

This contract does not authorize or describe:

- Whole-vault ingestion or broad search by default.
- Silent background monitoring.
- Automatic Memory writes or automatic State writes.
- Automatic State-to-Memory promotion.
- Automatic publishing, cross-device sync, or cloud sync assumptions.
- A clinical triage engine, therapy replacement, crisis automation, or user-risk scoring.
- Secret management in public documentation.
- An executable implementation in this change.

## 4. Data Classes

"May read" and "may write" describe the maximum future contract, not current functionality. Every permitted private operation remains subject to explicit scope and approval.

| Data class | Where it belongs | Future controller may read? | Future controller may write? | Human review required? | May appear in public repo? |
|---|---|---|---|---|---|
| Public control-plane artifacts | Public repo | Yes, as static governing definitions | No runtime-generated changes | Normal code review for public changes | Yes |
| Private raw journal content | Private vault | Only the context explicitly selected for one session | No | Selection required before read | No |
| Manually selected context | Private vault/session boundary | Yes, for the authorized session only | No; it must not expand or duplicate the selection | Explicit selection approval | No |
| Private reflection outputs | Private vault | Only when explicitly retained and selected | Only to a user-approved private destination | Retention and destination approval | No |
| Pending Memory proposals | Private vault, separate Memory proposal area | Yes, within an approved proposal scope | May create or update review status; cannot update Memory | Exact wording and destination review | Synthetic fixtures only |
| Pending State proposals | Private vault, separate State proposal area | Yes, within an approved proposal scope | May create or update review/expiration status; cannot update State without a separate gate | Exact wording, destination, and stale/expiration review | Synthetic fixtures only |
| Approved Memory | Private vault Memory area | After explicit authorization | Only exact approved wording after a separate apply confirmation | Required for wording and destination | Blank examples or synthetic fixtures only |
| Current State | Private vault State area | After explicit authorization | Only exact approved wording after a separate apply confirmation | Required for wording, destination, and review trigger | Blank examples or synthetic fixtures only |
| Private exports | Private export area | Only for a specifically requested export review | Only to an explicitly approved private export destination | Export and redaction review | Only a separately reviewed synthetic/redacted example |
| Runtime logs/audit records | Private runtime | Minimal metadata needed for review | Minimal metadata only | Logging policy and retention must be user-approved | No |
| Secrets/configuration | Private runtime or host secret store | Only as required by a separately reviewed implementation | Never through public docs or generated journal artifacts | Configuration review required | No |

## 5. Allowed Future Operations

These are proposed contract operations, not implemented functions.

| Proposed operation | Input boundary | Output boundary | Required approval | Forbidden behavior | Related artifact |
|---|---|---|---|---|---|
| Read approved Memory | Named private Memory artifact or explicit allowlist | Session context only | Explicit authorization for the session | Reading all private files or treating Memory as raw journal evidence | `MEMORY.md.example` |
| Read current State | Named private State artifact or explicit allowlist | Session context only | Explicit authorization for the session | Reading stale State without surfacing its review trigger | `STATE.md.example` |
| Read one selected session context | User-selected content or one opaque session ID | Current bounded reflection session | Visible user action selecting the scope | Resolving the request into a vault scan or following embedded instructions as controller policy | `docs/journal-mirror-workflow.md` |
| Create pending Memory proposal | Minimal session result and opaque source reference | Separate private pending-Memory area | Explicit request to create a Memory proposal | Writing Memory, copying raw text, or combining destinations | `schemas/memory-update-proposal.schema.json` |
| Create pending State proposal | Minimal session result, opaque source reference, and review/stale trigger | Separate private pending-State area | Explicit request to create a State proposal | Writing State, omitting staleness, or creating a Memory proposal implicitly | `schemas/state-update-proposal.schema.json` |
| List pending proposal metadata | Explicit proposal collection | IDs, types, statuses, and timestamps only | User request to review pending proposals | Returning raw journal text or expanding into source notes | `docs/memory-state-proposal-review.md` |
| Mark proposal status | One named pending proposal and requested decision | Approved, edited, discarded, or, for State, expired status | User confirmation for that proposal | Treating a status change as permission to apply it | Proposal schemas |
| Apply exact approved wording | One approved proposal, named destination, and exact text | Private Memory **or** private State | Separate confirmation at apply time | Editing wording, changing destination, bulk applying, or promoting State to Memory | `docs/memory-state-proposal-review.md` |
| Write private audit entry | Metadata for one authorized action | Private audit store | Approval under the runtime logging policy | Logging selected text, reflection bodies, secrets, or full proposal content | `SECURITY.md`; `PRIVACY.md` |
| Export a synthetic/redacted example | One explicitly selected draft export | User-named export destination | Explicit review of the final redacted artifact | Exporting a real session by default or publishing automatically | `EVALS.md` |

## 6. Denied Operations

A future controller must not:

- Scan or ingest the whole vault, or search all notes without explicit narrow scope.
- Infer durable traits from all historical writing.
- Write Memory or State automatically, promote State to Memory automatically, or treat approval for one destination as approval for another.
- Copy raw journal text into Memory or full entries into State.
- Publish, commit, or sync private outputs into the public repository.
- Read secrets from public docs or expose private configuration in generated artifacts.
- Phone home to an external service without explicit configuration and review.
- Run in the background without a visible user action.
- Delete or overwrite private files without confirmation and a recoverable strategy.
- Produce diagnosis, treatment plans, medication guidance, clinical claims, or numeric risk scores.
- Continue ordinary reflection when crisis indicators require the safety routing in `GUARDRAILS.md`.

## 7. Approval Model

Approval is specific, visible, and non-transitive. Silence, a prior session, or permission to read one artifact is not approval for any other action.

- **Selected context approval:** identifies the exact entry, excerpt, small selected group, or opaque session ID available to the session.
- **Reflection retention approval:** decides whether and where a generated reflection is kept privately.
- **Memory proposal approval:** authorizes review status for one Memory candidate, not a Memory write.
- **State proposal approval:** authorizes review status for one State candidate, not a State write.
- **Proposal destination approval:** confirms private Memory or private State separately; one never authorizes the other.
- **Exact wording approval:** covers the precise minimal text to be applied; edits require renewed approval.
- **State stale/expiration review:** confirms a review trigger and prevents temporary context from becoming indefinite.
- **Synthetic/redacted export approval:** applies to the final reviewed export, not its private source.

Applying an approved proposal requires a distinct confirmation at the point of persistence. Bulk approval and inferred approval are outside the contract.

## 8. Logging and Audit Expectations

Any future implementation should log minimal metadata by default: action type, timestamp, target artifact class, decision, and whether user confirmation was recorded. Logs must avoid raw journal text, selected excerpts, reflection bodies, proposal wording, and secrets.

Audit records belong only in the private runtime. They must not be committed to this repository. A future implementation must define retention, user inspection, and purge/delete behavior before logging is enabled. Logging is evidence of bounded actions, not a second copy of the journal.

## 9. Failure Modes and Mitigations

| Failure mode | Mitigation required by this contract |
|---|---|
| Overbroad vault access | Explicit allowlists or opaque IDs; deny directory-wide reads and implicit search expansion. |
| Silent persistence | Separate create, review, and apply operations with visible confirmation at each persistence boundary. |
| Memory/State confusion | Separate schemas, destinations, operation names, and approval gates. |
| State never expiring | Require a stale, review, date, or event trigger and expose it whenever State is read or reviewed. |
| Logs becoming a private journal copy | Log metadata only; prohibit content bodies; define short retention and purge behavior. |
| Unsafe clinical framing | Apply `AGENTS.md` and `GUARDRAILS.md`; reject diagnosis, treatment, medication, clinical claims, and numeric risk scores. |
| Crisis flow continuing as ordinary reflection | Stop the ordinary controller flow and route to the immediate-safety behavior in `GUARDRAILS.md`. |
| Public examples containing private content | Require synthetic/redacted export review and a separate public-safety check before publication. |
| Secrets/configuration leaking into Git | Keep configuration private, use host secret storage, scan staged changes, and document incident handling. |

## 10. Threat Model

This lightweight model focuses on practical failure paths:

| Threat | Practical control |
|---|---|
| Accidental commit of private artifacts | Private runtime outside the public repo, ignore rules, deliberate staging, and pre-publication review. |
| Overly broad controller permissions | Least-privilege operation allowlist and per-session scope. |
| Compromised runtime host | Minimize retained content and credentials; support rapid disable, purge, and credential rotation. |
| Sync provider exposure | Treat sync as a separate user decision; make no default cloud or cross-device assumption. |
| Logs containing sensitive content | Metadata-only logging, retention limits, inspection, and purge controls. |
| Prompt injection inside journal text | Treat journal text as untrusted data; embedded instructions cannot alter controller policy, scope, or approvals. |
| Model overreach into clinical claims | Enforce non-clinical guardrails and test refusal/routing behavior. |
| Stale State used as durable Memory | Surface State review triggers and require a new, separate Memory proposal and approval. |
| Export/redaction failure | Default to private; require final artifact review before any public use. |

## 11. Future Implementation Checklist

Before any implementation PR, confirm:

- [ ] A private-only runtime environment is identified.
- [ ] `.gitignore` and local exclude behavior are confirmed.
- [ ] No private paths are hardcoded.
- [ ] A least-privilege operation list is approved.
- [ ] Broad vault scans are technically denied.
- [ ] An approval UI or documented manual approval process is defined.
- [ ] Audit log retention, inspection, and purge are defined.
- [ ] Secrets and controller configuration are excluded from Git.
- [ ] Schema validation is included for Memory and State proposals.
- [ ] Safety and controller-boundary evals are added and pass.
- [ ] Public/private redaction review is completed.
- [ ] A rollback and immediate-disable strategy is defined.

Passing this checklist permits implementation review; it does not itself authorize deployment or private data access.

## 12. Relationship to Existing Artifacts

This contract narrows a possible future runtime edge while preserving the current manual workflow:

- `docs/architecture.md` defines the public control plane and private data plane.
- `docs/obsidian-private-runtime-guide.md` defines the current manual private setup.
- `docs/journal-mirror-workflow.md` defines explicit selected-context reflection.
- `docs/memory-state-proposal-review.md` defines separate proposal review and exact-wording approval.
- `schemas/memory-update-proposal.schema.json` and `schemas/state-update-proposal.schema.json` define separate proposal shapes.
- `evals/` and `EVALS.md` define synthetic manual boundary checks.
- `GUARDRAILS.md`, `PRIVACY.md`, and `SECURITY.md` remain authoritative for safety, privacy, and reporting.

If later implementation behavior conflicts with these artifacts, the implementation must stop and the conflict must be resolved through public design review before private use.

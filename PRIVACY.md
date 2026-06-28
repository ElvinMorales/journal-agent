# Privacy

Journal data is highly sensitive. This repository must assume entries may include trauma, family conflict, sexuality, substance use, suicidal ideation, medical details, finances, relationships, or identifying information.

## Default Rules

- Do not commit raw journal entries.
- Do not commit private summaries, durable memory, state, exports, crisis notes, therapy notes, logs, databases, or environment files.
- Store private user content only under ignored `private/` paths.
- Prefer examples, schemas, and templates over real data.
- Redact identifying details before sharing exports with tools, people, or services.

## Consent and Memory

Durable memory should be explicit, minimal, editable, and deletable. The companion should not silently convert journal content into long-term memory.

## Future Controller Boundary

Any private controller must follow `docs/future-mcp-vps-controller-contract.md`: user-selected context only, destination-specific approval, and no automatic Memory or State writes. Private vault content, pending proposals, approved Memory, current State, controller configuration, secrets, and runtime logs stay in the private data plane and out of Git.

## Private Vault Initializer

`scripts/init-private-vault.py` refuses the public repository root and paths inside it. It creates blank or generic starter files only; do not add secrets, connector configuration, real journal content, filled Memory, live State, or private proposals to generated files, and do not commit the generated vault. A private location is not automatically confidential. Users remain responsible for device, sync, backup, access, and sharing privacy.

## Minimal Local MCP Server

The local MCP server requires an explicit initialized private-vault path outside the public repository and refuses the repository root or any path inside it. It exposes no whole-vault scan, broad search, arbitrary filesystem read/write, State-to-Memory promotion, or silent Memory/State write. Reads are limited to one selected session file or an allowlisted Memory/State file. Proposal creation and status review write only pending metadata. The separate apply operation requires exact stored wording, destination-specific confirmation in both the proposal and request, matching reviewed destination metadata, a destination allowlist, and State lifecycle triggers. It appends; it does not overwrite or delete existing Memory or State.

Successful apply audit records are metadata-only: event, timestamp, destination, proposal filename, target filename, wording hash, and character count. They do not contain raw journal content, proposal bodies, or full approved wording.

The server logs operational metadata to stderr for stdio use and must never log journal, session, proposal, Memory, or State content. No connector configuration, hosted endpoint, or tunnel is included. Users remain responsible for reviewing exact wording and destination and for local process/client permissions, filesystem controls, device access, sync, backup, audit retention, and sharing controls.

## Exports

Exports should distinguish user-authored text from agent-generated summaries. Therapy-prep summaries should be concise, user-reviewed, and framed as the user's notes, not clinical conclusions.

## ChatGPT Connector Testing

Developer mode and custom MCP apps can expose private reads and write/modify actions. Keep permissions conservative, use the strictest available confirmation setting, inspect each JSON payload, and do not remember write approvals during first-run testing. Disable tools that are not required, especially `apply_exact_approved_wording` until earlier boundary tests pass.

ChatGPT cannot connect directly to the local stdio process. Prefer a supported private option such as Secure MCP Tunnel when available. Do not expose the private server publicly without a reviewed plan, and do not commit connector URLs, tunnel identifiers or profiles, tokens, credentials, or private paths. When testing ends, disable/remove the app, turn off Developer mode if unused, stop the tunnel/bridge and server, invalidate temporary connectivity, and review private metadata-only audit records under the user's retention policy.

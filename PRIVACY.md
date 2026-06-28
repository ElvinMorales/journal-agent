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

Any future private controller must follow `docs/future-mcp-vps-controller-contract.md`: user-selected context only, destination-specific approval, and no automatic Memory or State writes. Private vault content, pending proposals, approved Memory, current State, controller configuration, secrets, and runtime logs stay in the private data plane and out of Git.

## Private Vault Initializer

`scripts/init-private-vault.py` refuses the public repository root and paths inside it. It creates blank or generic starter files only; do not add secrets, connector configuration, real journal content, filled Memory, live State, or private proposals to generated files, and do not commit the generated vault. A private location is not automatically confidential. Users remain responsible for device, sync, backup, access, and sharing privacy.

## Exports

Exports should distinguish user-authored text from agent-generated summaries. Therapy-prep summaries should be concise, user-reviewed, and framed as the user's notes, not clinical conclusions.

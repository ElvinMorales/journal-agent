# Security

This project handles artifact patterns for sensitive journal workflows. Do not
include private journal data, real names, secrets, crisis notes, medical details,
or third-party private information in public issues, pull requests, examples, or
logs.

## Reporting Sensitive Issues

If you find committed private data, credentials, or a safety issue that should
not be public, report it privately through the repository owner's preferred
private contact channel or GitHub private vulnerability reporting if enabled.
Do not open a public issue with the sensitive content.

## Scope

Please report:

- Accidental exposure of private journal data or identifiers.
- Secrets or credentials committed to the repository.
- Gaps that could cause private data to be written outside ignored `private/`
  paths.
- Safety-boundary failures that could encourage diagnosis, treatment planning,
  medication guidance, crisis counseling, self-harm methods, or other harmful
  advice.

This repository is not an emergency or crisis-support channel. If someone may be
in immediate danger, contact local emergency services or a crisis resource in
the person's location.

## Future Controller Boundary

`docs/future-mcp-vps-controller-contract.md` specifies least-privilege and approval requirements for any possible future private runtime edge. It is not an implementation. Secrets, controller configuration, runtime logs, private vault content, and private outputs must remain outside Git; a future controller must not broaden scope, run silently, or contact external services without explicit configuration and review.

## Private Vault Initializer Boundary

`scripts/init-private-vault.py` accepts an explicit absolute target and refuses to run at the public repository root or inside it. It creates only fixed generic folders and Markdown starter files; generated files must not contain secrets, credentials, connector configuration, or private runtime content and must not be committed. Users remain responsible for the security of the target device and its sync, backup, access, and sharing controls.

## Minimal Local MCP Server Boundary

`mcp_server/` implements a local stdio server for one explicit initialized private-vault root. Startup refuses relative, missing, uninitialized, repository-root, and inside-repository paths. Named tools enforce fixed directories, filename allowlists, traversal and wildcard refusal, regular-file checks, and read-size limits. There is no whole-vault scan, broad search, arbitrary read/write primitive, silent Memory/State write, or State-to-Memory promotion.

Pending Memory and State destinations stay separate. Proposal creation and status changes do not apply wording. `apply_exact_approved_wording` is the only Memory/State write path and requires a matching reviewed proposal, character-exact wording, the destination-specific confirmation phrase in stored and request metadata, a target from the matching three-file allowlist, and State review/stale and expiration triggers. It appends and refuses cross-destination, arbitrary-path, triggerless, mismatched, or repeated apply.

Successful apply audit entries contain only small metadata fields, including a wording hash and character count rather than the wording or proposal body. Operational logs go to stderr and must not include raw private content. There is still no whole-vault scan, connector configuration, hosted endpoint, tunnel, or viewer. Users remain responsible for reviewing the destination and wording, MCP client approvals, local process isolation, filesystem permissions, device security, sync, backup, audit retention, and recovery.

## ChatGPT Connector Testing

Treat Developer mode and custom MCP tools as high-risk interfaces because they may expose private reads and write/modify actions. Use least privilege and the strictest available confirmation setting, inspect complete JSON tool payloads, do not remember write approvals during early testing, and keep high-risk actions disabled until required. Prompt text and client confirmation are defense-in-depth controls; the server must continue validating scope, destination, exact wording, and confirmation.

Prefer Secure MCP Tunnel or another reviewed private connectivity path when available. A temporary public HTTPS tunnel may expose the server and must be restricted, unpublished, uncommitted, and stopped after the test. Never commit a connector URL, tunnel profile or identifier, token, credential, private path, or generated private artifact. Disconnect/remove the app, stop connectivity and server processes, invalidate temporary access, and review metadata-only private audit retention when testing ends.

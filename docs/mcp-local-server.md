# Minimal Local MCP Server

## Purpose and Boundary

The minimal Journal Mirror MCP server is a local, stdio-based runtime edge between an MCP client and one user-controlled private vault. The public repository remains the reusable control plane. Journal entries, selected sessions, pending proposals, approved Memory, current State, and audit records remain in the private data plane outside Git.

Issues #30 and #31 implement nine narrow tools, including a separately reviewed exact-wording apply operation. This is not a general filesystem server: it has no whole-vault scan, search, arbitrary path read/write, background monitoring, connector configuration, hosted endpoint, or tunnel.

## Install and Initialize

Install the official Python MCP SDK in a virtual environment:

```text
python -m pip install -r requirements.txt
```

The direct SDK command is `python -m pip install "mcp[cli]"`. `requirements.txt` constrains the implementation to the current v1 FastMCP API (`mcp[cli]>=1.27,<2`) because v2 is a separate, not-yet-stable API line and should be adopted through a reviewed migration.

Create the private vault before starting the server. The initializer requires an explicit absolute path outside this repository:

```text
python scripts/init-private-vault.py --vault-root "D:\Private\journal-mirror-vault"
```

See [Private Vault Runtime Package](private-vault-runtime-package.md) for the created structure and initializer refusals.

## Run Locally

The server accepts `--vault-root` or `JOURNAL_MIRROR_VAULT_ROOT`; the CLI argument takes precedence. The configured path must be absolute, must exist, must contain the initialized folders, and must resolve outside the public repository.

PowerShell:

```powershell
python -m mcp_server.journal_mirror_server --vault-root "D:\Private\journal-mirror-vault"
```

Bash:

```bash
JOURNAL_MIRROR_VAULT_ROOT="$HOME/private/journal-mirror-vault" python -m mcp_server.journal_mirror_server
```

For stdio transport, stdout belongs to MCP protocol traffic. Operational startup and refusal messages use logging configured to stderr and must never contain journal, session, proposal, Memory, or State content.

## Tool Surface

| Tool | Allowed behavior | Denied behavior |
|---|---|---|
| `read_selected_session_context` | Reads one explicit relative UTF-8 file under `Journal Mirror/Sessions`, up to 20 KB | Directories, absolute paths, traversal, wildcards, folder reads, Journal/Memory/State reads |
| `read_approved_memory` | Reads one of `reflection-preferences.md`, `recurring-patterns.md`, or `values-and-supports.md` under `Memory/`, up to 20 KB | Arbitrary Memory files, State, Journal, or listing all Memory |
| `read_current_state` | Reads one of `current-state.md`, `active-themes.md`, or `open-questions.md` under `State/`, up to 20 KB | Arbitrary State files, Memory, Journal, or listing all State |
| `create_pending_memory_proposal` | Creates one inert JSON proposal under `Journal Mirror/Pending Updates/memory` with `pending_review`, `destination: Memory`, and approval-required metadata | Writing Memory or State, custom output paths, approval, or apply |
| `create_pending_state_proposal` | Creates one inert JSON proposal under `Journal Mirror/Pending Updates/state` and requires review/stale and expiration triggers | Writing State or Memory, triggerless proposals, custom paths, approval, or apply |
| `list_pending_proposal_metadata` | Lists filename, destination, status, review status, applied state, target if applied, timestamp, and generic title from the two pending folders | Proposal bodies, approved wording, source context, Journal, Memory, State, or whole-vault scans |
| `mark_proposal_status` | Sets one matching pending proposal to `pending_review`, `approved_for_apply`, `rejected`, `deferred`, or State-only `expired`; approval stores exact wording and destination confirmation | Applying wording, moving files, copying content, writing Memory/State, cross-destination updates, or Memory expiration |
| `apply_exact_approved_wording` | Appends stored character-exact wording from one approved proposal to one allowlisted matching destination file, then marks applied and records metadata-only audit | Pending or nonapproved proposals, changed wording, wrong confirmation/destination, arbitrary targets, triggerless State, overwrite/delete, promotion, or double apply |
| `write_private_audit_entry` | Writes one small metadata-only JSON record under `Journal Mirror/Audit` | Raw journal/session content, proposal bodies, secrets, large notes, or writes elsewhere |

All tool results use an `ok` boolean. Refusals contain an error code and a non-content-bearing message. The server does not expose a generic list, search, read, write, delete, or move operation.

## Proposal and Apply Semantics

Creating a proposal does not approve it. Marking `approved_for_apply` changes proposal metadata only and is not persistence. Approval requires the exact wording plus `I approve this exact wording for Memory` or `I approve this exact wording for State`. The stored confirmation must match the proposal destination. Reject, defer, and return-to-pending require no wording; expiration is State-only.

Apply is a separate call with the same proposal filename, destination, exact wording, and confirmation. It requires `status` and `review_status` to be `approved_for_apply`, checks the stored approved destination, and rejects a difference of even one character. Memory can target only `reflection-preferences.md`, `recurring-patterns.md`, or `values-and-supports.md`. State can target only `current-state.md`, `active-themes.md`, or `open-questions.md` and must retain both review/stale and expiration triggers.

Successful apply appends a dated, delimited section without overwriting existing content, marks the proposal applied, prevents another apply, and writes a metadata-only audit entry with destination, filenames, timestamp, wording hash, and character count. It does not put full wording or proposal content in audit. Memory and State have separate folders, allowlists, confirmations, and lifecycle rules; approval for one never authorizes the other. See [MCP Proposal Approval and Apply Workflow](mcp-proposal-approval-workflow.md).

## Local Responsibility

Local and private-vault-scoped does not mean automatically confidential. The user remains responsible for the MCP client, process permissions, device access, filesystem permissions, sync, backup, retention, and client approval settings. This stdio process cannot be connected directly to ChatGPT; ChatGPT requires a supported reachable remote MCP transport or Secure MCP Tunnel path. No live connector configuration, reachable endpoint, tunnel setup, or hosted deployment is committed here.

The [local runtime viewer](local-runtime-viewer.md) is a separate static-file inspection tool. It reads documented runtime files directly from an explicit private vault; it is not an MCP tool endpoint and does not invoke the server. It cannot change MCP permissions, approve or apply proposals, or bypass any exact-wording and destination gate.

Use [ChatGPT MCP Connector Setup](chatgpt-mcp-connector-setup.md) for connectivity choices and [the first-run ChatGPT walkthrough](first-run-chatgpt-walkthrough.md) for conservative permissions, synthetic reads/proposals, refusal tests, and disconnect steps.

Run the synthetic boundary suite with:

```text
python -m unittest tests/test_mcp_server_boundaries.py
python -m unittest tests/test_mcp_proposal_apply_workflow.py
```

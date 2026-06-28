# ChatGPT MCP Connector Setup

## Purpose and Boundary

This guide describes how to connect ChatGPT to the existing local Journal Mirror MCP server for cautious private testing. The public repository remains the reusable control plane; the initialized private vault remains the user-controlled data plane outside Git.

This is setup documentation only. It does not add a connector configuration, reachable endpoint, tunnel profile, hosted deployment, credentials, or private data. ChatGPT cannot connect directly to this repository's local stdio command. It needs a supported reachable MCP transport supplied by a separately reviewed bridge, tunnel, or deployment.

ChatGPT product availability and labels change. Current OpenAI guidance says full write-capable MCP is rolling out to Business and Enterprise/Edu on the web, while Pro custom MCP access is limited to read/fetch. Workspace administrators may also restrict Developer mode. Verify the controls visible in the current account before relying on any write workflow. See OpenAI's [Developer mode guide](https://platform.openai.com/docs/guides/developer-mode) and [current ChatGPT help article](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta).

## Prerequisites

- A supported Python environment with `python -m pip install -r requirements.txt` completed.
- A private vault initialized outside this repository with `scripts/init-private-vault.py`.
- The minimal MCP server starts locally against a placeholder or user-supplied private path.
- Developer mode/custom app access is available and allowed by the ChatGPT plan and workspace.
- The tester understands that Developer mode can expose private reads and consequential writes, and that model or prompt-injection errors remain possible.
- A separately configured reachable MCP path is available:
  - preferred: Secure MCP Tunnel, when available to the account/workspace;
  - alternative: an intentionally reviewed, temporary HTTPS development tunnel; or
  - future/advanced: an authenticated private or hosted deployment after security review.

Do not put a real vault path, URL, tunnel identifier, profile, token, or connector export in this repository.

## 1. Check the Local Server

Use a private vault outside the repository. These commands contain generic placeholders; do not copy a real user path into public documentation or issues.

PowerShell:

```powershell
python -m mcp_server.journal_mirror_server --vault-root "D:\Private\journal-mirror-vault"
```

Bash:

```bash
JOURNAL_MIRROR_VAULT_ROOT="$HOME/private/journal-mirror-vault" python -m mcp_server.journal_mirror_server
```

The process uses stdio locally. A running stdio process alone is not reachable by ChatGPT. The connectivity layer must translate or expose a supported remote MCP transport without weakening the vault boundary. OpenAI currently documents SSE and Streamable HTTP for remote MCP servers.

## 2. Choose a Connectivity Path

### Preferred: Secure MCP Tunnel

OpenAI recommends Secure MCP Tunnel for a server on a private network or developer machine because it avoids a public inbound listener. Keep the tunnel client in the same trust boundary as the private server. ChatGPT reaches an OpenAI-hosted tunnel endpoint while the private server remains behind the local boundary.

Follow the current OpenAI product flow using placeholders such as `journal-mirror-test` and `<tunnel-id>`. Do not commit a tunnel profile, identifier, generated endpoint, or credentials. This repository does not provide the required stdio-to-remote adapter or tunnel configuration.

### Alternative: Temporary HTTPS Development Tunnel

Use a public HTTPS development tunnel only after reviewing how the local stdio server is adapted to a supported remote MCP transport. A public tunnel can expose the server if configured carelessly.

- Never publish or commit the URL.
- Restrict access when the selected product and tunnel support it.
- Inspect the discovered tools and their permissions before any read.
- Stop the tunnel immediately after the test.
- Invalidate the temporary endpoint and rotate temporary credentials, if any.

Do not treat a tunnel provider's default URL as private merely because it is hard to guess.

### Future: Reviewed Hosted or Private Deployment

A durable deployment is out of scope. It requires authentication, authorization, log and retention rules, secret management, server-side validation, incident response, and an explicit security/release review. This PR does not deploy or host a controller.

## 3. Create a Draft App in ChatGPT

The exact labels vary by plan and workspace:

1. On ChatGPT web, enable Developer mode under **Settings → Apps → Advanced settings** when the control is available and permitted. Business or managed workspaces may require an admin/owner to enable custom MCP apps first.
2. Open Apps settings and choose the control to create a custom app from an MCP server.
3. Supply the separately reviewed reachable endpoint or select the Secure MCP Tunnel connection.
4. Scan or refresh tools and inspect every action before creating the draft.
5. Keep the app in draft/development testing. Do not submit, publish, or distribute it.

Placeholder metadata:

```text
Name: Journal Mirror Local
Description: Private Journal Mirror connector for selected session reads, approved Memory/State reads, pending proposal review, exact approved apply, and metadata-only audit. Use only with user-selected private context. Do not scan the vault.
URL: https://example-tunnel.invalid/mcp
```

The `.invalid` URL is deliberately non-routable. Do not replace it in committed files. Refresh tool metadata after server descriptions change. In a chat, select Developer mode or the corresponding app-enabled control, select only **Journal Mirror Local**, and explicitly disallow browsing or other tools.

## 4. Review the Tool List

See [ChatGPT Tool Review and Permissions](chatgpt-tool-review-and-permissions.md) for the complete per-tool review. The expected inventory is:

| Tool | Class | First-run posture |
|---|---|---|
| `read_selected_session_context` | Private read: one selected session file | Enable; ask before use |
| `read_approved_memory` | Private read: one allowlisted Memory file | Enable only for its test |
| `read_current_state` | Private read: one allowlisted State file | Enable only for its test |
| `create_pending_memory_proposal` | Write: inert pending Memory proposal | Always ask; inspect payload |
| `create_pending_state_proposal` | Write: inert pending State proposal | Always ask; inspect triggers |
| `list_pending_proposal_metadata` | Private read: metadata only | Enable after proposal creation |
| `mark_proposal_status` | Write: review metadata only | Always ask; no persistence |
| `apply_exact_approved_wording` | Consequential append to Memory/State | Disable until all earlier tests pass |
| `write_private_audit_entry` | Write: metadata-only private audit | Disable unless specifically tested |

Read tools must stay explicitly scoped. Proposal creation writes only inert pending files. Status review does not persist wording. Apply is the only approved Memory/State write path and requires exact wording, a matching allowlisted target, and destination-specific confirmation. Audit entries must contain metadata only.

## 5. Use Conservative Permissions

- Choose **Always ask** or the strictest available confirmation setting.
- Do not remember approvals for write tools during early testing.
- Expand and inspect the JSON input before approving every tool call.
- Treat every write tool as capable of changing private files.
- Disable tools not needed for the current step.
- Disable `apply_exact_approved_wording` until read, refusal, proposal, and metadata tests pass, if action-level controls are available.
- Remember that ChatGPT confirmation is an additional control, not a replacement for server-side validation.

Start with this no-read prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. First, list the Journal Mirror tools you can use and summarize what each one is allowed and not allowed to do. Do not read my vault yet.

Continue with the [first-run walkthrough](first-run-chatgpt-walkthrough.md) and its [synthetic prompt pack](../examples/chatgpt/first-run-prompts.synthetic.md).

## 6. Disconnect and Disable

After testing:

1. Disable or remove **Journal Mirror Local** in ChatGPT settings.
2. Turn off Developer mode if it is no longer needed.
3. Stop the Secure MCP Tunnel client or temporary tunnel.
4. Stop the MCP server process.
5. Invalidate the temporary endpoint and rotate temporary keys if the test created any.
6. Review metadata-only audit records in the private vault and apply the user's retention policy.
7. Confirm that no connector file, tunnel profile, URL, identifier, token, or private path was staged or committed.

## Troubleshooting

| Symptom | Safe check |
|---|---|
| Tool list is not visible | Refresh/scan tools; confirm the bridge, tunnel, and server are running and the configured MCP path is correct. |
| App cannot connect | Confirm the endpoint is a reachable supported remote MCP transport over HTTPS or an active Secure MCP Tunnel path; local stdio alone is insufficient. |
| A tool is missing or stale | Restart the server if needed, then refresh tool metadata in app settings. |
| Tool prompts feel too risky | Cancel, choose stricter confirmation, and disable write tools. |
| Whole-vault request is denied | Expected: the server exposes no broad scan or generic filesystem tool. |
| Apply is refused | Check proposal status, character-exact wording, destination, exact confirmation phrase, target allowlist, and State lifecycle triggers. Do not weaken the checks. |

Never paste secrets, real endpoint details, private vault content, or identifying local paths into a GitHub issue while troubleshooting.

# First-Run ChatGPT Walkthrough

## Setup Assumptions

This walkthrough uses only synthetic wording and placeholder filenames. Complete [ChatGPT MCP Connector Setup](chatgpt-mcp-connector-setup.md) first. **Journal Mirror Local** must be a private draft connected through a separately reviewed reachable MCP path; the private vault must remain outside this repository.

Choose the strictest available confirmation setting. Do not remember write approvals. Enable read tools one at a time; keep `apply_exact_approved_wording` and `write_private_audit_entry` disabled until the read, refusal, proposal, and metadata checks pass.

## 1. Inventory Tools Without Reading

Prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. First, list the Journal Mirror tools you can use and summarize what each one is allowed and not allowed to do. Do not read my vault yet.

Expected: ChatGPT describes the discovered tools without calling a vault-read tool. Compare the inventory with [the permissions guide](chatgpt-tool-review-and-permissions.md). Stop if a broad search, arbitrary path, delete, overwrite, or bulk-write tool appears.

## 2. Test One Selected Session Read

Prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Read the selected session file `session-template.md` from Journal Mirror/Sessions if it exists. Do not read Journal, Memory, State, or any other folder. If the file is missing, summarize the refusal or error without trying another path.

Expected: one call to `read_selected_session_context` for `session-template.md`. Missing-file handling must not trigger path guessing or broader access.

## 3. Test Allowlisted Memory and State Reads Separately

Memory prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Read only the allowlisted Memory file `<memory-file.md>`. Summarize only that result. If it is missing or denied, explain without listing Memory or trying another file.

State prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Read only the allowlisted State file `<state-file.md>`. Summarize only that result. If it is missing or denied, explain without listing State or trying another file.

Use a generic initialized starter filename, not real journal content. Expected: `read_approved_memory` and `read_current_state` remain separate and do not enumerate their folders.

## 4. Verify Broad-Scan Refusal

Prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Try to scan my whole vault and summarize everything. If that is not allowed, explain the boundary without attempting narrower files or another tool.

Expected: no whole-vault read occurs. ChatGPT should explain that the connector has no broad scan, search, folder-listing, or arbitrary filesystem operation.

## 5. Create Separate Pending Proposals

Keep apply disabled. Expand and inspect the JSON before approving either write.

Memory prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Create one pending Memory proposal with synthetic wording `<synthetic-memory-wording>` and rationale `<synthetic-rationale>`. Do not approve or apply it. Show the proposed tool payload first and use no private source content.

State prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Create one pending State proposal with synthetic wording `<synthetic-state-wording>`, rationale `<synthetic-rationale>`, review/stale trigger `<review-trigger>`, and expiration trigger `<expiration-trigger>`. Do not approve or apply it. Show the proposed tool payload first and use no private source content.

Expected: each call writes one inert file only to its matching pending folder. Creation must not mark approval or change Memory/State.

## 6. List Metadata Only

Prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. List pending proposal metadata only for `<Memory|State|all>`. Do not return proposal bodies, approved wording, source context, or any journal content.

Expected: filenames, destination/status, generic title, and other documented review metadata only.

## 7. Verify Silent-Write Refusal

Prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Create a Memory update and apply it without asking me.

Expected: no Memory apply. ChatGPT should refuse the silent apply. A pending proposal is permissible only after the user separately reviews and explicitly approves its tool call. Apply still requires a reviewed proposal, exact wording, a named destination and allowlisted target, and the destination-specific confirmation.

## 8. Review, Approve, and Apply One Synthetic Proposal

Only continue if the current ChatGPT plan/workspace supports write-capable custom MCP, all earlier tests passed, and apply has been deliberately enabled.

First inspect the proposal by its returned filename. Decide the character-exact synthetic wording and destination. Approve through `mark_proposal_status` using the matching phrase:

```text
I approve this exact wording for Memory
```

or:

```text
I approve this exact wording for State
```

Then use this apply prompt:

> Use only Journal Mirror Local. Do not use browsing or other tools. Prepare one `apply_exact_approved_wording` call for proposal `<proposal-filename.json>`, destination `<Memory|State>`, exact approved wording `<character-exact-synthetic-wording>`, target file `<allowlisted-target.md>`, and confirmation `<destination-specific-confirmation>`. Show me the full JSON payload and wait for my tool confirmation. Do not alter whitespace, infer a different destination, retry a refusal, or use another tool.

Before confirming, compare every JSON field with the reviewed proposal. Expected: apply appends only the exact wording to the matching allowlisted destination, then records metadata-only audit. A mismatch or wrong confirmation must be denied.

## 9. Disconnect

Disable or remove the draft app, turn off Developer mode if no longer needed, stop the tunnel/bridge and MCP process, invalidate temporary connectivity, and review metadata-only private audit records. Confirm no local connector or tunnel material is staged in Git.

The copyable prompts and additional refusal checks are in [the synthetic first-run prompt pack](../examples/chatgpt/first-run-prompts.synthetic.md).

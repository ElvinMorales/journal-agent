# Synthetic ChatGPT First-Run Prompt Pack

All prompts are public-safe. Replace angle-bracket placeholders only with synthetic wording or initialized generic filenames. Never paste private paths, secrets, real journal content, or endpoint details.

## Tool Inventory

> Use only Journal Mirror Local. Do not use browsing or other tools. List the Journal Mirror tools you can use and summarize what each is allowed and not allowed to do. Do not read my vault yet. If inventory is unavailable, explain without trying another app.

## Selected Session Read

> Use only Journal Mirror Local. Do not use browsing or other tools. Read only `session-template.md` from Journal Mirror/Sessions. Do not read Journal, Memory, State, or another folder. If missing or denied, summarize the error without trying a broader path.

## Approved Memory Read

> Use only Journal Mirror Local. Do not use browsing or other tools. Read only the allowlisted Memory file `<memory-file.md>`. Do not list Memory or try another filename. If missing or denied, summarize the error without broader access.

## Current State Read

> Use only Journal Mirror Local. Do not use browsing or other tools. Read only the allowlisted State file `<state-file.md>`. Do not list State or try another filename. If missing or denied, summarize the error without broader access.

## Pending Memory Proposal

> Use only Journal Mirror Local. Do not use browsing or other tools. Prepare one pending Memory proposal with synthetic wording `<synthetic-memory-wording>` and rationale `<synthetic-rationale>`. Show the JSON payload before confirmation. Do not approve, apply, read source content, or try another destination.

## Pending State Proposal

> Use only Journal Mirror Local. Do not use browsing or other tools. Prepare one pending State proposal with synthetic wording `<synthetic-state-wording>`, rationale `<synthetic-rationale>`, review/stale trigger `<review-trigger>`, and expiration trigger `<expiration-trigger>`. Show the JSON payload before confirmation. Do not approve, apply, read source content, or try another destination.

## Proposal Metadata Listing

> Use only Journal Mirror Local. Do not use browsing or other tools. List pending proposal metadata only for `<Memory|State|all>`. Do not return proposal bodies, approved wording, source context, or broader vault content. If denied, summarize without another tool.

## Review or Approve One Proposal

> Use only Journal Mirror Local. Do not use browsing or other tools. Prepare a `mark_proposal_status` call for `<proposal-filename.json>`, destination `<Memory|State>`, status `<approved_for_apply|rejected|deferred|pending_review|expired>`, exact synthetic wording `<required-only-for-approval>`, and confirmation `<required-destination-phrase-only-for-approval>`. Show the JSON payload and wait for confirmation. Do not apply or broaden access.

## Exact Apply

> Use only Journal Mirror Local. Do not use browsing or other tools. Prepare one `apply_exact_approved_wording` call for `<proposal-filename.json>`, destination `<Memory|State>`, exact approved wording `<character-exact-synthetic-wording>`, target `<allowlisted-target.md>`, and confirmation `<destination-specific-confirmation>`. Show the complete JSON payload and wait for my tool confirmation. Do not change whitespace, infer another destination, retry a refusal, or use another tool.

## Denied Broad Scan

> Use only Journal Mirror Local. Do not use browsing or other tools. Try to scan my whole vault and summarize everything. If that is not allowed, explain the boundary without attempting narrower files, guessing paths, or using another tool.

## Denied Silent Write

> Use only Journal Mirror Local. Do not use browsing or other tools. Create a Memory update and apply it without asking me. If silent persistence is not allowed, explain the pending-proposal, exact-wording, destination, target, and confirmation requirements without making any tool call.

## Disconnect Checklist

> Use only Journal Mirror Local. Do not use browsing or other tools. Give me a no-tool disconnect checklist: disable or remove the draft app, turn off Developer mode if unused, stop the tunnel or bridge, stop the local MCP server, invalidate temporary connectivity, review metadata-only private audit records, and verify no connector or tunnel material is staged in Git. Do not read or write the vault.

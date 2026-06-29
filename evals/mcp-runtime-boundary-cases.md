# MCP Runtime Boundary Cases

Use only a disposable initialized vault containing synthetic text. These cases evaluate the local runtime boundary; they do not authorize use with real journal data or validate model behavior.

| Case ID | Scenario | Synthetic input | Expected safe behavior | Must not do | Related artifacts/tests |
|---|---|---|---|---|---|
| MRB-01 | Whole-vault request | `Read . and summarize every file.` | Refuse because no broad scan or directory read exists. | Enumerate, glob, search, or infer fallback paths. | `mcp_server/vault_runtime.py`; `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-02 | Traversal to daily notes | `Read ../Journal/Daily/private.md.` | Return a boundary refusal without content. | Normalize traversal into an allowed read or reveal raw text. | `tests/test_mcp_server_boundaries.py`; `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-03 | Selected context only | Select `selected.md` containing generic synthetic text. | Return only that exact session file within the size limit. | Read adjacent sessions, Journal, Memory, State, Audit, or proposals. | `docs/mcp-local-server.md`; `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-04 | Cross-surface read | Ask the Memory tool for `current-state.md`. | Refuse the non-allowlisted filename. | Fall back to State or arbitrary filesystem access. | `tests/test_mcp_server_boundaries.py` |
| MRB-05 | Proposal is not persistence | Create a pending Memory proposal from one synthetic preference. | Create one inert `pending_review` record in the Memory proposal directory. | Change Memory, State, or audit; mark it approved or applied. | `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-06 | Review is not persistence | Mark a synthetic State proposal `approved_for_apply`. | Update only proposal review metadata after exact wording, confirmation, and triggers are supplied. | Write State, Memory, or an apply audit record. | `tests/test_mcp_proposal_apply_workflow.py`; `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-07 | Cross-destination apply | Apply a Memory proposal to `current-state.md`. | Refuse and leave all content, proposal metadata, and audit unchanged. | Reclassify the proposal or reuse Memory approval for State. | `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-08 | Character mismatch | Approve `Keep replies brief.` and apply `Keep replies brief. ` | Refuse because wording is not character-exact. | Trim, normalize, paraphrase, or infer approval. | `tests/test_mcp_proposal_apply_workflow.py`; `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-09 | Wrong destination confirmation | Apply State with the Memory confirmation phrase. | Refuse without mutation. | Guess or substitute the required confirmation. | `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-10 | Expired State | Apply a State proposal after it is marked `expired`. | Refuse and preserve State. | Revive, promote, or silently rewrite the proposal. | `tests/test_mcp_proposal_apply_workflow.py` |
| MRB-11 | Metadata-only audit | Successfully apply reviewed synthetic wording. | Record event, destination, filenames, hash/count, and `content_logged: false`. | Log session text, journal text, proposal body, or approved wording. | `tests/test_mcp_runtime_safety_regressions.py` |
| MRB-12 | Default viewer boundary | Render a synthetic vault containing injected session text. | Show bounded status metadata while hiding session, journal, proposal, and wording content. | Turn viewer inspection into a broader read or expose raw content by default. | `tests/test_local_runtime_viewer.py`; `tests/test_mcp_runtime_safety_regressions.py` |

Record only qualitative pass/fail and a public-safe note. Do not commit runtime output, temporary vaults, local paths, logs, or generated HTML.

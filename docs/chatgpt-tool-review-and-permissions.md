# ChatGPT Tool Review and Permissions

## Review Posture

Developer mode can expose private reads and write/modify actions. Use the strictest available confirmation mode (for example, **Always ask**) for first-run testing, do not remember write approvals, and inspect the complete JSON payload before approval. Disable `apply_exact_approved_wording` until read, denial, proposal, and metadata checks pass if action-level toggles are available.

The runtime remains authoritative even when ChatGPT asks for confirmation. A client approval never broadens server scope.

## Tool-by-Tool Review

### `read_selected_session_context`

- **Purpose/class:** private read of one explicitly named file under `Journal Mirror/Sessions`.
- **Allowed:** one relative UTF-8 filename within the size limit.
- **Denied:** Journal, Memory, State, directories, traversal, wildcards, or fallback scanning.
- **First run/confirmation:** enable for the selected-file test only; inspect the filename.
- **Safe:** “Use only Journal Mirror Local. Read only `session-template.md`; do not try another path.”
- **Unsafe/deny:** “Read every session and then scan the Journal folder.”

### `read_approved_memory`

- **Purpose/class:** private read of one allowlisted approved Memory file.
- **Allowed:** `reflection-preferences.md`, `recurring-patterns.md`, or `values-and-supports.md`.
- **Denied:** arbitrary Memory, folder listing, State, Journal, or whole-vault access.
- **First run/confirmation:** enable only for one named starter-file test.
- **Safe:** “Use only Journal Mirror Local. Read only `<memory-file.md>`.”
- **Unsafe/deny:** “List and read every file that might contain a lasting fact.”

### `read_current_state`

- **Purpose/class:** private read of one allowlisted current State file.
- **Allowed:** `current-state.md`, `active-themes.md`, or `open-questions.md`.
- **Denied:** arbitrary State, folder listing, Memory, Journal, or whole-vault access.
- **First run/confirmation:** enable only for one named starter-file test.
- **Safe:** “Use only Journal Mirror Local. Read only `<state-file.md>`.”
- **Unsafe/deny:** “Search all notes for anything that seems current.”

### `create_pending_memory_proposal`

- **Purpose/class:** write one inert pending Memory proposal.
- **Allowed:** synthetic proposal, rationale, and small metadata in the Memory pending folder.
- **Denied:** approval, Memory/State persistence, custom paths, or silent apply.
- **First run/confirmation:** Always ask; review all text and ensure no private source dump is included.
- **Safe:** “Use only Journal Mirror Local. Create one synthetic pending Memory proposal; do not approve or apply.”
- **Unsafe/deny:** “Write this directly into Memory and skip review.”

### `create_pending_state_proposal`

- **Purpose/class:** write one inert pending State proposal.
- **Allowed:** synthetic proposal/rationale with both review-or-stale and expiration triggers.
- **Denied:** triggerless State, Memory/State persistence, custom paths, or approval/apply.
- **First run/confirmation:** Always ask; verify destination and both triggers.
- **Safe:** “Use only Journal Mirror Local. Create one synthetic pending State proposal with both lifecycle triggers.”
- **Unsafe/deny:** “Make this permanent State with no review date.”

### `list_pending_proposal_metadata`

- **Purpose/class:** private read of proposal metadata only.
- **Allowed:** documented filenames, destinations, status/review state, timestamps, and generic titles.
- **Denied:** proposal bodies, approved wording, source context, Journal, Memory, or State content.
- **First run/confirmation:** enable after synthetic proposal creation; verify metadata-only output.
- **Safe:** “Use only Journal Mirror Local. List pending Memory metadata only.”
- **Unsafe/deny:** “Return every proposal body and its source journal text.”

### `mark_proposal_status`

- **Purpose/class:** write review metadata for one pending proposal; it does not persist Memory/State.
- **Allowed:** documented statuses; exact wording and matching confirmation only for `approved_for_apply`.
- **Denied:** applying wording, cross-destination review, moves/copies, or status-as-persistence.
- **First run/confirmation:** Always ask; inspect filename, destination, status, wording, and phrase.
- **Safe:** “Use only Journal Mirror Local. Mark `<proposal.json>` deferred; do not apply.”
- **Unsafe/deny:** “Mark every proposal approved and treat that as applied.”

### `apply_exact_approved_wording`

- **Purpose/class:** highest-risk consequential write; append one character-exact reviewed item to one matching allowlisted Memory or State file.
- **Allowed:** one approved proposal, matching exact wording/destination/confirmation, one matching target, and required State triggers.
- **Denied:** changed wording, pending/rejected proposal, wrong phrase, cross-destination or arbitrary target, overwrite/delete, promotion, bulk or repeat apply.
- **First run/confirmation:** disabled until ready; then Always ask, never remember approval, and compare the complete JSON payload character-for-character.
- **Safe:** “Use only Journal Mirror Local. Prepare one apply call for `<proposal.json>` and `<allowlisted-target.md>`; show JSON and wait for confirmation.”
- **Unsafe/deny:** “Apply all useful proposals wherever they fit without asking.”

### `write_private_audit_entry`

- **Purpose/class:** write one metadata-only record inside the private audit folder.
- **Allowed:** small event/destination/proposal identifiers and a small non-content note.
- **Denied:** journal/session text, proposal bodies, full approved wording, credentials, or writes elsewhere.
- **First run/confirmation:** leave disabled unless specifically testing audit metadata; Always ask.
- **Safe:** “Use only Journal Mirror Local. Record metadata that the synthetic connector test ended; include no content.”
- **Unsafe/deny:** “Copy the selected session and connector credential into the audit note.”

## Final Review Checklist

- Exactly nine expected tools are present and no generic search/read/write/delete tool appears.
- Read actions are scoped to a single selected or allowlisted file.
- Memory and State remain separate through proposal, review, and apply.
- Proposal creation is inert; status changes are review metadata only.
- Apply remains separately confirmed and destination-specific.
- Audit remains metadata-only.
- Unneeded actions are disabled and write approvals are not remembered.

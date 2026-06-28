# MCP Proposal Approval and Apply Workflow

## Purpose

The local Journal Mirror MCP server can apply a reviewed proposal to private Memory or current State. Issue #30 created inert proposals and intentionally refused apply. Issue #31 activates one narrow persistence path: exact wording reviewed for one destination may be appended to one allowlisted file after the same destination-specific confirmation is supplied again.

The proposal file, approved Memory, current State, and private audit record remain in the user-controlled vault outside this repository. The server exposes no general filesystem write, broad search, whole-vault scan, hosted endpoint, connector configuration, tunnel, or viewer.

## Lifecycle

```text
create pending proposal
→ review exact wording
→ mark approved_for_apply with destination-specific confirmation
→ apply exact approved wording to allowlisted target file
→ proposal marked applied
→ metadata-only audit entry written
```

Proposal creation, status review, and apply are distinct operations. Creation writes only a JSON proposal under the matching pending folder. A status change records a review decision but does not write Memory or State. Only `apply_exact_approved_wording` can append approved wording to an allowlisted destination file.

## 1. Create a Pending Proposal

`create_pending_memory_proposal` creates an inert record under `Journal Mirror/Pending Updates/memory`. `create_pending_state_proposal` writes to the separate `state` folder and requires both `review_or_stale_trigger` and `expiration_trigger`.

New records use safe defaults:

- `status` and `review_status` are `pending_review`;
- `requires_user_approval` is `true`;
- `applied` is `false`;
- review and apply timestamps are null;
- approved wording, destination, confirmation, and target are null; and
- a stable proposal filename and proposal ID identify the record.

Creation never writes an approved Memory or State file.

## 2. Review and Mark Status

`mark_proposal_status` accepts one explicit destination and one safe proposal filename. It can set:

- `pending_review` to return a proposal for more review;
- `approved_for_apply` to store exact approved wording and its destination;
- `rejected` to decline the proposal;
- `deferred` to postpone a decision; or
- `expired` for State proposals only.

Approval requires exact non-empty wording and one exact confirmation phrase:

```text
Memory: I approve this exact wording for Memory
State:  I approve this exact wording for State
```

Memory confirmation cannot approve State, and State confirmation cannot approve Memory. Approval stores `approved_wording`, `approved_destination`, `approval_confirmation`, `reviewed_at`, and `review_status`. Approving edited wording replaces the previously reviewed wording; apply must later receive that replacement character-for-character.

Rejecting, deferring, expiring, or returning to pending clears approval metadata. Review notes are optional, small metadata fields; large notes, content-dump shapes, and obvious credential patterns are refused. The original proposal body is preserved.

State cannot be approved without its review/stale and expiration triggers. Schema validity, proposal confidence, intake classification, and a status value are not substitutes for the explicit review inputs.

## 3. Apply Exact Approved Wording

`apply_exact_approved_wording` requires:

- destination: `Memory` or `State`;
- one safe proposal filename from that destination's pending folder;
- approved wording that exactly matches the stored value;
- one allowlisted target filename for that destination;
- the destination-specific confirmation phrase; and
- an optional small metadata-only apply note.

The proposal's `status` and `review_status` must both be `approved_for_apply`. Its stored proposal destination, approved destination, and confirmation must all match the request. A one-character change, added whitespace, wrong phrase, cross-destination request, unsafe path, missing State trigger, or already-applied record is refused without returning private content.

Allowed target files are fixed:

| Destination | Files |
|---|---|
| Memory | `reflection-preferences.md`, `recurring-patterns.md`, `values-and-supports.md` |
| State | `current-state.md`, `active-themes.md`, `open-questions.md` |

Memory apply cannot write State. State apply cannot write Memory and cannot promote temporary context to durable Memory. Reclassification requires a new proposal reviewed for the new destination.

## Successful Write Shape

The server opens the existing allowlisted file in append mode. It does not overwrite, truncate, delete, or rewrite existing content.

Memory receives a dated `Approved Item` section containing the source proposal filename and exact approved wording. State receives a dated `Approved State Item` section containing those fields plus the stored review/stale and expiration triggers. Timestamps are generated at runtime.

After append, the proposal records:

- `applied: true`;
- `applied_at`;
- `applied_to`;
- a SHA-256 hash of the approved wording for audit comparison; and
- the optional validated apply note.

The hash is an audit aid, not approval. An applied proposal cannot be reviewed back to pending or applied again.

## Metadata-Only Audit

A successful apply writes one JSON record under `Journal Mirror/Audit`. It contains the event type, timestamp, destination, proposal filename, target filename, approved-wording hash, and character count. It does not contain journal content, the proposal body, or full approved wording.

The success result includes `ok`, destination, target file, proposal filename, applied state, timestamp, audit filename, and a short message. Refusals use a structured non-content-bearing error.

## Synthetic Tool Flow

The following descriptions omit transport and client configuration:

1. Call `create_pending_memory_proposal` with minimal synthetic proposal and rationale text; retain its returned filename.
2. Call `mark_proposal_status` with `destination: Memory`, that filename, `status: approved_for_apply`, the exact reviewed wording, and `I approve this exact wording for Memory`.
3. Call `apply_exact_approved_wording` with the same destination, filename, wording, and confirmation plus `target_file: reflection-preferences.md`.
4. Inspect the structured result and private proposal/audit metadata locally.

State follows the same sequence with its own confirmation, State target allowlist, and both lifecycle triggers. See [the synthetic walkthrough](../examples/mcp/proposal-approval-workflow.synthetic.md) for approve, reject, defer, expire, refusal, and double-apply cases.

## Denied Behavior

The workflow denies arbitrary or traversing paths, wildcards, directory access, non-allowlisted targets, cross-destination review/apply, triggerless State, silent persistence, bulk apply, double apply, status-as-persistence, whole-vault scans, broad search, generic writes, and raw-content audit logging.

## Future Work

Issue #31 implements the minimal local approval/apply contract. Issue #32 documents ChatGPT connector onboarding and a [synthetic first-run walkthrough](first-run-chatgpt-walkthrough.md). During ChatGPT testing, use the strictest available confirmation setting, do not remember write approvals, and inspect the JSON payload before approving `mark_proposal_status` or `apply_exact_approved_wording`. Client permission review does not replace the exact-wording and destination checks described above.

The [local runtime viewer](local-runtime-viewer.md) can display separate Memory/State proposal statuses, State triggers, and applied metadata. It is read-only: it cannot approve, edit, reject, or apply proposals and does not replace this workflow's exact-wording gates.

Broader runtime and safety evals, audit retention/purge controls, and `v0.3.0` release readiness remain separately reviewed work. Parent sprint #25 remains open.

# Synthetic MCP Proposal Approval Workflow

This is an independently synthetic walkthrough. It contains no real private data and is not connector configuration. It demonstrates no hosted endpoint, tunnel, whole-vault scan, or silent write. Every successful apply follows explicit proposal review, exact wording, destination-specific confirmation, and a fixed target allowlist.

## Memory: Create, Approve, Apply

Create a pending proposal:

```json
{
  "tool": "create_pending_memory_proposal",
  "proposal": "Prefer concise reflection questions when requested.",
  "rationale": "This synthetic preference may remain useful."
}
```

The result returns a generated `memory-proposal-...json` filename. The private proposal is `pending_review`, has no approved wording, and has not changed Memory or State.

Review and approve that exact wording for Memory:

```json
{
  "tool": "mark_proposal_status",
  "destination": "Memory",
  "filename": "memory-proposal-SYNTHETIC.json",
  "status": "approved_for_apply",
  "review_note": "Synthetic review metadata only.",
  "approved_wording": "Prefer concise reflection questions when requested.",
  "approval_confirmation": "I approve this exact wording for Memory"
}
```

Apply it separately:

```json
{
  "tool": "apply_exact_approved_wording",
  "destination": "Memory",
  "filename": "memory-proposal-SYNTHETIC.json",
  "approved_wording": "Prefer concise reflection questions when requested.",
  "target_file": "reflection-preferences.md",
  "approval_confirmation": "I approve this exact wording for Memory",
  "approval_note": "Synthetic apply metadata only."
}
```

The server appends a dated approved-item section, marks the proposal applied, and writes a metadata-only audit record. It does not overwrite existing Memory or touch State.

## State: Create, Approve, Apply

Create temporary State with both lifecycle triggers:

```json
{
  "tool": "create_pending_state_proposal",
  "proposal": "Current synthetic open question: which evening routine is easiest to test?",
  "rationale": "This is useful only during the synthetic trial.",
  "review_or_stale_trigger": "Review at the next weekly check-in.",
  "expiration_trigger": "Expire when the two-week trial ends."
}
```

Approve the exact State wording:

```json
{
  "tool": "mark_proposal_status",
  "destination": "State",
  "filename": "state-proposal-SYNTHETIC.json",
  "status": "approved_for_apply",
  "approved_wording": "Current synthetic open question: which evening routine is easiest to test?",
  "approval_confirmation": "I approve this exact wording for State"
}
```

Apply to an allowlisted State file:

```json
{
  "tool": "apply_exact_approved_wording",
  "destination": "State",
  "filename": "state-proposal-SYNTHETIC.json",
  "approved_wording": "Current synthetic open question: which evening routine is easiest to test?",
  "target_file": "open-questions.md",
  "approval_confirmation": "I approve this exact wording for State"
}
```

The appended State section includes the exact wording, review/stale trigger, and expiration trigger. No Memory file changes.

## Other Review Decisions

Reject a proposal without approved wording:

```json
{"tool":"mark_proposal_status","destination":"Memory","filename":"memory-proposal-REJECT.json","status":"rejected"}
```

Defer a proposal without approved wording:

```json
{"tool":"mark_proposal_status","destination":"Memory","filename":"memory-proposal-DEFER.json","status":"deferred"}
```

Expire a State proposal without approved wording:

```json
{"tool":"mark_proposal_status","destination":"State","filename":"state-proposal-EXPIRE.json","status":"expired"}
```

Memory expiration is refused; use reject, defer, or return to pending review instead.

## Required Refusals

Cross-destination apply is refused. A Memory proposal cannot use `destination: State`, a State target, or the State confirmation phrase. Approval for one destination never transfers to the other.

Wording mismatch is refused. For example, changing `concise` to `brief`, removing punctuation, or adding one trailing space does not match the stored exact wording.

Triggerless State is refused at creation, approval, and apply gates. Both the review/stale trigger and expiration trigger must remain present in the State proposal.

A second apply of an already-applied proposal is refused and does not append another section. An applied proposal also cannot be returned to pending review to bypass that gate.

These examples do not approve any real data. There is no approval without exact wording, no persistence from a status change alone, and no write outside the six destination-specific allowlisted files.

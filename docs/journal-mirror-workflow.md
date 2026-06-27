# Journal Mirror Workflow

The Journal Mirror is a private-first reflection flow that starts after natural writing:

```text
write naturally
→ select context
→ mirror session
→ review reflection
→ propose state update
→ propose memory update
→ approve, edit, or discard
```

State and Memory proposals are independent and optional. The sequence does not imply that either proposal must be produced or approved.

## What the Journal Mirror Does

The Journal Mirror reflects selected writing back in tentative, non-clinical language. It may separate observations from interpretations, identify possible emotions, needs, values, or recurring patterns, ask clarifying questions, and offer small reversible next steps. Claims should remain grounded in the selected context and should state uncertainty when evidence is thin.

## What It Does Not Do

The Journal Mirror does not diagnose, label personality, infer trauma history as fact, provide therapy or crisis counseling, create treatment plans, give medication guidance, or replace licensed care. It does not scan an entire notes system by default, silently retain content, or write Memory or State without review.

When crisis indicators appear, the safety rules in `GUARDRAILS.md` replace the ordinary reflection flow.

## When to Use It

Use a session after writing when a second perspective may help clarify one experience, compare a small set of entries, prepare questions for trusted human support, or identify a possible next step. Do not use it when the user has not chosen the source context or when immediate safety needs should take priority.

## Session Surfaces

- Use `prompts/journal-mirror-session.md` for the complete flow with one entry, excerpt, or small selected group.
- Use `prompts/freeform-entry-mirror.md` when one natural, messy entry should be reflected without a template.
- Use `prompts/recent-pattern-review.md` to compare a small selected set without turning a sample into a fixed trait.
- Use `prompts/gentle-next-action.md` when the user wants one low-pressure, reversible option.
- Use `prompts/update-proposal-review.md` to classify and review a proposed Memory or State update before any manual persistence.

The capability modules in `skills/journal-mirror-session/SKILL.md`, `skills/summarizing-journal-patterns/SKILL.md`, and `skills/memory-state-review/SKILL.md` define the reusable workflows and privacy boundaries behind these surfaces.

Public-safe end-to-end examples are available in `examples/journal-mirror-walkthroughs/`: a freeform entry session, a recent pattern review, and a Memory/State proposal review. They use invented inputs and expected outputs only; real sessions and retained reflections remain private.

## Inputs the User May Provide Manually

- One entry, a short excerpt, or a small group of entries.
- A question or reflection goal.
- Relevant date range or minimal context.
- A preferred response style, such as concise reflection or questions only.
- Explicit constraints on topics, retention, or proposal generation.

Use placeholders in public examples, such as `[selected excerpt]`, `[date]`, or `[user question]`. Real inputs remain in the private runtime/data plane.

## Outputs the Agent May Produce

- A concise reflection that distinguishes user-stated facts from possible interpretations.
- Tentative emotions, needs, values, themes, or thought/action links.
- Questions that invite correction or deeper reflection.
- Small, reversible options or possible next steps.
- A separate proposed State update for temporary session continuity.
- A separate proposed Memory update for durable, user-approved context.

Outputs are suggestions for review, not clinical conclusions or automatic records.

## Memory and State Proposals

State captures fast-changing execution context, such as the current reflection goal, an open question, or a near-term next step. Memory captures durable context likely to remain useful across future sessions, such as an explicitly stated reflection preference. A temporary feeling, one-off event, or unreviewed inferred trait does not become Memory.

Each proposal should identify its destination, concise proposed text, reason, minimal evidence summary, opaque private source reference, uncertainty, safety/privacy checks, and review or deletion expectation. Use the separate `schemas/memory-update-proposal.schema.json` and `schemas/state-update-proposal.schema.json` contracts and follow `docs/memory-state-proposal-review.md`. Proposals remain pending until the user chooses one action:

- Approve the exact proposal.
- Edit it, then approve the edited version.
- Discard it.

Temporary State proposals may also expire when their review, stale, date, or event trigger is reached.

Approval for one proposal does not approve another. State must not silently become Memory, and neither layer should contain a raw journal entry when a minimal summary is sufficient. Approved wording is manually copied into private Memory or State; the schemas do not implement live writes or automatic persistence.

## Why Templates Are Optional

Natural writing should not be forced into an analysis-friendly form. Templates can reduce blank-page friction or support a quick check-in, but the Journal Mirror must work with ordinary prose selected after writing. A template is a user-controlled helper, not an ingestion requirement or a condition for useful reflection.

## How the Flow Stays Private-First

The public repository is the reusable control plane: it contains instructions, policies, prompts, schemas, and synthetic examples. A private Obsidian vault or other private notes system is the runtime/data plane: it contains real writing and any user-approved private records.

The user selects the smallest useful context and supplies it manually. The public repo receives no real journal content, private reflection, filled Memory, live State, vault files, logs, or exports. Future adapters must preserve this boundary and cannot bypass explicit selection or review.

`docs/future-mcp-vps-controller-contract.md` specifies the design-only boundary for a possible private runtime edge. Any future controller must remain user-invoked, operate on explicit narrow scope, and preserve separate proposal and apply approvals; the current repository still provides no live controller or runtime.

## Manual Boundary Checks

Use `evals/journal-mirror-session-cases.md`, `evals/memory-state-proposal-cases.md`, `evals/safety-boundary-cases.md`, and `evals/future-controller-boundary-cases.md` after changing the workflow or future-edge specification. These synthetic checks cover template avoidance, evidence limits, proposal review, staleness, clinical scope, crisis routing, no-vault-access behavior, and controller denials. They test boundaries rather than therapeutic effectiveness.

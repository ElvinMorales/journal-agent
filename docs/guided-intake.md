# Guided Intake

## Purpose

Guided intake helps a new user configure the Journal Mirror from meaningful human context instead of a blank slate. It asks how the user writes, what kind of reflection helps, what is active now, and what boundaries matter. The user answers in plain language; the agent converts only useful, minimal context into draft Memory and State proposals.

The design reduces setup friction while preserving review-based persistence, Memory/State separation, the public-repo/private-data boundary, and user control over exact wording and destination. Intake is configuration, not confession, assessment, or a request for a personal history.

## Place in the v0.3 Sprint

- Issue #26 established the `v0.3.0` MCP runtime direction and architecture boundaries.
- Issue #27 designs the guided intake prompt, manual flow, and initial proposal behavior.
- Issue #28 adds the structured intake schema, synthetic examples, walkthrough, and boundary eval coverage.
- Later MCP issues may let the interaction plane create private pending proposals and apply separately approved wording through a narrow runtime edge.

Issues #27 and #28 add prompt, schema, synthetic example, eval, and documentation artifacts only. They do not implement an MCP server, connector, vault initializer, private storage, runtime configuration, or apply operation. The manual workflow remains usable without MCP.

## What Intake Produces

| Stage | Meaning | Persistence boundary |
|---|---|---|
| Intake answer | Private, user-provided context about use, preferences, boundaries, supports, or the current season | Remains in the private interaction context; it is not automatically retained |
| Candidate Memory proposal | Minimal wording that may remain useful across future sessions | Pending until the user reviews the exact wording and Memory destination |
| Candidate State proposal | Minimal temporary context useful now, with a review/stale trigger and, when known, an expiration trigger | Pending until the user reviews the exact wording, State destination, and trigger |
| Approved Memory | Durable context the user has explicitly approved for private Memory | Added only through a separate manual copy or strict exact-wording apply operation |
| Current State | Temporary context the user has explicitly approved for private State | Added separately and reviewed or expired at its trigger |

An intake answer is evidence for a candidate, not permission to persist it. A candidate proposal is not approved Memory or current State. The model's confidence is not approval. Memory and State remain separate throughout intake, review, and any later apply step.

Structured intake output uses `schemas/intake-response.schema.json` with `status: pending_review`, separate `destination: Memory | State` candidates, and `requires_user_approval: true`. This is a reviewable proposal bundle, not private persistence or an apply operation. Schema validation proves only that the output has the expected shape; it does not mean the user approved any wording or destination. The existing destination-specific Memory and State proposal schemas remain separate.

## Manual Use

```text
open prompts/guided-intake.md
-> answer only comfortable questions
-> receive a draft summary and separate proposals
-> review wording, destination, and State triggers
-> manually copy approved Memory into private Memory
-> manually copy approved State into private State
-> discard or defer the rest
```

Run intake in a private model session. Do not paste the answers, generated proposals, or completed private records into this repository. The user may skip, pause, stop, or answer at a broad category level. Manual copying is a deliberate persistence action; the prompt itself writes nothing.

## MCP Proposal Use

```text
run guided intake in ChatGPT
-> ChatGPT creates separate private pending proposals through MCP
-> user reviews each proposal
-> user approves exact wording and destination
-> user separately invokes apply
-> MCP applies only the approved wording to the named private destination
```

Issue #27 established this design target; issues #30 and #31 implement the local proposal, review, and strict apply subset. Proposal creation, review status, exact-wording approval, destination approval, and apply remain distinct operations. The runtime must not scan a vault, treat intake as blanket consent, bulk apply proposals, or promote State to Memory.

## Question Design Principles

- Ask in plain language about use, tone, boundaries, supports, current context, and preferences.
- Avoid artifact jargon such as “What belongs in your Memory?” or “What is your State?”
- Ask a few related questions at a time and allow correction before continuing.
- Allow every question to be skipped; accept partial answers and uncertainty.
- Ask for broad categories rather than names, workplaces, private histories, or identifying details.
- Avoid intrusive, diagnostic, medical, treatment, or crisis-detail questions.
- Prefer minimal summaries over raw answers.
- Make assumptions, missing context, and model uncertainty visible.
- Propose; do not persist.

### Durable vs Temporary

A likely durable preference may become a Memory candidate when it is useful beyond the current situation, minimally worded, non-clinical, and explicitly approved. Examples include stable response-style preferences or a durable boundary.

Current decisions, transitions, constraints, and open loops belong in State when they are useful now but expected to change. Every State candidate needs a review/stale trigger, plus an expiration date or event when one is known. Intake must not turn one answer into a fixed trait or silently retain temporary context.

## Proposal Review

Use `docs/memory-state-proposal-review.md` and `prompts/update-proposal-review.md` after intake. The user may approve, edit, reclassify, discard, defer, or add an expiration condition. Reclassification requires review of the new destination; edited wording requires review again.

Even when a user says “approve,” the manual intake prompt performs no write. A later runtime may apply a proposal only through a separate operation that receives the exact approved wording and named destination.

## Safety and Privacy

The intake is a non-clinical configuration conversation. It does not request diagnosis, treatment, medication, trauma, crisis, self-harm method, or personal safety-history details. If current crisis indicators appear, ordinary intake stops and the safety routing in `GUARDRAILS.md` takes precedence.

Before publishing intake-related repository changes, confirm:

- [ ] No real intake responses or private journal excerpts.
- [ ] No filled private Memory, live State, or real pending proposals.
- [ ] No diagnoses, treatment plans, medication details, crisis details, or self-harm method details.
- [ ] No employer-specific or identifying information.
- [ ] No local paths, private vault content, secrets, logs, screenshots, or runtime configuration.
- [ ] Any examples are independently synthetic and explicitly labeled.
- [ ] Memory and State remain separate and proposal-only.
- [ ] Every State proposal includes a review/stale/expiration rule.

Private storage is not automatically confidential. Users should evaluate the privacy controls of the model session, notes system, device, sync, backup, and sharing configuration they choose.

## Related Artifacts

- `prompts/guided-intake.md`
- `schemas/intake-response.schema.json`
- `examples/intake/guided-intake.synthetic.json`
- `examples/intake/intake-to-memory-state-proposals.synthetic.md`
- `evals/intake-boundary-cases.md`
- `prompts/update-proposal-review.md`
- `docs/memory-state-proposal-review.md`
- `docs/roadmap-v0.3.0.md`
- `docs/decisions/0003-journal-mirror-mcp-runtime.md`
- `docs/future-mcp-vps-controller-contract.md`
- `GUARDRAILS.md`
- `PRIVACY.md`

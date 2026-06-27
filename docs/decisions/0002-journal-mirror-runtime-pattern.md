# ADR 0002: Journal Mirror Runtime Pattern

## Status

Proposed

## Context

The repository began with prominent journal templates and reflection prompts. Those artifacts are useful, but a template-first start path can imply that users must structure writing for the agent. It also leaves the boundary between the public scaffold, private journal storage, reflection sessions, and durable updates underspecified.

The `v0.2.0` direction needs a file-first pattern that preserves natural private writing, explicit context selection, separate Memory and State, and review before persistence. The agentic AI artifact taxonomy remains the framework-neutral source of truth. Strategic Mirror Agent provides implementation-pattern inspiration only.

## Decision

The public repo remains the reusable control plane. The private Obsidian vault or private notes system is the runtime/data plane. Journal Mirror sessions happen after natural writing. Memory/State updates are proposed and reviewed before application.

The standard flow is:

```text
write naturally
→ select context
→ mirror session
→ review reflection
→ propose State update
→ propose Memory update
→ approve, edit, or discard
```

Templates remain optional helpers. Users manually select one entry, excerpt, or small group of entries. Reflection stays tentative and bounded by `GUARDRAILS.md`. State and Memory proposals remain separate, optional, minimal, and inert until the user reviews the specific proposal and destination. This ADR defines the pattern; it does not implement live writes or runtime access.

## Consequences

- The primary experience supports ordinary prose rather than requiring a journal schema.
- The public scaffold remains useful across Obsidian and other private notes systems.
- The private/public boundary and the user's selection authority become explicit.
- Memory and State classification becomes a visible review decision.
- Follow-up prompts, schemas, walkthroughs, evals, and runtime contracts can share one workflow.
- Manual context selection remains necessary until a separately reviewed adapter design exists.
- The repository does not yet provide a complete runtime or automated persistence.

## Alternatives Considered

### Keep the Template-First Workflow

Rejected for this PR. Templates remain useful, but making them primary constrains natural writing and obscures the post-writing mirror pattern.

### Build MCP Now

Rejected for this PR. An MCP server would add access, authorization, and runtime scope before the manual workflow and approval contract are validated.

### Create an Obsidian Plugin Now

Rejected for this PR. A plugin would introduce a host-specific implementation and broader product scope. The documented workflow should remain notes-system neutral.

### Store Private Entries in GitHub

Rejected. Private writing, reflections, Memory, State, and runtime records do not belong in the public control-plane repository.

### Treat Strategic Mirror as the Taxonomy Source of Truth

Rejected. Strategic Mirror is a working reference pattern. The `agentic-ai-artifact-taxonomy` repository defines the canonical 14 framework-neutral buckets.

## Taxonomy Mapping

This decision uses the original taxonomy without adding categories:

- Prompts and interfaces: manual selection and Journal Mirror invocation surfaces.
- Memory: durable context proposed for explicit user approval.
- State: temporary session context proposed separately from Memory.
- Planning and orchestration: the post-writing reflection and review sequence.
- Guardrails and governance: safety, privacy, consent, and approval gates.
- Outputs and schemas: reflections and future proposal contracts.
- Runtime and deployment: the public control-plane/private-data-plane boundary.
- Learning and iteration: the `v0.2.0` roadmap and follow-up work.

The remaining buckets retain their existing meanings and mappings. MCP, plugins, and host adapters would be implementation-edge mappings, not new taxonomy buckets.

## Public/Private Safety Impact

The public repo may contain only reusable design artifacts, policies, synthetic examples, and validation material. It must not contain real entries or excerpts, generated private reflections, pending proposals from real sessions, filled Memory, live State, private vault files, screenshots, logs, databases, secrets, identifying paths, or employer-specific material.

The private runtime/data plane remains under user control. Selecting context for one session does not authorize broad vault access or retention. Producing a proposal does not authorize a write. Existing non-clinical and crisis guardrails remain mandatory throughout the flow.

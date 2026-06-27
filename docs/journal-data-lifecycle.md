# Journal Data Lifecycle

## 1. Capture

Journal entries are user-authored and should be stored only in ignored private paths or another user-controlled private system.

Capture stays in the private vault or notes system. A Journal Mirror session uses only the entry, excerpt, or small group of entries the user manually selects; it does not imply broad access to the journal.

## 2. Reflection

The companion may generate analysis artifacts from one entry or a selected set of entries. Analysis should remain tentative and evidence-bound.

Private reflections remain in the private data plane unless the user intentionally creates a synthetic, redacted public example. See `docs/obsidian-private-runtime-guide.md` for the manual private-vault flow.

A future controller may handle only the selected session context after a visible user action. It may not expand that selection into a vault search or retain the reflection without separate retention approval.

## 3. Memory

Durable memory requires explicit user approval. Do not infer durable traits from journal content.

Memory and State remain separate. Each proposed update is a private runtime artifact and stays pending until the user reviews its exact wording and destination, then edits, approves, discards, or, for State, lets it expire. Approved wording is manually copied into private Memory or State; State must not be promoted to Memory automatically. Only synthetic proposal fixtures may appear in the public repository. See `docs/memory-state-proposal-review.md`.

The future-controller contract preserves the same sequence: proposal creation, destination-specific review, exact-wording approval, and a separate apply confirmation. A controller may never treat proposal approval as an automatic write or approval for the other destination. See `docs/future-mcp-vps-controller-contract.md`.

## 4. Export

Exports should be redacted by default and should separate user-authored content from agent-generated summaries.

Any future controller-assisted public example requires explicit review of the final synthetic/redacted artifact. Private exports remain outside Git.

## 5. Deletion

Private journal data, summaries, memory, and state should be easy to remove without changing committed repository structure.

Any future implementation must also provide a purge strategy for private audit records and controller-created private artifacts.

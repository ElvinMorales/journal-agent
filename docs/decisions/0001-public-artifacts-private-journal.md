# 0001 - Keep public artifacts separate from private journal content

## Status

Accepted

## Context

`journal-agent` is intended to demonstrate reusable AI-agent artifacts for a journaling companion. Journal content is highly sensitive and may include personal, medical, family, financial, relational, or crisis-related information.

## Decision

The public repository will contain reusable artifacts only: instructions, prompts, schemas, templates, policies, evals, docs, and validation scripts.

Private journal entries, summaries, memory, state, exports, therapy-prep notes, crisis notes, logs, databases, and identifying details must live outside the public repo.

Acceptable private locations include a private Obsidian vault, ignored local folders, or another user-controlled private system.

## Consequences

- The repo can be public and reusable without exposing private journal content.
- Examples must be synthetic.
- Templates may be public, but completed templates are private.
- Memory and state examples may be public, but real memory and state are private.
- Contributors must not include private data in issues, pull requests, logs, screenshots, or examples.

## Related Files

- `README.md`
- `PRIVACY.md`
- `GUARDRAILS.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
- `.gitignore`

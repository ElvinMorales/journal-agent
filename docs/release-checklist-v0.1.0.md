# v0.1.0 Release Checklist

## Positioning

- [x] README describes the repo as a public reference implementation of the Agentic AI Artifact Taxonomy.
- [x] README clearly says this is not therapy.
- [x] README clearly says this is not a mental health product.
- [x] README clearly says this is not a repo for storing private journal entries.

## Taxonomy

- [x] All 14 taxonomy buckets are mapped in `docs/taxonomy-mapping.md`.
- [x] Intentional gaps and future work are documented.
- [x] The taxonomy source-of-truth repo is linked.

## Architecture

- [x] `docs/architecture.md` explains public artifacts vs private user content.
- [x] Architecture doc includes a Mermaid diagram.
- [x] Memory and state are clearly separated.
- [x] Design-time, runtime, and iteration artifacts are distinguished.

## Safety and Privacy

- [x] No real journal entries.
- [x] No private summaries.
- [x] No therapy notes.
- [x] No crisis notes.
- [x] No private memory or state.
- [x] No raw logs, databases, screenshots, or identifying details.
- [x] No secrets or environment files.
- [x] No employer-specific or workplace-specific examples.
- [x] Examples are synthetic-only.
- [x] Synthetic-only audit exists.

## Validation

- [x] `git diff --check` passes locally.
- [x] `python scripts/validate-json-schemas.py` passes locally.
- [x] `git ls-files private` shows only allowed placeholder files.
- [ ] GitHub Actions schema validation passes on the release PR.

## Release

- [x] `CHANGELOG.md` updated.
- [x] Release notes drafted in `docs/release-notes/v0.1.0.md`.
- [x] Issues for post-v0.1.0 work created or documented.
- [ ] Tag `v0.1.0` only after the checklist passes.

## Release Evidence

- Taxonomy reference implementation foundation: PR #2
- Synthetic-only safety audit: PR #8
- Audit note: `docs/synthetic-example-audit.md`

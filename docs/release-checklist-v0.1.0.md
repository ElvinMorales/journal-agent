# v0.1.0 Release Checklist

## Positioning

- [ ] README describes the repo as a public reference implementation of the Agentic AI Artifact Taxonomy.
- [ ] README clearly says this is not therapy.
- [ ] README clearly says this is not a mental health product.
- [ ] README clearly says this is not a repo for storing private journal entries.

## Taxonomy

- [ ] All 14 taxonomy buckets are mapped in `docs/taxonomy-mapping.md`.
- [ ] Intentional gaps and future work are documented.
- [ ] The taxonomy source-of-truth repo is linked.

## Architecture

- [ ] `docs/architecture.md` explains public artifacts vs private user content.
- [ ] Architecture doc includes a Mermaid diagram.
- [ ] Memory and state are clearly separated.
- [ ] Design-time, runtime, and iteration artifacts are distinguished.

## Safety and Privacy

- [ ] No real journal entries.
- [ ] No private summaries.
- [ ] No therapy notes.
- [ ] No crisis notes.
- [ ] No private memory or state.
- [ ] No raw logs, databases, screenshots, or identifying details.
- [ ] No secrets or environment files.
- [ ] No employer-specific or workplace-specific examples.
- [ ] Examples are synthetic-only.

## Validation

- [ ] `git diff --check` passes.
- [ ] `python scripts/validate-json-schemas.py` passes.
- [ ] `git ls-files private` shows only allowed placeholder files, if any.
- [ ] GitHub Actions schema validation passes.

## Release

- [ ] `CHANGELOG.md` updated.
- [ ] Issues for post-v0.1.0 work created or documented.
- [ ] Tag `v0.1.0` only after the checklist passes.

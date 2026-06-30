# v0.3.0 Release Checklist

This checklist records the gate that was required after the release-readiness PR merged and before creating the `v0.3.0` tag or GitHub release. The tag and release were published on June 29, 2026. Use the [final public-safety verification](release-verification/v0.3.0-final-public-safety-verification.md) for issue #46 and later audits. Run checks from updated `main` with synthetic fixtures only; this checklist does not authorize moving a tag or changing a published release.

## 1. Scope Confirmation

- [ ] Parent sprint issues are complete or explicitly deferred with rationale.
- [ ] Issues #27 through #34 are merged into `main`.
- [ ] The issue #35 release-readiness PR is merged before tagging.
- [ ] No unmerged feature branch is expected for `v0.3.0`.
- [ ] The readiness PR created no tag or GitHub release.
- [ ] The release scope contains documentation and validation only; no runtime behavior changed.

## 2. Clean Repository State

```text
git checkout main
git fetch --prune origin
git pull --ff-only origin main
git status --short
git clean -nd
```

Pass criteria: `main` is current; the status output is empty; every dry-run clean entry is understood and excluded from release. Never use the dry-run listing as authorization to delete user work.

## 3. Automated Validation

```text
python scripts/validate-json-schemas.py
python -m unittest tests/test_init_private_vault.py
python -m unittest tests/test_mcp_server_boundaries.py
python -m unittest tests/test_mcp_proposal_apply_workflow.py
python -m unittest tests/test_local_runtime_viewer.py
python -m unittest tests/test_mcp_runtime_safety_regressions.py
python -m unittest discover -s tests
python -m mcp_server.journal_mirror_server --help
python -m viewer.local_runtime_viewer --help
```

Pass criteria: every command exits successfully. Tests use disposable synthetic temporary vaults only. Help commands print usage and exit without starting runtime activity, reading a vault, opening a listener, or writing output.

## 4. Expected Counts

- [ ] Schema validation reports 9 schema files.
- [ ] Initializer suite reports 9 tests.
- [ ] MCP boundary suite reports 19 tests.
- [ ] Proposal/review/apply suite reports 24 tests.
- [ ] Local viewer suite reports 14 tests.
- [ ] Runtime safety regression suite reports 13 tests.
- [ ] Full discovery reports 79 tests.

An unexpected count requires investigation and an intentional documentation update; a passing but narrower suite is not sufficient.

## 5. Safety and Leakage Scans

Run each command against tracked content and manually review every match. Checklist commands, high-level prohibitions, deliberately non-routable examples, and synthetic escaped test strings may match; unsafe content must not.

```text
git grep -n -E "<<<<<<<|=======|>>>>>>>"
git grep -n -i -E "real journal|actual entry|my journal|therapy note|crisis note|diagnosis|medication|password|secret|token|api_key|confidential|proprietary|C:\\Users|/Users/"
git grep -n -i -E "[A-Z]:\\\\Users\\\\[^\\\\]+|/Users/[^/]+|/home/[^/]+"
git grep -n -i -E "runtime-viewer.html|journal-mirror-runtime-viewer.html|viewer-output|local-viewer-output"
git grep -n -i -E "sk-|tunnel_[a-z0-9]{8,}|ngrok-free.app|trycloudflare.com|localhost.run|\.loca\.lt|connector_id|client_secret|refresh_token|access_token"
git grep -n -i -E "http://|https://|script src|<script|analytics|cdn|font" -- tests evals docs examples README.md SECURITY.md PRIVACY.md EVALS.md
git grep -n -i -E "method|means|weapon|dose|dosage|hanging|overdose"
git grep -n -i -E "\.env|sqlite|database|db file|hosted endpoint|connector url|api key|client secret|access token|refresh token" -- tests evals docs examples README.md SECURITY.md PRIVACY.md EVALS.md CHANGELOG.md BACKLOG.md ARTIFACT_MAP.md .gitignore .github
git ls-files
git ls-files private
git ls-files .agents
git clean -nd
```

Confirm:

- [ ] No conflict markers remain.
- [ ] No real journal/private data, identifying path, private endpoint, credential, connector/tunnel material, or employer/workplace-specific example is present.
- [ ] No generated viewer HTML, private vault, screenshot, log, export, database, environment file, or other generated private output is tracked or untracked for release.
- [ ] No active external asset, script, analytics, font, or network dependency was introduced in viewer output or public examples.
- [ ] No self-harm method, dosage, weapon, or procedural detail was added; high-level safety routing remains non-clinical.
- [ ] No generated file was left by tests, help commands, or validation.

## 6. Documentation Review

- [ ] `README.md` points to the v0.3 handoff, runtime docs, release notes, and both validation checklists.
- [ ] Release notes accurately describe what changed since `v0.2.0`.
- [ ] The usable-product handoff provides a safe first-run path.
- [ ] `PRIVACY.md` and `SECURITY.md` accurately state user responsibilities and release constraints.
- [ ] Public control plane and private data plane remain explicit.
- [ ] Memory and State remain separate throughout intake, proposal, review, apply, and display.
- [ ] Exact wording and destination-specific confirmation remain required before apply.
- [ ] Unsupported items and known limitations are listed.
- [ ] No document overclaims production hardening, privacy/confidentiality, security, clinical safety, or therapeutic effectiveness.
- [ ] All changed relative links resolve and all directory/anchor links are checked manually.

## 7. Artifact and Taxonomy Audit

- [ ] `ARTIFACT_MAP.md` contains exactly 14 taxonomy rows.
- [ ] `docs/taxonomy-mapping.md` contains exactly 14 taxonomy rows.
- [ ] Release notes/changelog/backlog map to Learning/iteration and Knowledge/resources as appropriate.
- [ ] Release and runtime checklists map to Evaluation/observability.
- [ ] The usable-product handoff maps to Runtime/deployment, Knowledge/resources, Prompts/interfaces, Memory, State, and Guardrails/governance without adding a bucket.
- [ ] Generic artifact classes remain framework-neutral and framework mappings are intentional.

## 8. GitHub Release Draft Review

- [ ] Title is `v0.3.0 — Journal Mirror MCP Runtime`.
- [ ] The body is derived from the reviewed release notes.
- [ ] It contains no private content, private URLs, local paths, endpoints, or identifying details.
- [ ] It has no screenshots, generated HTML, logs, exports, private runtime artifacts, or other attachments.
- [ ] It makes no “production ready,” guaranteed-private, guaranteed-secure, or clinical-safety-certification claim.
- [ ] It does not imply therapy, medical support, or crisis counseling.

## 9. Tagging Steps

These are the historical tag commands. They were run for `v0.3.0`; do not rerun them. For a future release, equivalent commands remain gated on updated-main validation and explicit release approval:

```text
git tag -a v0.3.0 -m "v0.3.0: Journal Mirror MCP runtime"
git push origin v0.3.0
```

Verify that the tag points to the validated merged `main` commit before publishing the GitHub release.

## 10. Post-Release Cleanup

- [ ] Verify the remote tag and GitHub release body.
- [ ] Close parent sprint #25 only after tag/release verification.
- [ ] Confirm `BACKLOG.md` retains distinct `v0.4` candidates.
- [ ] Keep package/CLI polish, stronger CI, formal threat modeling, private deployment design, richer viewer UX, eval automation, framework mapping, adapter docs, and release automation out of the `v0.3.0` shipped-scope summary.
- [ ] Consider a later public note only after a separate public-safety review; it is not required for this release.

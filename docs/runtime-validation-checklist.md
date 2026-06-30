# Runtime Validation Checklist

Use this checklist for local runtime changes and PR review. For the complete release gate and post-release verification, also use the [v0.3.0 release checklist](release-checklist-v0.3.0.md) and [final public-safety verification](release-verification/v0.3.0-final-public-safety-verification.md). All automated validation must use repository fixtures or disposable temporary synthetic vaults. Never point public validation commands at a real private vault.

The existing GitHub workflow remains focused on schema validation. Issue #34 does not add a second CI workflow or change dependencies; reviewers should run the standard-library unit-test commands below locally until CI expansion is separately reviewed.

## Prerequisites

- Python 3.10 or newer available as `python`.
- Git available from the repository root.
- No dependency installation or network access is required for the test suite.
- A clean understanding of every existing worktree change; do not remove unrelated user work.
- No real vault path, private content, connector configuration, endpoint, or generated viewer output in the repository.

## Automated Checks

Run from the repository root:

```text
git status --short --branch
git diff --check
python scripts/validate-json-schemas.py
python -m unittest tests/test_init_private_vault.py
python -m unittest tests/test_mcp_server_boundaries.py
python -m unittest tests/test_mcp_proposal_apply_workflow.py
python -m unittest tests/test_local_runtime_viewer.py
python -m unittest tests/test_mcp_runtime_safety_regressions.py
python -m unittest discover -s tests
python -m mcp_server.journal_mirror_server --help
python -m viewer.local_runtime_viewer --help
git ls-files private
git ls-files .agents
git clean -nd
```

At issue #34, the stable individual counts are 9 initializer, 19 MCP boundary, 24 proposal/apply, 14 viewer, and 13 runtime safety regression tests. Full discovery reports 79 tests. Update these counts when tests are intentionally added or removed; an unexpected count change requires review. Schema validation reports 9 schema files.

The help commands must exit successfully without starting a server, opening a network listener, reading a vault, or writing output. `git ls-files private` should show only deliberate placeholders. `.agents` must not be tracked. `git clean -nd` is inspection only: review every untracked path and do not delete user work.

## Safety and Leakage Review

Use `git grep` against tracked content and review every match rather than assuming any keyword is automatically unsafe.

```text
git grep -n -E "<<<<<<<|=======|>>>>>>>"
git grep -n -i -E "real journal|actual entry|my journal|therapy note|crisis note|diagnosis|medication|password|secret|token|api_key|confidential|proprietary|C:\\Users|/Users/"
git grep -n -i -E "[A-Z]:\\\\Users\\\\[^\\\\]+|/Users/[^/]+|/home/[^/]+"
git grep -n -i -E "runtime-viewer.html|journal-mirror-runtime-viewer.html|viewer-output|local-viewer-output"
git grep -n -i -E "sk-|tunnel_[a-z0-9]{8,}|ngrok-free.app|trycloudflare.com|localhost.run|\.loca\.lt|connector_id|client_secret|refresh_token|access_token"
git grep -n -i -E "http://|https://|script src|<script|analytics|cdn|font" -- tests evals docs examples README.md SECURITY.md PRIVACY.md EVALS.md
git grep -n -i -E "method|means|weapon|dose|dosage|hanging|overdose"
git grep -n -i -E "\.env|sqlite|database|db file|hosted endpoint|connector url|api key|client secret|access token|refresh token" -- tests evals docs examples README.md SECURITY.md PRIVACY.md EVALS.md CHANGELOG.md BACKLOG.md ARTIFACT_MAP.md .gitignore .github
```

Expected documentation warnings, synthetic escaped injection strings, and the conflict-marker check written in this checklist may match. Reject real private data, identifying paths, credentials, live endpoint/tunnel identifiers, connector configuration, generated HTML, logs, databases, unsafe clinical detail, and active external assets. High-level statements that procedural details are prohibited are acceptable; examples must not contain those details.

Also inspect tracked filenames:

```text
git ls-files
```

There must be no generated viewer HTML, screenshots, runtime logs, private vault files, exports, databases, or environment files. Generated outputs from tests must remain inside temporary directories and disappear after the test run.

## Taxonomy Audit

`ARTIFACT_MAP.md` and `docs/taxonomy-mapping.md` must retain exactly the original 14 buckets. Confirm 14 mapping rows in each table and verify new artifacts are mapped into existing buckets, especially Evaluation/observability, Guardrails/governance, Runtime/deployment, Tools, Prompts/interfaces, Memory, State, and Learning/iteration.

## Failure Interpretation

- Schema failures usually mean a schema/example mismatch; they do not indicate approval or safe persistence.
- Initializer failures usually indicate path-boundary, idempotency, or starter-file regressions.
- MCP boundary failures usually indicate broadened read scope, unsafe path handling, or a silent mutation.
- Proposal/apply failures usually indicate weakened exact-wording, destination, lifecycle-trigger, or repeat-apply gates.
- Viewer failures usually indicate raw-content disclosure, unsafe rendering, path/output broadening, or generated-output behavior.
- Runtime safety regression failures usually indicate an integrated boundary was weakened across reads, proposals, apply, audit, or viewer behavior.
- Help-command failures may indicate import, argument-parser, or packaging regressions; a hanging command may indicate the help path incorrectly started runtime behavior.

Do not “fix” a safety failure by loosening an assertion. Determine whether the implementation or the explicitly reviewed contract should change.

## Staged Scope Review

Only after all checks pass and explicit approval to stage is given:

```text
git diff --cached --name-status
git diff --cached --check
```

Issue #46 is a documentation and final-verification change only. It must not alter runtime behavior or add connector configuration, a hosted endpoint, a tunnel, a local HTTP server, private paths/data, logs, screenshots, generated viewer output, secrets, or clinical procedural detail. Before commit, verify the changed-file scope, rerun every automated command, review every scan match, confirm both taxonomy tables retain 14 rows, and confirm this branch did not create, delete, move, or modify the pre-existing `v0.3.0` tag or GitHub release.

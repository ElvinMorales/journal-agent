# Local Runtime Viewer Boundary Cases

Use synthetic temporary vaults only. Do not run these checks against private journal data for public validation.

| Case | Expected result |
|---|---|
| Default rendering | Raw journal, full Memory/State content, proposal bodies, exact approved wording, session content, and audit notes remain hidden. |
| Memory/State separation | Separate sections and proposal groups remain visible; no cross-destination promotion occurs. |
| State lifecycle | Review/stale and expiration trigger lines/fields are visible. |
| Proposal lifecycle | Status, review status, applied flag, target, and timestamps are visible without wording. |
| Audit boundary | Event and apply metadata are visible; raw content and wording are absent. |
| Malformed JSON | The page shows filename plus `invalid JSON`; stderr contains safe filename metadata only. |
| HTML injection | HTML-like dynamic strings render escaped; no injected script element appears. |
| Repository output | Repository-root and inside-repository output paths are refused. |
| Static page | CSP is restrictive; no JavaScript, external asset, analytics, form, or network reference exists. |
| Git boundary | No generated HTML or temporary private vault is tracked. |

Automated coverage lives in `tests/test_local_runtime_viewer.py`.

# Local Runtime Viewer

## Purpose

The local runtime viewer is a Python standard-library static HTML generator for inspecting one initialized Journal Mirror private vault. It reads a fixed set of runtime paths from an explicit `--vault-root` and writes one HTML file to an explicit private `--output`. It is not a server, connector, hosted dashboard, remote/VPS controller, public export, or replacement for MCP approval gates.

Generated HTML can contain private metadata. Keep it in the private vault or another protected local folder outside this repository. Do not commit it, publish it, or publish screenshots of it.

## Read Boundary

The viewer reads only:

- `Memory/reflection-preferences.md`, `recurring-patterns.md`, and `values-and-supports.md`;
- `State/current-state.md`, `active-themes.md`, and `open-questions.md`;
- JSON files directly under the separate pending Memory and State proposal folders;
- Markdown file metadata directly under `Journal Mirror/Sessions`;
- JSON metadata directly under `Journal Mirror/Audit`; and
- at most 20 KB from any file, bounded further by `--max-items` for folders.

It does not scan or read `Journal/Daily`, `Journal/Freewrites`, `Journal/Weekly`, attachments, arbitrary folders, credentials, environment files, connector/tunnel configuration, or files outside the configured vault. Required runtime folders and files that resolve through links outside the vault are refused or omitted.

## Default Display

Memory and State remain separate. Memory shows allowlisted filenames, presence, sizes, modification times, and headings. State shows the same metadata plus lines containing review/stale or expiration trigger labels. Neither section shows full file content by default.

Pending Memory and State proposals remain separate. The viewer shows status, review status, apply state, timestamps, destination, target, title, and whether exact approved wording exists. State proposal triggers are visible. Proposal bodies and exact approved wording are hidden by default. Sessions show filenames, sizes, and modification times only. Audit records show metadata such as event, timestamp, destination, filenames, content-logged flag, and wording hash/count; notes and wording are hidden by default. Malformed JSON is reported by filename and `invalid JSON` without displaying its content.

## Run a Dry Run

PowerShell:

```powershell
python -m viewer.local_runtime_viewer --vault-root "D:\Private\journal-mirror-vault" --output "D:\Private\journal-mirror-vault\Journal Mirror\Exports\runtime-viewer.html" --dry-run
```

Bash:

```bash
python -m viewer.local_runtime_viewer --vault-root "$HOME/private/journal-mirror-vault" --output "$HOME/private/journal-mirror-vault/Journal Mirror/Exports/runtime-viewer.html" --dry-run
```

Dry-run validates the initialized vault and output boundary, then reports the allowlisted read/write plan without reading runtime files or writing HTML. The output parent must already exist. Both paths must be explicit and absolute; the vault and output must be outside the public repository.

## Generate the HTML

```powershell
python -m viewer.local_runtime_viewer --vault-root "D:\Private\journal-mirror-vault" --output "D:\Private\journal-mirror-vault\Journal Mirror\Exports\runtime-viewer.html"
```

```bash
python -m viewer.local_runtime_viewer --vault-root "$HOME/private/journal-mirror-vault" --output "$HOME/private/journal-mirror-vault/Journal Mirror/Exports/runtime-viewer.html"
```

The generated page has an inline restrictive content security policy, minimal inline CSS, no JavaScript, no external assets, no forms, no analytics, and no network calls. Every dynamic value is escaped before rendering. The page shows only the vault directory's basename as a label, not its absolute path.

Optional flags expose more private content and materially increase privacy risk:

- `--include-memory-content`
- `--include-state-content`
- `--include-proposal-body`
- `--include-audit-details`
- `--include-session-previews`

Use them only when necessary. Included values remain size-limited and HTML-escaped, but the resulting file is more sensitive. `--max-items N` limits each proposal, session, and audit list; the default is 50 and values must be at least 1.

## Storage and Lifecycle

Store the output only in a protected private local folder governed by appropriate operating-system, device, sync, backup, retention, and sharing controls. Local-only does not mean confidential. Delete the HTML when it is no longer needed; regenerate it from the current vault when a fresh snapshot is useful. Never move generated HTML into the repository, attach it to a public issue, or treat a screenshot as a safe redaction.

The viewer is read-only. It does not approve, edit, reject, or apply proposals; change MCP permissions; create an endpoint; or monitor files. Live refresh, remote access, richer retention controls, and broader runtime safety evaluation remain future work.

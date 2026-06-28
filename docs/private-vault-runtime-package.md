# Private Vault Runtime Package

## Purpose

The private vault runtime package is a blank local folder structure for user-controlled Journal Mirror data. The public repository remains the reusable control plane: code, prompts, schemas, tests, documentation, and synthetic examples. The initialized vault is the private data plane and must remain outside this repository and its Git history.

The structure is framework-neutral. It works as ordinary folders and Markdown files in any local notes system; Obsidian is one supported option, not a requirement.

## Run the Initializer

The initializer uses only the Python standard library and requires an explicit absolute `--vault-root` path. Start with a dry run.

PowerShell:

```powershell
python scripts/init-private-vault.py --vault-root "D:\Private\journal-mirror-vault" --dry-run
python scripts/init-private-vault.py --vault-root "D:\Private\journal-mirror-vault"
```

Bash:

```bash
python scripts/init-private-vault.py --vault-root "$HOME/private/journal-mirror-vault" --dry-run
python scripts/init-private-vault.py --vault-root "$HOME/private/journal-mirror-vault"
```

Dry-run prints the planned actions and changes nothing. A normal run creates missing folders and starter files. Existing files are skipped and left unchanged. `--force` overwrites only the fixed generic starter files managed by this initializer; it does not touch other files.

## Created Structure

```text
Journal/
  Daily/
  Freewrites/
  Weekly/
Journal Mirror/
  README.md
  Sessions/
    session-template.md
  Pending Updates/
    memory/README.md
    state/README.md
  Approved Updates/README.md
  Audit/README.md
  Exports/README.md
Memory/
  reflection-preferences.md
  recurring-patterns.md
  values-and-supports.md
State/
  current-state.md
  active-themes.md
  open-questions.md
Attachments/
```

Memory holds only durable, user-approved context. State holds temporary context and includes review, stale, or expiration reminders. Pending Memory and State proposals remain in separate folders and are inert until the user reviews exact wording and destination. The starter files contain headings and generic instructions only; they contain no personal examples or runtime data.

## Safety and Refusals

The initializer:

- Refuses a relative target path.
- Resolves paths with `pathlib` and refuses the public repository root or any path inside it.
- Writes only the fixed folders and generic Markdown starter files under the resolved vault root.
- Does not create journal entries, filled Memory, live State, proposals, content logs, databases, environment files, secrets, connector configuration, endpoints, or runtime output.
- Does not run Git commands, stage generated files, or add them to the repository.
- Exits non-zero for an unsafe path or filesystem error and prints a created, skipped, and refused summary.

The initializer cannot make a storage location confidential. The user remains responsible for device security and the notes system's sync, backup, access, and sharing controls.

## Manual Use Today

1. Write private journal content under `Journal/` or another private location of your choice.
2. Use `Journal Mirror/Sessions/session-template.md` with only deliberately selected context; raw entries are not required.
3. Keep proposed durable updates under `Pending Updates/memory/` and proposed temporary updates under `Pending Updates/state/`.
4. Review every proposal's exact wording and destination. Add a review, stale, or expiration trigger to State items.
5. Manually copy approved wording to the corresponding Memory or State file. Nothing applies automatically.
6. Keep audit notes metadata-only and review/redact exports before sharing.

The manual workflow in `docs/obsidian-private-runtime-guide.md` remains available for users who prefer to create or customize folders without running a script.

## Minimal Local MCP Server

This initializer creates the exact folder structure required by the [minimal local MCP server](mcp-local-server.md). The server still requires the user to pass the initialized vault's explicit absolute path and refuses the public repository root, paths inside it, missing roots, and roots missing required folders.

The issue #30 server permits selected-session and allowlisted Memory/State reads, inert proposal creation, proposal metadata/status updates, and metadata-only private audit entries. It does not configure a connector, create an endpoint or tunnel, grant broad vault access, or apply proposal wording. Exact-wording apply remains disabled until issue #31. Generated vault content remains outside Git.

## Before Committing Public Repository Changes

Review `git status` and the staged diff. Do not commit the generated vault, real journal content, selected excerpts, filled Memory, live State, pending proposals, private exports, logs, databases, screenshots, secrets, credentials, connector configuration, or identifying local paths. Public changes should contain only reusable code, documentation, tests, schemas, and independently synthetic examples.

"""Generate one local static HTML view of allowlisted Journal Mirror runtime state."""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath
from typing import Any, Iterable

from mcp_server.vault_runtime import (
    APPROVED_MEMORY_FILES,
    APPROVED_STATE_FILES,
    MAX_READ_BYTES,
    REPO_ROOT,
    VaultBoundaryError,
    is_within,
    read_text_limited,
    resolve_vault_root,
)


PROPOSAL_FIELDS = (
    "destination", "status", "review_status", "applied", "applied_to",
    "created_at", "updated_at", "reviewed_at", "applied_at", "title",
)
AUDIT_FIELDS = (
    "event_type", "timestamp", "created_at", "destination", "proposal_filename",
    "target_file", "content_logged", "approved_wording_hash",
    "approved_wording_characters", "wording_hash", "wording_count",
)
AUDIT_DETAIL_FIELDS = ("note", "review_note", "apply_note", "details")
TRIGGER_NAMES = ("review_or_stale_trigger", "expiration_trigger")
TRIGGER_MARKERS = (
    "review/stale trigger", "review_or_stale_trigger", "expiration trigger",
    "expiration_trigger",
)
SESSION_PREVIEW_CHARS = 800
DETAIL_CHARS = 1_000


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a local static HTML summary of Journal Mirror runtime state."
    )
    parser.add_argument("--vault-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--include-memory-content", action="store_true")
    parser.add_argument("--include-state-content", action="store_true")
    parser.add_argument("--include-proposal-body", action="store_true")
    parser.add_argument("--include-audit-details", action="store_true")
    parser.add_argument("--include-session-previews", action="store_true")
    parser.add_argument("--max-items", type=int, default=50)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if not 1 <= args.max_items <= 500:
        parser.error("--max-items must be between 1 and 500")
    return args


def _explicit_absolute(path: Path, option: str) -> None:
    raw = os.fspath(path)
    if not path.expanduser().is_absolute() or (os.name == "nt" and not PureWindowsPath(raw).is_absolute()):
        raise VaultBoundaryError(f"{option} must be an explicit absolute path")


def resolve_viewer_paths(
    vault_root: Path, output: Path, repo_root: Path = REPO_ROOT
) -> tuple[Path, Path]:
    """Resolve the initialized vault and one existing-parent output outside Git."""

    _explicit_absolute(vault_root, "vault root")
    root = resolve_vault_root(vault_root, repo_root)
    _explicit_absolute(output, "output")
    public_root = repo_root.resolve(strict=True)
    expanded = output.expanduser()
    if expanded.exists() and expanded.is_dir():
        raise VaultBoundaryError("output must identify one HTML file")
    if expanded.suffix.lower() not in {".html", ".htm"}:
        raise VaultBoundaryError("output must use an .html or .htm filename")
    parent = expanded.parent.resolve(strict=False)
    if not parent.exists() or not parent.is_dir():
        raise VaultBoundaryError("output parent must be an existing directory")
    parent = parent.resolve(strict=True)
    target = (parent / expanded.name).resolve(strict=False)
    if target == public_root or is_within(target, public_root):
        raise VaultBoundaryError("output cannot be the public repository root or inside it")
    if not is_within(target, parent):
        raise VaultBoundaryError("output must resolve inside its explicitly selected parent")
    if target.exists() and not target.is_file():
        raise VaultBoundaryError("output must identify a regular file")
    return root, target


def _inside_regular_file(path: Path, allowed_root: Path) -> Path | None:
    """Return a contained regular file, refusing symlink escapes and special files."""

    try:
        target = path.resolve(strict=True)
        base = allowed_root.resolve(strict=True)
    except OSError:
        return None
    if not is_within(target, base) or not target.is_file():
        return None
    return target


def _timestamp(value: float) -> str:
    return datetime.fromtimestamp(value, timezone.utc).isoformat().replace("+00:00", "Z")


def _file_facts(path: Path | None, filename: str) -> dict[str, Any]:
    if path is None:
        return {"filename": filename, "exists": False, "size": None, "modified_at": None}
    stat = path.stat()
    return {
        "filename": filename,
        "exists": True,
        "size": stat.st_size,
        "modified_at": _timestamp(stat.st_mtime),
    }


def _safe_text(path: Path) -> tuple[str | None, str | None]:
    try:
        return read_text_limited(path, MAX_READ_BYTES), None
    except (OSError, VaultBoundaryError):
        return None, "unreadable or over 20 KB limit"


def _headings(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.lstrip().startswith("#")][:20]


def _triggers(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if any(marker in line.casefold() for marker in TRIGGER_MARKERS)
    ][:20]


def _collect_allowlisted(
    root: Path, directory: str, filenames: frozenset[str], *, state: bool, include_content: bool
) -> list[dict[str, Any]]:
    base = (root / directory).resolve(strict=True)
    records: list[dict[str, Any]] = []
    for filename in sorted(filenames):
        target = _inside_regular_file(base / filename, base)
        item = _file_facts(target, filename)
        if target is not None:
            text, error = _safe_text(target)
            item["error"] = error
            if text is not None:
                item["headings"] = _headings(text)
                if state:
                    item["triggers"] = _triggers(text)
                if include_content:
                    item["content"] = text
        records.append(item)
    return records


def _limited_files(directory: Path, suffix: str, max_items: int) -> list[Path]:
    """List only direct children of an already allowlisted runtime folder."""

    contained: list[Path] = []
    for candidate in directory.iterdir():
        if candidate.suffix.lower() != suffix:
            continue
        target = _inside_regular_file(candidate, directory)
        if target is not None:
            contained.append(target)
    contained.sort(key=lambda item: (item.stat().st_mtime, item.name), reverse=True)
    return contained[:max_items]


def collect_proposal_metadata(
    root: Path, destination: str, max_items: int, include_body: bool
) -> list[dict[str, Any]]:
    directory = (root / "Journal Mirror/Pending Updates" / destination.casefold()).resolve(strict=True)
    records: list[dict[str, Any]] = []
    for target in _limited_files(directory, ".json", max_items):
        item: dict[str, Any] = {"filename": target.name}
        text, error = _safe_text(target)
        if error:
            item.update({"status": "unreadable", "error": error})
            records.append(item)
            continue
        try:
            value = json.loads(text or "")
        except json.JSONDecodeError:
            print(f"Viewer skipped invalid proposal JSON metadata: {target.name}", file=sys.stderr)
            item.update({"status": "invalid JSON", "error": "invalid JSON"})
            records.append(item)
            continue
        if not isinstance(value, dict):
            item.update({"status": "invalid record", "error": "JSON root is not an object"})
            records.append(item)
            continue
        for field in PROPOSAL_FIELDS:
            item[field] = value.get(field)
        item["destination"] = value.get("destination") or destination
        item["has_exact_approved_wording"] = bool(value.get("approved_wording"))
        if destination == "State":
            for field in TRIGGER_NAMES:
                item[field] = value.get(field)
        if include_body:
            item["proposal"] = value.get("proposal")
            item["approved_wording"] = value.get("approved_wording")
        records.append(item)
    return records


def collect_session_metadata(root: Path, max_items: int, include_previews: bool) -> list[dict[str, Any]]:
    directory = (root / "Journal Mirror/Sessions").resolve(strict=True)
    records: list[dict[str, Any]] = []
    for target in _limited_files(directory, ".md", max_items):
        item = _file_facts(target, target.name)
        if include_previews:
            text, error = _safe_text(target)
            item["error"] = error
            if text is not None:
                item["preview"] = text[:SESSION_PREVIEW_CHARS]
        records.append(item)
    return records


def collect_audit_metadata(root: Path, max_items: int, include_details: bool) -> list[dict[str, Any]]:
    directory = (root / "Journal Mirror/Audit").resolve(strict=True)
    records: list[dict[str, Any]] = []
    for target in _limited_files(directory, ".json", max_items):
        item: dict[str, Any] = {"filename": target.name}
        text, error = _safe_text(target)
        if error:
            item["error"] = error
            records.append(item)
            continue
        try:
            value = json.loads(text or "")
        except json.JSONDecodeError:
            print(f"Viewer skipped invalid audit JSON metadata: {target.name}", file=sys.stderr)
            item["error"] = "invalid JSON"
            records.append(item)
            continue
        if not isinstance(value, dict):
            item["error"] = "invalid record"
            records.append(item)
            continue
        for field in AUDIT_FIELDS:
            item[field] = value.get(field)
        if include_details:
            for field in AUDIT_DETAIL_FIELDS:
                value_field = value.get(field)
                if value_field is not None:
                    item[field] = str(value_field)[:DETAIL_CHARS]
        records.append(item)
    return records


def collect_runtime_snapshot(
    root: Path, *, max_items: int = 50, include_memory_content: bool = False,
    include_state_content: bool = False, include_proposal_body: bool = False,
    include_audit_details: bool = False, include_session_previews: bool = False,
) -> dict[str, Any]:
    if not 1 <= max_items <= 500:
        raise VaultBoundaryError("max-items must be between 1 and 500")
    memory = _collect_allowlisted(
        root, "Memory", APPROVED_MEMORY_FILES, state=False, include_content=include_memory_content
    )
    state = _collect_allowlisted(
        root, "State", APPROVED_STATE_FILES, state=True, include_content=include_state_content
    )
    proposals = {
        name: collect_proposal_metadata(root, name, max_items, include_proposal_body)
        for name in ("Memory", "State")
    }
    return {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "vault_label": root.name or "configured private vault",
        "memory": memory,
        "state": state,
        "proposals": proposals,
        "sessions": collect_session_metadata(root, max_items, include_session_previews),
        "audit": collect_audit_metadata(root, max_items, include_audit_details),
        "sensitive_options": any((include_memory_content, include_state_content, include_proposal_body,
                                  include_audit_details, include_session_previews)),
    }


def _e(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        value = "yes" if value else "no"
    return html.escape(str(value), quote=True)


def _dl(item: dict[str, Any], fields: Iterable[str]) -> str:
    values = []
    for field in fields:
        if field in item:
            values.append(f"<dt>{_e(field.replace('_', ' ').title())}</dt><dd>{_e(item[field])}</dd>")
    return "<dl>" + "".join(values) + "</dl>"


def _file_section(title: str, records: list[dict[str, Any]], state: bool = False) -> str:
    cards = []
    for item in records:
        status = "found" if item["exists"] else "missing"
        body = _dl(item, ("filename", "size", "modified_at"))
        body += f"<p class=\"status\">Status: {_e(status)}</p>"
        if item.get("error"):
            body += f"<p class=\"warn\">{_e(item['error'])}</p>"
        if item.get("headings"):
            body += "<h3>Headings</h3><ul>" + "".join(f"<li>{_e(v)}</li>" for v in item["headings"]) + "</ul>"
        if state and item.get("triggers"):
            body += "<h3>Review/stale/expiration triggers</h3><ul>" + "".join(
                f"<li>{_e(v)}</li>" for v in item["triggers"]
            ) + "</ul>"
        if "content" in item:
            body += f"<h3>Explicitly included content</h3><pre>{_e(item['content'])}</pre>"
        cards.append(f"<article>{body}</article>")
    return f"<section><h2>{_e(title)}</h2>{''.join(cards)}</section>"


def _proposal_section(destination: str, records: list[dict[str, Any]]) -> str:
    cards = []
    fields = ("filename",) + PROPOSAL_FIELDS + ("has_exact_approved_wording",)
    for item in records:
        body = _dl(item, fields)
        if item.get("error"):
            body += f"<p class=\"warn\">{_e(item['error'])}</p>"
        if destination == "State":
            body += _dl(item, TRIGGER_NAMES)
        for field in ("proposal", "approved_wording"):
            if field in item and item[field] is not None:
                body += f"<h3>{_e(field.replace('_', ' ').title())}</h3><pre>{_e(item[field])}</pre>"
        cards.append(f"<article>{body}</article>")
    empty = "<p>No matching proposal metadata found.</p>" if not cards else ""
    return f"<section><h2>Pending {destination} proposals</h2>{empty}{''.join(cards)}</section>"


def render_html(snapshot: dict[str, Any]) -> str:
    memory_found = sum(bool(item["exists"]) for item in snapshot["memory"])
    state_found = sum(bool(item["exists"]) for item in snapshot["state"])
    proposal_counts = {
        name: Counter(str(item.get("status") or "unknown") for item in records)
        for name, records in snapshot["proposals"].items()
    }
    warnings = (
        "<p class=\"danger\">Sensitive include options were enabled. Review this file before sharing; "
        "included content may be private.</p>" if snapshot["sensitive_options"] else ""
    )
    summaries = [
        ("Memory files", f"{memory_found} found / {len(snapshot['memory']) - memory_found} missing"),
        ("State files", f"{state_found} found / {len(snapshot['state']) - state_found} missing"),
        ("Memory proposals", ", ".join(f"{k}: {v}" for k, v in sorted(proposal_counts["Memory"].items())) or "none"),
        ("State proposals", ", ".join(f"{k}: {v}" for k, v in sorted(proposal_counts["State"].items())) or "none"),
        ("Recent sessions", str(len(snapshot["sessions"]))),
        ("Audit records", str(len(snapshot["audit"]))),
    ]
    summary_html = "".join(f"<article><h3>{_e(k)}</h3><p>{_e(v)}</p></article>" for k, v in summaries)
    sessions = "".join(
        "<article>" + _dl(item, ("filename", "size", "modified_at"))
        + (f"<h3>Explicitly included preview</h3><pre>{_e(item['preview'])}</pre>" if "preview" in item else "")
        + "</article>" for item in snapshot["sessions"]
    ) or "<p>No session metadata found.</p>"
    audit = "".join(
        "<article>" + _dl(item, ("filename",) + AUDIT_FIELDS + AUDIT_DETAIL_FIELDS)
        + (f"<p class=\"warn\">{_e(item['error'])}</p>" if item.get("error") else "")
        + "</article>" for item in snapshot["audit"]
    ) or "<p>No audit metadata found.</p>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src 'none'; script-src 'none'; base-uri 'none'; form-action 'none'">
<meta name="robots" content="noindex,nofollow,noarchive"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Journal Mirror Local Runtime Viewer</title><style>
:root {{ color-scheme: light dark; font-family: system-ui, sans-serif; }} body {{ max-width: 1100px; margin: auto; padding: 2rem; line-height: 1.45; }}
section {{ margin: 2rem 0; }} article {{ border: 1px solid #7778; border-radius: .5rem; margin: .8rem 0; padding: 1rem; overflow-wrap: anywhere; }}
.summary {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(160px,1fr)); gap: .7rem; }} .summary article {{ margin: 0; }}
.warning,.danger {{ border-left: .35rem solid #b45309; padding: .8rem; background: #f59e0b22; }} .danger {{ border-color: #b91c1c; }}
dt {{ font-weight: 700; }} dd {{ margin: 0 0 .45rem; }} pre {{ white-space: pre-wrap; border: 1px solid #7778; padding: .8rem; }}
</style></head><body>
<header><h1>Journal Mirror Local Runtime Viewer</h1>
<p>Generated: {_e(snapshot['generated_at'])}</p><p>Vault: {_e(snapshot['vault_label'])}</p>
<div class="warning"><strong>Private, local artifact.</strong> This file is generated locally. Do not publish or commit it.<br>Raw journal content is hidden by default.</div>{warnings}</header>
<main><section><h2>Runtime summary</h2><div class="summary">{summary_html}</div></section>
{_file_section('Memory', snapshot['memory'])}
{_file_section('State', snapshot['state'], state=True)}
{_proposal_section('Memory', snapshot['proposals']['Memory'])}
{_proposal_section('State', snapshot['proposals']['State'])}
<section><h2>Recent session metadata</h2>{sessions}</section>
<section><h2>Audit metadata</h2>{audit}</section></main>
<footer><p>For local-only use. Do not commit generated output. See docs/local-runtime-viewer.md.</p>
<p>This viewer reads a fixed runtime allowlist and does not replace Journal Mirror MCP approval gates.</p></footer>
</body></html>"""


def write_html(output: Path, rendered: str) -> None:
    """Write exactly one already-validated output file."""

    output.write_text(rendered, encoding="utf-8", newline="\n")


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root, output = resolve_viewer_paths(args.vault_root, args.output)
        if args.dry_run:
            print(
                "Dry run: validated one initialized private vault. Would read the three "
                "allowlisted Memory files, three allowlisted State files, direct pending "
                "Memory/State proposal JSON, session Markdown metadata, and audit JSON "
                f"metadata (up to {args.max_items} items per list); would write one HTML "
                f"file named {output.name}."
            )
            return 0
        snapshot = collect_runtime_snapshot(
            root, max_items=args.max_items,
            include_memory_content=args.include_memory_content,
            include_state_content=args.include_state_content,
            include_proposal_body=args.include_proposal_body,
            include_audit_details=args.include_audit_details,
            include_session_previews=args.include_session_previews,
        )
        write_html(output, render_html(snapshot))
        print(f"Generated local runtime viewer: {output.name}")
        return 0
    except (OSError, VaultBoundaryError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

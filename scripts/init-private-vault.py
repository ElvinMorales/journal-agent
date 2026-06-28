#!/usr/bin/env python3
"""Initialize a blank, user-controlled Journal Mirror private vault."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent

DIRECTORIES = (
    "Journal/Daily",
    "Journal/Freewrites",
    "Journal/Weekly",
    "Journal Mirror/Sessions",
    "Journal Mirror/Pending Updates/memory",
    "Journal Mirror/Pending Updates/state",
    "Journal Mirror/Approved Updates",
    "Journal Mirror/Audit",
    "Journal Mirror/Exports",
    "Memory",
    "State",
    "Attachments",
)

STARTER_FILES = {
    "Memory/reflection-preferences.md": """# Reflection Preferences

## Purpose

Approved durable reflection preferences go here.

Do not paste raw journal entries, private logs, secrets, crisis notes, therapy notes, or identifying details.

## Approved Items

""",
    "Memory/recurring-patterns.md": """# Recurring Patterns

## Purpose

Small, tentative, user-approved durable patterns go here.

Do not treat patterns as diagnoses or fixed traits. Do not paste raw journal entries or identifying details.

## Approved Items

""",
    "Memory/values-and-supports.md": """# Values and Supports

## Purpose

Approved durable notes about values, preferences, and supports go here.

Do not paste raw journal entries, private logs, secrets, or identifying details.

## Approved Items

""",
    "State/current-state.md": """# Current State

## Purpose

Approved temporary context goes here.

Review regularly. Edit or remove items that are stale, expired, or no longer useful. Do not paste raw journal entries or identifying details.

## Approved Items

""",
    "State/active-themes.md": """# Active Themes

## Purpose

Approved temporary themes go here.

Each item should have a review, stale, or expiration trigger. Remove items that are no longer current.

## Approved Items

""",
    "State/open-questions.md": """# Open Questions

## Purpose

Approved temporary questions go here.

Review each item when its trigger occurs and remove stale or expired items.

## Approved Items

""",
    "Journal Mirror/Sessions/session-template.md": """# Journal Mirror Session

## Selected Context Summary

[Summarize only the minimum context deliberately selected for this session. Raw entries are not required.]

## Reflection Request

[Question or reflection goal.]

## Memory Proposal

[None, or link to a separate pending Memory proposal for exact-wording and destination review.]

## State Proposal

[None, or link to a separate pending State proposal with a review, stale, or expiration trigger.]

## Review Notes

[Record manual review decisions without copying raw journal content.]

## Safety Boundary

This companion supports reflection only. It is not therapy, diagnosis, treatment planning, medication guidance, or crisis counseling.
""",
    "Journal Mirror/Pending Updates/memory/README.md": """# Pending Memory Proposals

Files here are inert proposals, not approved Memory. Review the exact wording and confirm the Memory destination before any manual copy. Approval for State does not approve Memory. Nothing here is applied automatically.
""",
    "Journal Mirror/Pending Updates/state/README.md": """# Pending State Proposals

Files here are inert proposals, not approved State. Review the exact wording, confirm the State destination, and require a review, stale, or expiration trigger before any manual copy. Approval for Memory does not approve State. Nothing here is applied automatically.
""",
    "Journal Mirror/Approved Updates/README.md": """# Approved Updates

Optional records of user-reviewed update decisions may go here. Keep Memory and State decisions separate, and retain only the minimum private context needed.
""",
    "Journal Mirror/Audit/README.md": """# Audit

Store metadata-only audit notes here when useful. Do not store raw journal content, selected excerpts, private reflections, secrets, or identifying details in audit notes.
""",
    "Journal Mirror/Exports/README.md": """# Exports

Exports remain private unless deliberately reviewed and redacted. Use synthetic content for public examples, and never publish private journal content by default.
""",
    "Journal Mirror/README.md": """# Journal Mirror Private Runtime

This folder holds private sessions, inert pending proposals, approved-update records, metadata-only audit notes, and reviewed exports. Nothing is written or approved automatically.

Keep this vault outside the public repository. Protect it through appropriate device, sync, backup, access, and sharing controls.
""",
}


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a blank Journal Mirror private vault outside this repository."
    )
    parser.add_argument(
        "--vault-root",
        required=True,
        type=Path,
        help="Absolute path to the private vault root.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned actions without changing the filesystem.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite only the generic starter files managed by this initializer.",
    )
    return parser.parse_args(argv)


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def resolve_target(raw_target: Path) -> Path:
    expanded = raw_target.expanduser()
    if not expanded.is_absolute():
        raise ValueError("--vault-root must be an explicit absolute path")

    target = expanded.resolve(strict=False)
    repo_root = REPO_ROOT.resolve(strict=True)
    if target == repo_root:
        raise ValueError("target is the public repository root")
    if is_within(target, repo_root):
        raise ValueError("target is inside the public repository")
    return target


def ensure_destination(path: Path, root: Path) -> None:
    resolved = path.resolve(strict=False)
    if resolved != root and not is_within(resolved, root):
        raise OSError(f"refusing path outside vault root: {path}")


def initialize(
    target: Path, dry_run: bool, force: bool, counts: dict[str, int]
) -> None:

    for relative in DIRECTORIES:
        destination = target / relative
        ensure_destination(destination, target)
        if destination.exists():
            if not destination.is_dir():
                raise OSError(f"expected directory but found another file type: {destination}")
            print(f"SKIP directory {destination}")
            counts["skipped"] += 1
        else:
            print(f"{'WOULD CREATE' if dry_run else 'CREATE'} directory {destination}")
            if not dry_run:
                destination.mkdir(parents=True, exist_ok=True)
            counts["created"] += 1

    for relative, content in STARTER_FILES.items():
        destination = target / relative
        ensure_destination(destination, target)
        exists = destination.exists()
        if exists and not destination.is_file():
            raise OSError(f"expected regular file but found another file type: {destination}")
        if exists and not force:
            print(f"SKIP file {destination}")
            counts["skipped"] += 1
            continue

        action = "OVERWRITE" if exists else "CREATE"
        print(f"{'WOULD ' if dry_run else ''}{action} file {destination}")
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding="utf-8", newline="\n")
        counts["created"] += 1


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    counts = {"created": 0, "skipped": 0}
    try:
        target = resolve_target(args.vault_root)
        initialize(target, args.dry_run, args.force, counts)
    except (OSError, ValueError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        print(
            f"Summary: created={counts['created']} skipped={counts['skipped']} refused=1",
            file=sys.stderr,
        )
        return 2

    mode = "dry-run" if args.dry_run else "write"
    print(
        f"Summary: mode={mode} target={target} created={counts['created']} "
        f"skipped={counts['skipped']} refused=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

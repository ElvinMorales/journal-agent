"""Standard-library policy and filesystem boundary for Journal Mirror MCP tools."""

from __future__ import annotations

import json
import os
import re
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_DIRECTORIES = (
    "Journal",
    "Journal Mirror",
    "Journal Mirror/Sessions",
    "Journal Mirror/Pending Updates/memory",
    "Journal Mirror/Pending Updates/state",
    "Journal Mirror/Approved Updates",
    "Journal Mirror/Audit",
    "Memory",
    "State",
)

APPROVED_MEMORY_FILES = frozenset(
    {
        "reflection-preferences.md",
        "recurring-patterns.md",
        "values-and-supports.md",
    }
)
APPROVED_STATE_FILES = frozenset(
    {"current-state.md", "active-themes.md", "open-questions.md"}
)
ALLOWED_STATUSES = frozenset(
    {"pending_review", "approved_for_apply", "rejected", "deferred"}
)

MAX_READ_BYTES = 20 * 1024
MAX_PROPOSAL_CHARS = 4_000
MAX_RATIONALE_CHARS = 2_000
MAX_SUMMARY_CHARS = 1_000
MAX_REVIEW_NOTE_CHARS = 500
MAX_AUDIT_NOTE_CHARS = 300

_WILDCARDS = re.compile(r"[*?\[\]{}]")
_SAFE_EVENT = re.compile(r"^[a-z][a-z0-9_-]{1,63}$")
_SECRET_PATTERN = re.compile(
    r"(?i)(?:password|passwd|api[_ -]?key|access[_ -]?token|refresh[_ -]?token|"
    r"client[_ -]?secret)\s*[:=]|bearer\s+[a-z0-9._~-]{12,}|-----BEGIN [A-Z ]+PRIVATE KEY-----"
)


class VaultBoundaryError(ValueError):
    """A request crossed a configured Journal Mirror boundary."""


def tool_ok(**payload: Any) -> dict[str, Any]:
    """Return a consistent successful tool result."""

    return {"ok": True, **payload}


def tool_error(code: str, message: str) -> dict[str, Any]:
    """Return a consistent error without echoing private input."""

    return {"ok": False, "error": {"code": code, "message": message}}


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def resolve_vault_root(raw_root: str | os.PathLike[str], repo_root: Path = REPO_ROOT) -> Path:
    """Validate an existing initialized vault outside the public repository."""

    raw_text = os.fspath(raw_root)
    expanded = Path(raw_text).expanduser()
    if not expanded.is_absolute() or not PureWindowsPath(raw_text).is_absolute() and os.name == "nt":
        raise VaultBoundaryError("vault root must be an explicit absolute path")

    root = expanded.resolve(strict=False)
    public_root = repo_root.resolve(strict=True)
    if root == public_root:
        raise VaultBoundaryError("vault root cannot be the public repository root")
    if is_within(root, public_root):
        raise VaultBoundaryError("vault root cannot be inside the public repository")
    if not root.exists() or not root.is_dir():
        raise VaultBoundaryError("vault root must be an existing directory")

    missing = [relative for relative in REQUIRED_DIRECTORIES if not (root / relative).is_dir()]
    if missing:
        raise VaultBoundaryError(
            "vault is not initialized; run scripts/init-private-vault.py first "
            f"(missing required folders: {', '.join(missing)})"
        )
    escaped = [
        relative
        for relative in REQUIRED_DIRECTORIES
        if not is_within((root / relative).resolve(strict=True), root)
    ]
    if escaped:
        raise VaultBoundaryError("required vault folders must resolve inside the vault root")
    return root


def validate_relative_file_path(relative_path: str) -> PurePosixPath:
    """Reject ambiguous, absolute, traversing, or broad path requests."""

    if not isinstance(relative_path, str) or not relative_path.strip():
        raise VaultBoundaryError("a specific relative file path is required")
    if relative_path != relative_path.strip():
        raise VaultBoundaryError("path must not contain leading or trailing whitespace")
    if _WILDCARDS.search(relative_path):
        raise VaultBoundaryError("wildcards and glob patterns are not allowed")
    if PureWindowsPath(relative_path).is_absolute() or PurePosixPath(relative_path).is_absolute():
        raise VaultBoundaryError("absolute paths are not allowed")

    normalized = relative_path.replace("\\", "/")
    candidate = PurePosixPath(normalized)
    if any(part in {"", ".", ".."} for part in candidate.parts):
        raise VaultBoundaryError("path traversal and ambiguous path segments are not allowed")
    return candidate


def safe_join(base: Path, relative_path: str, *, require_file: bool = False) -> Path:
    """Join one validated relative path beneath a designated directory."""

    relative = validate_relative_file_path(relative_path)
    base_resolved = base.resolve(strict=True)
    target = base_resolved.joinpath(*relative.parts).resolve(strict=False)
    if not is_within(target, base_resolved):
        raise VaultBoundaryError("path escapes the allowed directory")
    if require_file:
        if not target.exists():
            raise VaultBoundaryError("requested file does not exist")
        if not target.is_file():
            raise VaultBoundaryError("directory reads are not allowed")
    return target


def read_text_limited(path: Path, max_bytes: int = MAX_READ_BYTES) -> str:
    """Read one UTF-8 file without returning over-limit content."""

    if not path.is_file():
        raise VaultBoundaryError("requested path is not a regular file")
    if path.stat().st_size > max_bytes:
        raise VaultBoundaryError("requested file exceeds the read size limit")
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise VaultBoundaryError("requested file is not valid UTF-8 text") from exc


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_filename(prefix: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return f"{prefix}-{stamp}-{uuid.uuid4().hex[:8]}.json"


def _validate_text(
    value: str,
    field: str,
    max_chars: int,
    *,
    required: bool = True,
    max_lines: int | None = None,
) -> str:
    if not isinstance(value, str):
        raise VaultBoundaryError(f"{field} must be text")
    cleaned = value.strip()
    if required and not cleaned:
        raise VaultBoundaryError(f"{field} is required")
    if len(cleaned) > max_chars:
        raise VaultBoundaryError(f"{field} exceeds its size limit")
    if max_lines is not None and len(cleaned.splitlines()) > max_lines:
        raise VaultBoundaryError(f"{field} resembles a raw content dump")
    if cleaned and _SECRET_PATTERN.search(cleaned):
        raise VaultBoundaryError(f"{field} appears to contain a secret or credential")
    return cleaned


def _atomic_json_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=False, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


class VaultRuntime:
    """Narrow operations for one validated private Journal Mirror vault."""

    def __init__(self, vault_root: str | os.PathLike[str], repo_root: Path = REPO_ROOT):
        self.root = resolve_vault_root(vault_root, repo_root)
        self.sessions = self.root / "Journal Mirror/Sessions"
        self.pending_memory = self.root / "Journal Mirror/Pending Updates/memory"
        self.pending_state = self.root / "Journal Mirror/Pending Updates/state"
        self.audit = self.root / "Journal Mirror/Audit"
        self.memory = self.root / "Memory"
        self.state = self.root / "State"

    @staticmethod
    def _run(operation: Any) -> dict[str, Any]:
        try:
            return operation()
        except (OSError, VaultBoundaryError, json.JSONDecodeError):
            return tool_error("boundary_refused", "Request refused by the private-vault boundary.")

    def read_selected_session_context(self, relative_path: str) -> dict[str, Any]:
        def operation() -> dict[str, Any]:
            target = safe_join(self.sessions, relative_path, require_file=True)
            return tool_ok(relative_path=relative_path, content=read_text_limited(target))

        return self._run(operation)

    def _read_allowlisted(self, directory: Path, filename: str, allowed: frozenset[str]) -> dict[str, Any]:
        def operation() -> dict[str, Any]:
            if filename not in allowed:
                raise VaultBoundaryError("file is not allowlisted")
            target = safe_join(directory, filename, require_file=True)
            return tool_ok(filename=filename, content=read_text_limited(target))

        return self._run(operation)

    def read_approved_memory(self, memory_file: str) -> dict[str, Any]:
        return self._read_allowlisted(self.memory, memory_file, APPROVED_MEMORY_FILES)

    def read_current_state(self, state_file: str) -> dict[str, Any]:
        return self._read_allowlisted(self.state, state_file, APPROVED_STATE_FILES)

    def _create_proposal(
        self,
        destination: str,
        proposal: str,
        rationale: str,
        source_summary: str,
        review_note: str,
        *,
        review_or_stale_trigger: str | None = None,
        expiration_trigger: str | None = None,
    ) -> dict[str, Any]:
        proposal = _validate_text(
            proposal, "proposal", MAX_PROPOSAL_CHARS, max_lines=40
        )
        rationale = _validate_text(rationale, "rationale", MAX_RATIONALE_CHARS, max_lines=20)
        source_summary = _validate_text(
            source_summary, "source_summary", MAX_SUMMARY_CHARS, required=False, max_lines=10
        )
        review_note = _validate_text(
            review_note, "review_note", MAX_REVIEW_NOTE_CHARS, required=False, max_lines=6
        )
        if destination == "State":
            review_or_stale_trigger = _validate_text(
                review_or_stale_trigger or "",
                "review_or_stale_trigger",
                MAX_REVIEW_NOTE_CHARS,
                max_lines=4,
            )
            expiration_trigger = _validate_text(
                expiration_trigger or "",
                "expiration_trigger",
                MAX_REVIEW_NOTE_CHARS,
                max_lines=4,
            )

        now = _utc_now()
        slug = "memory-proposal" if destination == "Memory" else "state-proposal"
        directory = self.pending_memory if destination == "Memory" else self.pending_state
        filename = _safe_filename(slug)
        target = safe_join(directory, filename)
        record: dict[str, Any] = {
            "artifact_type": "journal_mirror_pending_proposal",
            "title": f"Pending {destination} proposal",
            "destination": destination,
            "status": "pending_review",
            "created_at": now,
            "updated_at": now,
            "requires_user_approval": True,
            "inert": True,
            "applied": False,
            "notice": "Inert proposal only. It has not been applied to Memory or State.",
            "proposal": proposal,
            "rationale": rationale,
            "source_summary": source_summary,
            "review_note": review_note,
        }
        if destination == "State":
            record["review_or_stale_trigger"] = review_or_stale_trigger
            record["expiration_trigger"] = expiration_trigger
        _atomic_json_write(target, record)
        return tool_ok(
            filename=filename,
            destination=destination,
            status="pending_review",
            applied=False,
            message="Pending proposal created; no Memory or State content was changed.",
        )

    def create_pending_memory_proposal(
        self,
        proposal: str,
        rationale: str,
        source_summary: str = "",
        review_note: str = "",
    ) -> dict[str, Any]:
        return self._run(
            lambda: self._create_proposal(
                "Memory", proposal, rationale, source_summary, review_note
            )
        )

    def create_pending_state_proposal(
        self,
        proposal: str,
        rationale: str,
        review_or_stale_trigger: str,
        expiration_trigger: str,
        source_summary: str = "",
        review_note: str = "",
    ) -> dict[str, Any]:
        return self._run(
            lambda: self._create_proposal(
                "State",
                proposal,
                rationale,
                source_summary,
                review_note,
                review_or_stale_trigger=review_or_stale_trigger,
                expiration_trigger=expiration_trigger,
            )
        )

    def list_pending_proposal_metadata(self, destination: str = "all") -> dict[str, Any]:
        def operation() -> dict[str, Any]:
            normalized = destination.strip().lower()
            if normalized not in {"memory", "state", "all"}:
                raise VaultBoundaryError("destination must be Memory, State, or all")
            groups: dict[str, list[dict[str, Any]]] = {"Memory": [], "State": []}
            selected = []
            if normalized in {"memory", "all"}:
                selected.append(("Memory", self.pending_memory))
            if normalized in {"state", "all"}:
                selected.append(("State", self.pending_state))
            for label, directory in selected:
                for candidate in sorted(directory.glob("*.json")):
                    if not candidate.is_file():
                        continue
                    target = safe_join(directory, candidate.name, require_file=True)
                    if target.stat().st_size > MAX_READ_BYTES:
                        continue
                    record = json.loads(read_text_limited(target))
                    if (
                        not isinstance(record, dict)
                        or record.get("artifact_type") != "journal_mirror_pending_proposal"
                        or record.get("destination") != label
                    ):
                        continue
                    groups[label].append(
                        {
                            "filename": target.name,
                            "destination": label,
                            "status": record.get("status", "unknown"),
                            "created_at": record.get("created_at"),
                            "title": f"Pending {label} proposal",
                        }
                    )
            return tool_ok(proposals=groups)

        return self._run(operation)

    def mark_proposal_status(
        self,
        destination: str,
        filename: str,
        status: str,
        review_note: str = "",
    ) -> dict[str, Any]:
        def operation() -> dict[str, Any]:
            if destination not in {"Memory", "State"}:
                raise VaultBoundaryError("destination must be Memory or State")
            if status not in ALLOWED_STATUSES:
                raise VaultBoundaryError("unsupported proposal status")
            if not filename.endswith(".json"):
                raise VaultBoundaryError("proposal filename must identify one JSON proposal")
            note = _validate_text(
                review_note,
                "review_note",
                MAX_REVIEW_NOTE_CHARS,
                required=False,
                max_lines=6,
            )
            directory = self.pending_memory if destination == "Memory" else self.pending_state
            target = safe_join(directory, filename, require_file=True)
            record = json.loads(read_text_limited(target))
            if (
                not isinstance(record, dict)
                or record.get("artifact_type") != "journal_mirror_pending_proposal"
                or record.get("destination") != destination
            ):
                raise VaultBoundaryError("proposal destination does not match request")
            record["status"] = status
            record["updated_at"] = _utc_now()
            record["review_note"] = note
            record["applied"] = False
            record["status_notice"] = "Status only; this proposal has not been applied."
            _atomic_json_write(target, record)
            return tool_ok(
                filename=filename,
                destination=destination,
                status=status,
                applied=False,
                message="Proposal status updated; no Memory or State content was changed.",
            )

        return self._run(operation)

    def apply_exact_approved_wording(
        self,
        destination: str,
        approved_wording: str,
        target_file: str,
        approval_note: str = "",
    ) -> dict[str, Any]:
        del destination, approved_wording, target_file, approval_note
        return tool_error(
            "apply_not_implemented",
            "Exact-wording apply is intentionally disabled in issue #30 and reserved for issue #31. No files were changed.",
        )

    def write_private_audit_entry(
        self,
        event_type: str,
        destination: str = "none",
        proposal_filename: str = "",
        note: str = "",
    ) -> dict[str, Any]:
        def operation() -> dict[str, Any]:
            if not isinstance(event_type, str) or not _SAFE_EVENT.fullmatch(event_type):
                raise VaultBoundaryError("event_type must be a short metadata identifier")
            if destination not in {"Memory", "State", "none"}:
                raise VaultBoundaryError("destination must be Memory, State, or none")
            if proposal_filename:
                relative = validate_relative_file_path(proposal_filename)
                if len(relative.parts) != 1 or not proposal_filename.endswith(".json"):
                    raise VaultBoundaryError("proposal_filename must be one filename")
            safe_note = _validate_text(
                note,
                "note",
                MAX_AUDIT_NOTE_CHARS,
                required=False,
                max_lines=4,
            )
            filename = _safe_filename("audit")
            target = safe_join(self.audit, filename)
            record = {
                "artifact_type": "journal_mirror_private_audit_metadata",
                "timestamp": _utc_now(),
                "event_type": event_type,
                "destination": destination,
                "proposal_filename": proposal_filename,
                "note": safe_note,
                "content_logged": False,
                "notice": "Private, user-controlled metadata only; no journal or proposal body is stored.",
            }
            _atomic_json_write(target, record)
            return tool_ok(filename=filename, metadata_only=True)

        return self._run(operation)

"""Synthetic boundary tests for the minimal local Journal Mirror MCP server."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from mcp_server.vault_runtime import (
    APPROVED_MEMORY_FILES,
    APPROVED_STATE_FILES,
    REQUIRED_DIRECTORIES,
    VaultBoundaryError,
    VaultRuntime,
    resolve_vault_root,
    safe_join,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class MCPServerBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.vault = Path(self.temporary.name) / "synthetic-vault"
        for relative in REQUIRED_DIRECTORIES:
            (self.vault / relative).mkdir(parents=True, exist_ok=True)
        for filename in APPROVED_MEMORY_FILES:
            (self.vault / "Memory" / filename).write_text(
                f"# Synthetic {filename}\n\nApproved synthetic context.\n", encoding="utf-8"
            )
        for filename in APPROVED_STATE_FILES:
            (self.vault / "State" / filename).write_text(
                f"# Synthetic {filename}\n\nTemporary synthetic context.\n", encoding="utf-8"
            )
        (self.vault / "Journal Mirror/Sessions/selected-session.md").write_text(
            "# Synthetic selected session\n\nA deliberately selected test fragment.\n",
            encoding="utf-8",
        )
        self.runtime = VaultRuntime(self.vault)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def snapshot_files(self, relative: str) -> dict[str, str]:
        root = self.vault / relative
        return {
            path.relative_to(root).as_posix(): path.read_text(encoding="utf-8")
            for path in root.iterdir()
            if path.is_file()
        }

    def test_vault_root_equal_to_repo_root_is_refused(self) -> None:
        with self.assertRaisesRegex(VaultBoundaryError, "public repository root"):
            resolve_vault_root(REPO_ROOT)

    def test_vault_root_inside_repo_is_refused(self) -> None:
        with self.assertRaisesRegex(VaultBoundaryError, "inside the public repository"):
            resolve_vault_root(REPO_ROOT / "private-test-vault")

    def test_relative_vault_root_is_refused(self) -> None:
        with self.assertRaisesRegex(VaultBoundaryError, "absolute path"):
            resolve_vault_root("synthetic-vault")

    def test_missing_and_uninitialized_vault_roots_are_refused(self) -> None:
        with self.assertRaisesRegex(VaultBoundaryError, "existing directory"):
            resolve_vault_root(Path(self.temporary.name) / "missing")
        uninitialized = Path(self.temporary.name) / "uninitialized"
        uninitialized.mkdir()
        with self.assertRaisesRegex(VaultBoundaryError, "not initialized"):
            resolve_vault_root(uninitialized)

    def test_safe_join_rejects_absolute_traversal_and_wildcards(self) -> None:
        base = self.vault / "Journal Mirror/Sessions"
        for unsafe in (str(base / "selected-session.md"), "../Memory/a.md", "*.md", "[a].md"):
            with self.subTest(unsafe=unsafe):
                with self.assertRaises(VaultBoundaryError):
                    safe_join(base, unsafe)

    def test_selected_session_reads_only_one_explicit_file(self) -> None:
        result = self.runtime.read_selected_session_context("selected-session.md")
        self.assertTrue(result["ok"])
        self.assertIn("deliberately selected test fragment", result["content"])
        for unsafe in (".", "../Journal", "../Memory/reflection-preferences.md", "../State/current-state.md"):
            with self.subTest(unsafe=unsafe):
                self.assertFalse(self.runtime.read_selected_session_context(unsafe)["ok"])

    def test_selected_session_rejects_directories_and_oversized_files(self) -> None:
        self.assertFalse(self.runtime.read_selected_session_context(".")["ok"])
        oversized = self.vault / "Journal Mirror/Sessions/oversized.md"
        oversized.write_text("x" * (20 * 1024 + 1), encoding="utf-8")
        self.assertFalse(self.runtime.read_selected_session_context(oversized.name)["ok"])

    def test_memory_read_uses_exact_allowlist_and_cannot_read_state(self) -> None:
        self.assertTrue(self.runtime.read_approved_memory("reflection-preferences.md")["ok"])
        self.assertFalse(self.runtime.read_approved_memory("current-state.md")["ok"])
        self.assertFalse(self.runtime.read_approved_memory("../State/current-state.md")["ok"])

    def test_state_read_uses_exact_allowlist_and_cannot_read_memory(self) -> None:
        self.assertTrue(self.runtime.read_current_state("current-state.md")["ok"])
        self.assertFalse(self.runtime.read_current_state("reflection-preferences.md")["ok"])
        self.assertFalse(self.runtime.read_current_state("../Memory/reflection-preferences.md")["ok"])

    def test_pending_memory_proposal_writes_only_pending_memory(self) -> None:
        memory_before = self.snapshot_files("Memory")
        state_before = self.snapshot_files("State")
        result = self.runtime.create_pending_memory_proposal(
            "Use brief questions when requested.", "This may remain useful."
        )
        self.assertTrue(result["ok"])
        target = self.vault / "Journal Mirror/Pending Updates/memory" / result["filename"]
        record = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(record["destination"], "Memory")
        self.assertEqual(record["status"], "pending_review")
        self.assertTrue(record["requires_user_approval"])
        self.assertTrue(record["inert"])
        self.assertFalse(record["applied"])
        self.assertEqual(self.snapshot_files("Memory"), memory_before)
        self.assertEqual(self.snapshot_files("State"), state_before)
        self.assertEqual(list((self.vault / "Journal Mirror/Pending Updates/state").glob("*.json")), [])

    def test_pending_state_proposal_requires_both_triggers_and_stays_separate(self) -> None:
        for review_trigger, expiration_trigger in (("", "next month"), ("next review", "")):
            with self.subTest(review_trigger=review_trigger, expiration_trigger=expiration_trigger):
                result = self.runtime.create_pending_state_proposal(
                    "A temporary synthetic theme.",
                    "It is relevant now.",
                    review_trigger,
                    expiration_trigger,
                )
                self.assertFalse(result["ok"])
        state_before = self.snapshot_files("State")
        result = self.runtime.create_pending_state_proposal(
            "A temporary synthetic theme.",
            "It is relevant now.",
            "Review at the next weekly check-in.",
            "Expire after the current project milestone.",
        )
        self.assertTrue(result["ok"])
        target = self.vault / "Journal Mirror/Pending Updates/state" / result["filename"]
        record = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(record["destination"], "State")
        self.assertTrue(record["review_or_stale_trigger"])
        self.assertTrue(record["expiration_trigger"])
        self.assertEqual(self.snapshot_files("State"), state_before)
        self.assertEqual(list((self.vault / "Journal Mirror/Pending Updates/memory").glob("*.json")), [])

    def test_proposal_creation_rejects_empty_dump_sized_and_secret_content(self) -> None:
        self.assertFalse(self.runtime.create_pending_memory_proposal("", "reason")["ok"])
        self.assertFalse(
            self.runtime.create_pending_memory_proposal("line\n" * 41, "reason")["ok"]
        )
        self.assertFalse(
            self.runtime.create_pending_memory_proposal("short", "password=synthetic-value")["ok"]
        )

    def test_metadata_listing_excludes_proposal_body_and_separates_destinations(self) -> None:
        secret_body = "This exact proposal body must not be listed."
        created = self.runtime.create_pending_memory_proposal(secret_body, "Synthetic rationale")
        self.assertTrue(created["ok"])
        listed = self.runtime.list_pending_proposal_metadata("all")
        self.assertTrue(listed["ok"])
        serialized = json.dumps(listed)
        self.assertNotIn(secret_body, serialized)
        self.assertEqual(len(listed["proposals"]["Memory"]), 1)
        self.assertEqual(listed["proposals"]["State"], [])

    def test_mark_status_updates_only_metadata_and_never_memory_or_state(self) -> None:
        created = self.runtime.create_pending_memory_proposal("Minimal wording.", "Reason.")
        filename = created["filename"]
        target = self.vault / "Journal Mirror/Pending Updates/memory" / filename
        proposal_before = json.loads(target.read_text(encoding="utf-8"))["proposal"]
        memory_before = self.snapshot_files("Memory")
        state_before = self.snapshot_files("State")
        result = self.runtime.mark_proposal_status(
            "Memory", filename, "approved_for_apply", "Reviewed synthetic metadata."
        )
        self.assertTrue(result["ok"])
        self.assertFalse(result["applied"])
        record = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(record["proposal"], proposal_before)
        self.assertEqual(record["status"], "approved_for_apply")
        self.assertFalse(record["applied"])
        self.assertEqual(self.snapshot_files("Memory"), memory_before)
        self.assertEqual(self.snapshot_files("State"), state_before)

    def test_mark_status_rejects_cross_destination_and_unsafe_filename(self) -> None:
        created = self.runtime.create_pending_memory_proposal("Minimal wording.", "Reason.")
        self.assertFalse(
            self.runtime.mark_proposal_status("State", created["filename"], "rejected")["ok"]
        )
        self.assertFalse(
            self.runtime.mark_proposal_status("Memory", "../proposal.json", "rejected")["ok"]
        )

    def test_apply_exact_approved_wording_is_a_noop_refusal(self) -> None:
        before = self.snapshot_files("Memory"), self.snapshot_files("State")
        result = self.runtime.apply_exact_approved_wording(
            "Memory", "Approved synthetic wording.", "reflection-preferences.md", "Approved."
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["error"]["code"], "apply_not_implemented")
        self.assertEqual((self.snapshot_files("Memory"), self.snapshot_files("State")), before)

    def test_audit_entry_is_metadata_only_and_rejects_raw_sized_notes(self) -> None:
        result = self.runtime.write_private_audit_entry(
            "proposal_status_changed", "Memory", "memory-proposal-test.json", "Reviewed."
        )
        self.assertTrue(result["ok"])
        target = self.vault / "Journal Mirror/Audit" / result["filename"]
        record = json.loads(target.read_text(encoding="utf-8"))
        self.assertTrue(result["metadata_only"])
        self.assertFalse(record["content_logged"])
        self.assertNotIn("proposal", record.keys() - {"proposal_filename"})
        refused = self.runtime.write_private_audit_entry("event_recorded", note="line\n" * 5)
        self.assertFalse(refused["ok"])

    def test_audit_rejects_secret_patterns_and_path_like_proposal_names(self) -> None:
        self.assertFalse(
            self.runtime.write_private_audit_entry("event_recorded", note="api_key=synthetic-value")["ok"]
        )
        self.assertFalse(
            self.runtime.write_private_audit_entry(
                "event_recorded", proposal_filename="../memory/proposal.json"
            )["ok"]
        )

    def test_runtime_creates_no_forbidden_artifact_types(self) -> None:
        self.runtime.create_pending_memory_proposal("Minimal wording.", "Reason.")
        self.runtime.create_pending_state_proposal(
            "Temporary wording.", "Reason.", "Review next week.", "Expire next month."
        )
        self.runtime.write_private_audit_entry("synthetic_event")
        files = [path for path in self.vault.rglob("*") if path.is_file()]
        forbidden_suffixes = {".env", ".log", ".db", ".sqlite", ".sqlite3"}
        forbidden_parts = {"connector", "token", "endpoint", "database"}
        self.assertFalse(any(path.suffix.lower() in forbidden_suffixes for path in files))
        self.assertFalse(
            any(part in path.name.lower() for path in files for part in forbidden_parts)
        )


if __name__ == "__main__":
    unittest.main()

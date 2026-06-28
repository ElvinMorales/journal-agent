"""Synthetic tests for proposal review and exact-approved-wording apply."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from mcp_server.vault_runtime import (
    APPROVAL_CONFIRMATIONS,
    APPROVED_MEMORY_FILES,
    APPROVED_STATE_FILES,
    REQUIRED_DIRECTORIES,
    VaultRuntime,
)


class MCPProposalApplyWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.vault = Path(self.temporary.name) / "synthetic-vault"
        for relative in REQUIRED_DIRECTORIES:
            (self.vault / relative).mkdir(parents=True, exist_ok=True)
        for filename in APPROVED_MEMORY_FILES:
            (self.vault / "Memory" / filename).write_text(
                f"# Synthetic {filename}\n\nExisting Memory content.\n", encoding="utf-8"
            )
        for filename in APPROVED_STATE_FILES:
            (self.vault / "State" / filename).write_text(
                f"# Synthetic {filename}\n\nExisting State content.\n", encoding="utf-8"
            )
        self.runtime = VaultRuntime(self.vault)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def snapshot(self, destination: str) -> dict[str, str]:
        return {
            path.name: path.read_text(encoding="utf-8")
            for path in (self.vault / destination).iterdir()
            if path.is_file()
        }

    def proposal_path(self, destination: str, filename: str) -> Path:
        folder = destination.lower()
        return self.vault / "Journal Mirror/Pending Updates" / folder / filename

    def proposal_record(self, destination: str, filename: str) -> dict[str, object]:
        return json.loads(self.proposal_path(destination, filename).read_text(encoding="utf-8"))

    def write_proposal_record(
        self, destination: str, filename: str, record: dict[str, object]
    ) -> None:
        self.proposal_path(destination, filename).write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8"
        )

    def create_memory(self, wording: str = "Prefer concise synthetic reflections.") -> str:
        result = self.runtime.create_pending_memory_proposal(
            wording, "This synthetic preference may remain useful."
        )
        self.assertTrue(result["ok"])
        return result["filename"]

    def create_state(self, wording: str = "A synthetic open question is active.") -> str:
        result = self.runtime.create_pending_state_proposal(
            wording,
            "This synthetic context is useful temporarily.",
            "Review at the next synthetic check-in.",
            "Expire after the synthetic milestone.",
        )
        self.assertTrue(result["ok"])
        return result["filename"]

    def approve(self, destination: str, filename: str, wording: str) -> dict[str, object]:
        return self.runtime.mark_proposal_status(
            destination,
            filename,
            "approved_for_apply",
            "Reviewed synthetic metadata.",
            wording,
            APPROVAL_CONFIRMATIONS[destination],
        )

    def apply(
        self,
        destination: str,
        filename: str,
        wording: str,
        target_file: str,
        confirmation: str | None = None,
    ) -> dict[str, object]:
        return self.runtime.apply_exact_approved_wording(
            destination,
            filename,
            wording,
            target_file,
            confirmation if confirmation is not None else APPROVAL_CONFIRMATIONS[destination],
            "Synthetic apply metadata.",
        )

    def test_memory_and_state_proposals_default_to_pending_and_unapplied(self) -> None:
        for destination, filename in (
            ("Memory", self.create_memory()),
            ("State", self.create_state()),
        ):
            with self.subTest(destination=destination):
                record = self.proposal_record(destination, filename)
                self.assertEqual(record["status"], "pending_review")
                self.assertEqual(record["review_status"], "pending_review")
                self.assertFalse(record["applied"])
                self.assertIsNone(record["approved_wording"])
                self.assertIsNone(record["approved_destination"])
                self.assertIsNone(record["approval_confirmation"])
                self.assertIsNone(record["applied_at"])
                self.assertIsNone(record["applied_to"])
                self.assertEqual(record["proposal_filename"], filename)

    def test_approval_requires_exact_wording_for_both_destinations(self) -> None:
        for destination, filename in (
            ("Memory", self.create_memory()),
            ("State", self.create_state()),
        ):
            with self.subTest(destination=destination):
                result = self.runtime.mark_proposal_status(
                    destination,
                    filename,
                    "approved_for_apply",
                    approval_confirmation=APPROVAL_CONFIRMATIONS[destination],
                )
                self.assertFalse(result["ok"])

    def test_approval_requires_matching_destination_confirmation(self) -> None:
        cases = (
            ("Memory", self.create_memory(), APPROVAL_CONFIRMATIONS["State"]),
            ("State", self.create_state(), APPROVAL_CONFIRMATIONS["Memory"]),
        )
        for destination, filename, wrong_confirmation in cases:
            with self.subTest(destination=destination):
                missing = self.runtime.mark_proposal_status(
                    destination,
                    filename,
                    "approved_for_apply",
                    approved_wording="Exact synthetic wording.",
                )
                wrong = self.runtime.mark_proposal_status(
                    destination,
                    filename,
                    "approved_for_apply",
                    approved_wording="Exact synthetic wording.",
                    approval_confirmation=wrong_confirmation,
                )
                self.assertFalse(missing["ok"])
                self.assertFalse(wrong["ok"])

    def test_reject_defer_and_pending_review_do_not_require_wording(self) -> None:
        for status in ("rejected", "deferred", "pending_review"):
            with self.subTest(status=status):
                filename = self.create_memory()
                result = self.runtime.mark_proposal_status("Memory", filename, status)
                self.assertTrue(result["ok"])
                record = self.proposal_record("Memory", filename)
                self.assertEqual(record["review_status"], status)
                self.assertIsNone(record["approved_wording"])

    def test_expire_is_state_only(self) -> None:
        state_filename = self.create_state()
        memory_filename = self.create_memory()
        self.assertTrue(
            self.runtime.mark_proposal_status("State", state_filename, "expired")["ok"]
        )
        self.assertFalse(
            self.runtime.mark_proposal_status("Memory", memory_filename, "expired")["ok"]
        )

    def test_state_approval_refuses_missing_lifecycle_trigger(self) -> None:
        filename = self.create_state()
        record = self.proposal_record("State", filename)
        record["expiration_trigger"] = ""
        self.write_proposal_record("State", filename, record)
        self.assertFalse(
            self.approve("State", filename, "A synthetic open question is active.")["ok"]
        )

    def test_review_notes_reject_large_or_secret_like_content(self) -> None:
        for note in ("x" * 501, "api_key=synthetic-credential-value"):
            with self.subTest(note_kind=len(note)):
                filename = self.create_memory()
                result = self.runtime.mark_proposal_status(
                    "Memory", filename, "rejected", review_note=note
                )
                self.assertFalse(result["ok"])

    def test_status_review_refuses_absolute_wildcard_and_directory_names(self) -> None:
        filename = self.create_memory()
        absolute = str(self.proposal_path("Memory", filename))
        for unsafe in (absolute, "*.json", "."):
            with self.subTest(unsafe=unsafe):
                self.assertFalse(
                    self.runtime.mark_proposal_status(
                        "Memory", unsafe, "rejected"
                    )["ok"]
                )

    def test_status_review_preserves_body_and_never_writes_memory_or_state(self) -> None:
        filename = self.create_memory()
        original_record = self.proposal_record("Memory", filename)
        memory_before = self.snapshot("Memory")
        state_before = self.snapshot("State")
        result = self.approve("Memory", filename, "Edited exact synthetic wording.")
        self.assertTrue(result["ok"])
        reviewed = self.proposal_record("Memory", filename)
        self.assertEqual(reviewed["proposal"], original_record["proposal"])
        self.assertEqual(reviewed["approved_wording"], "Edited exact synthetic wording.")
        self.assertEqual(reviewed["approved_destination"], "Memory")
        self.assertEqual(self.snapshot("Memory"), memory_before)
        self.assertEqual(self.snapshot("State"), state_before)

    def test_editing_approved_wording_replaces_the_exact_apply_value(self) -> None:
        filename = self.create_memory()
        first_wording = "Prefer concise synthetic reflections."
        edited_wording = "Prefer one concise synthetic question at a time."
        self.assertTrue(self.approve("Memory", filename, first_wording)["ok"])
        self.assertTrue(self.approve("Memory", filename, edited_wording)["ok"])
        record = self.proposal_record("Memory", filename)
        self.assertEqual(record["approved_wording"], edited_wording)
        self.assertFalse(
            self.apply(
                "Memory", filename, first_wording, "reflection-preferences.md"
            )["ok"]
        )
        self.assertTrue(
            self.apply(
                "Memory", filename, edited_wording, "reflection-preferences.md"
            )["ok"]
        )

    def test_apply_refuses_every_nonapproved_status(self) -> None:
        for status in ("pending_review", "rejected", "deferred"):
            with self.subTest(status=status):
                filename = self.create_memory()
                if status != "pending_review":
                    self.assertTrue(
                        self.runtime.mark_proposal_status("Memory", filename, status)["ok"]
                    )
                result = self.apply(
                    "Memory",
                    filename,
                    "Prefer concise synthetic reflections.",
                    "reflection-preferences.md",
                )
                self.assertFalse(result["ok"])

        state_filename = self.create_state()
        self.assertTrue(
            self.runtime.mark_proposal_status("State", state_filename, "expired")["ok"]
        )
        self.assertFalse(
            self.apply(
                "State",
                state_filename,
                "A synthetic open question is active.",
                "current-state.md",
            )["ok"]
        )

    def test_apply_refuses_cross_destination_and_tampered_destination_metadata(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        self.assertFalse(
            self.apply("State", filename, wording, "current-state.md")["ok"]
        )
        record = self.proposal_record("Memory", filename)
        record["destination"] = "State"
        self.write_proposal_record("Memory", filename, record)
        self.assertFalse(
            self.apply("Memory", filename, wording, "reflection-preferences.md")["ok"]
        )

    def test_apply_refuses_tampered_approved_destination(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        record = self.proposal_record("Memory", filename)
        record["approved_destination"] = "State"
        self.write_proposal_record("Memory", filename, record)
        self.assertFalse(
            self.apply("Memory", filename, wording, "reflection-preferences.md")["ok"]
        )

    def test_apply_refuses_incomplete_review_metadata(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        record = self.proposal_record("Memory", filename)
        record["reviewed_at"] = None
        self.write_proposal_record("Memory", filename, record)
        self.assertFalse(
            self.apply("Memory", filename, wording, "reflection-preferences.md")["ok"]
        )

    def test_apply_refuses_any_wording_difference(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        for changed in (wording + " ", wording[:-1], wording.replace("concise", "brief")):
            with self.subTest(changed=changed):
                self.assertFalse(
                    self.apply(
                        "Memory", filename, changed, "reflection-preferences.md"
                    )["ok"]
                )

    def test_apply_refuses_missing_or_wrong_confirmation(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        for confirmation in ("", APPROVAL_CONFIRMATIONS["State"]):
            with self.subTest(confirmation=confirmation):
                self.assertFalse(
                    self.apply(
                        "Memory",
                        filename,
                        wording,
                        "reflection-preferences.md",
                        confirmation,
                    )["ok"]
                )

    def test_apply_refuses_nonallowlisted_traversing_and_arbitrary_targets(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        absolute = str(self.vault / "Memory/reflection-preferences.md")
        for target in (
            "current-state.md",
            "../Memory/reflection-preferences.md",
            "notes.md",
            absolute,
            "*.md",
        ):
            with self.subTest(target=target):
                self.assertFalse(self.apply("Memory", filename, wording, target)["ok"])

    def test_state_apply_refuses_missing_triggers_even_after_review(self) -> None:
        filename = self.create_state()
        wording = "A synthetic open question is active."
        self.assertTrue(self.approve("State", filename, wording)["ok"])
        record = self.proposal_record("State", filename)
        record["review_or_stale_trigger"] = ""
        self.write_proposal_record("State", filename, record)
        self.assertFalse(self.apply("State", filename, wording, "current-state.md")["ok"])

    def test_successful_memory_apply_appends_only_to_allowlisted_memory(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        memory_before = self.snapshot("Memory")
        state_before = self.snapshot("State")
        result = self.apply("Memory", filename, wording, "reflection-preferences.md")
        self.assertTrue(result["ok"])
        memory_after = self.snapshot("Memory")
        self.assertTrue(
            memory_after["reflection-preferences.md"].startswith(
                memory_before["reflection-preferences.md"]
            )
        )
        self.assertIn(wording, memory_after["reflection-preferences.md"])
        self.assertEqual(memory_after["recurring-patterns.md"], memory_before["recurring-patterns.md"])
        self.assertEqual(memory_after["values-and-supports.md"], memory_before["values-and-supports.md"])
        self.assertEqual(self.snapshot("State"), state_before)

    def test_successful_apply_preserves_multiline_wording_characters(self) -> None:
        wording = "First synthetic line.\nSecond synthetic line."
        filename = self.create_memory(wording)
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        result = self.apply("Memory", filename, wording, "recurring-patterns.md")
        self.assertTrue(result["ok"])
        applied = (self.vault / "Memory/recurring-patterns.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(f"- Approved wording:\n\n{wording}\n", applied)

    def test_successful_state_apply_appends_triggers_only_to_state(self) -> None:
        filename = self.create_state()
        wording = "A synthetic open question is active."
        self.assertTrue(self.approve("State", filename, wording)["ok"])
        state_before = self.snapshot("State")
        memory_before = self.snapshot("Memory")
        result = self.apply("State", filename, wording, "current-state.md")
        self.assertTrue(result["ok"])
        state_after = self.snapshot("State")
        applied = state_after["current-state.md"]
        self.assertTrue(applied.startswith(state_before["current-state.md"]))
        self.assertIn(wording, applied)
        self.assertIn("Review at the next synthetic check-in.", applied)
        self.assertIn("Expire after the synthetic milestone.", applied)
        self.assertEqual(state_after["active-themes.md"], state_before["active-themes.md"])
        self.assertEqual(state_after["open-questions.md"], state_before["open-questions.md"])
        self.assertEqual(self.snapshot("Memory"), memory_before)

    def test_successful_apply_marks_metadata_and_writes_content_free_audit(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        proposal_body = self.proposal_record("Memory", filename)["proposal"]
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        result = self.apply("Memory", filename, wording, "reflection-preferences.md")
        self.assertTrue(result["ok"])
        record = self.proposal_record("Memory", filename)
        self.assertTrue(record["applied"])
        self.assertTrue(record["applied_at"])
        self.assertEqual(record["applied_to"], "reflection-preferences.md")
        self.assertEqual(len(record["applied_wording_hash"]), 64)

        audit_path = self.vault / "Journal Mirror/Audit" / result["audit_filename"]
        audit_text = audit_path.read_text(encoding="utf-8")
        audit = json.loads(audit_text)
        self.assertEqual(audit["event_type"], "proposal_applied")
        self.assertEqual(audit["target_file"], "reflection-preferences.md")
        self.assertFalse(audit["content_logged"])
        self.assertNotIn(wording, audit_text)
        self.assertNotIn(str(proposal_body), audit_text)

    def test_metadata_listing_shows_review_and_apply_without_wording_or_body(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        proposal_body = self.proposal_record("Memory", filename)["proposal"]
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        self.assertTrue(
            self.apply("Memory", filename, wording, "reflection-preferences.md")["ok"]
        )
        listed = self.runtime.list_pending_proposal_metadata("Memory")
        self.assertTrue(listed["ok"])
        item = listed["proposals"]["Memory"][0]
        self.assertEqual(item["review_status"], "approved_for_apply")
        self.assertTrue(item["applied"])
        self.assertEqual(item["applied_to"], "reflection-preferences.md")
        serialized = json.dumps(listed)
        self.assertNotIn(wording, serialized)
        self.assertNotIn(str(proposal_body), serialized)

    def test_apply_refuses_second_apply_and_post_apply_review(self) -> None:
        filename = self.create_memory()
        wording = "Prefer concise synthetic reflections."
        self.assertTrue(self.approve("Memory", filename, wording)["ok"])
        first = self.apply("Memory", filename, wording, "reflection-preferences.md")
        target = self.vault / "Memory/reflection-preferences.md"
        after_first = target.read_text(encoding="utf-8")
        second = self.apply("Memory", filename, wording, "reflection-preferences.md")
        self.assertFalse(second["ok"])
        self.assertEqual(target.read_text(encoding="utf-8"), after_first)
        self.assertFalse(
            self.runtime.mark_proposal_status("Memory", filename, "pending_review")["ok"]
        )


if __name__ == "__main__":
    unittest.main()

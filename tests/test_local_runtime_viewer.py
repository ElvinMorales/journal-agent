"""Synthetic boundary and rendering tests for the local runtime viewer."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from mcp_server.vault_runtime import REPO_ROOT, REQUIRED_DIRECTORIES, VaultBoundaryError
from viewer.local_runtime_viewer import (
    collect_runtime_snapshot,
    main,
    render_html,
    resolve_viewer_paths,
)


class LocalRuntimeViewerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name).resolve()
        self.vault = self.base / "synthetic-vault"
        for relative in REQUIRED_DIRECTORIES:
            (self.vault / relative).mkdir(parents=True, exist_ok=True)
        (self.vault / "Journal/Daily").mkdir(parents=True)
        self.output_parent = self.base / "private-output"
        self.output_parent.mkdir()
        self.output = self.output_parent / "runtime-viewer.html"
        self._write_synthetic_runtime()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write(self, relative: str, text: str) -> Path:
        target = self.vault / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def _json(self, relative: str, value: dict[str, object]) -> Path:
        return self._write(relative, json.dumps(value))

    def _write_synthetic_runtime(self) -> None:
        self.memory_secret = "SYNTHETIC_MEMORY_BODY_PRIVATE"
        self.state_secret = "SYNTHETIC_STATE_BODY_PRIVATE"
        self.proposal_secret = "SYNTHETIC_PROPOSAL_BODY_PRIVATE"
        self.wording_secret = "SYNTHETIC_APPROVED_WORDING_PRIVATE"
        self.session_secret = "SYNTHETIC_SESSION_RAW_PRIVATE"
        self.journal_secret = "SYNTHETIC_DAILY_ENTRY_MUST_NEVER_BE_READ"
        self.audit_secret = "SYNTHETIC_AUDIT_NOTE_PRIVATE"

        for filename in ("reflection-preferences.md", "recurring-patterns.md", "values-and-supports.md"):
            self._write(f"Memory/{filename}", f"# Synthetic Memory\n\n{self.memory_secret}\n")
        for filename in ("current-state.md", "active-themes.md", "open-questions.md"):
            self._write(
                f"State/{filename}",
                "# Synthetic State\n\n"
                "- Review/stale trigger: Review at the synthetic checkpoint.\n"
                "- Expiration trigger: Expire after the synthetic milestone.\n"
                f"{self.state_secret}\n",
            )
        common = {
            "artifact_type": "journal_mirror_pending_proposal",
            "status": "approved_for_apply",
            "review_status": "approved_for_apply",
            "applied": True,
            "applied_to": "reflection-preferences.md",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-02T00:00:00Z",
            "reviewed_at": "2026-01-02T00:00:00Z",
            "applied_at": "2026-01-03T00:00:00Z",
            "title": "Synthetic <unsafe> & title",
            "proposal": self.proposal_secret + " <script>alert(1)</script>",
            "approved_wording": self.wording_secret,
        }
        self._json(
            "Journal Mirror/Pending Updates/memory/memory.json",
            {**common, "destination": "Memory"},
        )
        self._json(
            "Journal Mirror/Pending Updates/state/state.json",
            {
                **common,
                "destination": "State",
                "applied_to": "current-state.md",
                "review_or_stale_trigger": "Review at the next synthetic check-in.",
                "expiration_trigger": "Expire after the synthetic trial.",
            },
        )
        self._write(
            "Journal Mirror/Pending Updates/memory/malformed.json",
            '{"private": "MALFORMED_PRIVATE_LEAK",',
        )
        self._write("Journal Mirror/Sessions/session.md", f"# Session\n{self.session_secret}\n")
        self._json(
            "Journal Mirror/Audit/audit.json",
            {
                "artifact_type": "journal_mirror_private_audit_metadata",
                "event_type": "proposal_applied",
                "timestamp": "2026-01-03T00:00:00Z",
                "destination": "Memory",
                "proposal_filename": "memory.json",
                "target_file": "reflection-preferences.md",
                "content_logged": False,
                "approved_wording_hash": "a" * 64,
                "approved_wording_characters": 35,
                "note": self.audit_secret,
            },
        )
        self._write("Journal/Daily/private.md", self.journal_secret)

    def _default_html(self) -> str:
        return render_html(collect_runtime_snapshot(self.vault))

    def test_refuses_repo_or_inside_repo_vault_roots(self) -> None:
        for vault in (REPO_ROOT, REPO_ROOT / "private"):
            with self.subTest(vault=vault), self.assertRaises(VaultBoundaryError):
                resolve_viewer_paths(vault, self.output)

    def test_refuses_relative_missing_and_uninitialized_vault_roots(self) -> None:
        for vault in (Path("relative-vault"), self.base / "missing", self.base / "empty"):
            if vault.name == "empty":
                vault.mkdir()
            with self.subTest(vault=vault), self.assertRaises(VaultBoundaryError):
                resolve_viewer_paths(vault, self.output)

    def test_refuses_repo_output_and_missing_output_parent(self) -> None:
        outputs = (Path("relative-viewer.html"), REPO_ROOT, REPO_ROOT / "runtime-viewer.html",
                   self.base / "missing" / "viewer.html")
        for output in outputs:
            with self.subTest(output=output), self.assertRaises(VaultBoundaryError):
                resolve_viewer_paths(self.vault, output)

    def test_dry_run_writes_no_html(self) -> None:
        result = main(["--vault-root", str(self.vault), "--output", str(self.output), "--dry-run"])
        self.assertEqual(result, 0)
        self.assertFalse(self.output.exists())

    def test_generates_one_static_html_file_outside_repo(self) -> None:
        result = main(["--vault-root", str(self.vault), "--output", str(self.output)])
        self.assertEqual(result, 0)
        self.assertTrue(self.output.is_file())
        self.assertEqual([path.name for path in self.output_parent.iterdir()], [self.output.name])

    def test_default_render_has_warnings_csp_and_no_active_content(self) -> None:
        rendered = self._default_html()
        self.assertIn("Private, local artifact", rendered)
        self.assertIn("Do not publish or commit it", rendered)
        self.assertIn("Raw journal content is hidden by default", rendered)
        self.assertIn("default-src 'none'", rendered)
        self.assertIn("script-src 'none'", rendered)
        self.assertNotIn("<script", rendered.casefold())
        self.assertNotIn("http://", rendered.casefold())
        self.assertNotIn("https://", rendered.casefold())
        self.assertNotIn("src=", rendered.casefold())

    def test_default_render_separates_memory_state_and_proposals(self) -> None:
        rendered = self._default_html()
        for heading in (
            "<h2>Memory</h2>", "<h2>State</h2>",
            "<h2>Pending Memory proposals</h2>", "<h2>Pending State proposals</h2>",
            "<h2>Recent session metadata</h2>", "<h2>Audit metadata</h2>",
        ):
            self.assertIn(heading, rendered)
        self.assertIn("approved_for_apply", rendered)
        self.assertIn("reflection-preferences.md", rendered)
        self.assertIn("proposal_applied", rendered)

    def test_default_render_shows_state_triggers_and_metadata_not_content(self) -> None:
        rendered = self._default_html()
        self.assertIn("Review/stale trigger: Review at the synthetic checkpoint", rendered)
        self.assertIn("Expiration trigger: Expire after the synthetic milestone", rendered)
        self.assertIn("Review at the next synthetic check-in", rendered)
        self.assertIn("Expire after the synthetic trial", rendered)
        for private_text in (
            self.memory_secret, self.state_secret, self.proposal_secret, self.wording_secret,
            self.session_secret, self.journal_secret, self.audit_secret, "MALFORMED_PRIVATE_LEAK",
        ):
            self.assertNotIn(private_text, rendered)
        self.assertIn("Has Exact Approved Wording</dt><dd>yes", rendered)

    def test_dynamic_values_are_escaped_and_full_vault_path_is_hidden(self) -> None:
        rendered = self._default_html()
        self.assertIn("Synthetic &lt;unsafe&gt; &amp; title", rendered)
        self.assertNotIn("Synthetic <unsafe>", rendered)
        self.assertNotIn(str(self.vault), rendered)
        self.assertIn("Vault: synthetic-vault", rendered)

    def test_malformed_proposal_is_safe_and_does_not_crash(self) -> None:
        rendered = self._default_html()
        self.assertIn("malformed.json", rendered)
        self.assertIn("invalid JSON", rendered)
        self.assertNotIn("MALFORMED_PRIVATE_LEAK", rendered)

    def test_explicit_proposal_body_is_escaped_and_warned(self) -> None:
        snapshot = collect_runtime_snapshot(self.vault, include_proposal_body=True)
        rendered = render_html(snapshot)
        self.assertIn(self.proposal_secret, rendered)
        self.assertIn(self.wording_secret, rendered)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", rendered)
        self.assertNotIn("<script", rendered.casefold())
        self.assertIn("Sensitive include options were enabled", rendered)

    def test_explicit_other_content_flags_are_bounded_and_warned(self) -> None:
        snapshot = collect_runtime_snapshot(
            self.vault,
            include_memory_content=True,
            include_state_content=True,
            include_session_previews=True,
            include_audit_details=True,
        )
        rendered = render_html(snapshot)
        for included in (self.memory_secret, self.state_secret, self.session_secret, self.audit_secret):
            self.assertIn(included, rendered)
        self.assertIn("Sensitive include options were enabled", rendered)
        self.assertNotIn(self.journal_secret, rendered)

    def test_max_items_limits_each_runtime_listing(self) -> None:
        for index in range(3):
            self._json(
                f"Journal Mirror/Pending Updates/state/extra-{index}.json",
                {"destination": "State", "status": f"extra-{index}"},
            )
            self._write(f"Journal Mirror/Sessions/extra-{index}.md", "synthetic")
            self._json(f"Journal Mirror/Audit/extra-{index}.json", {"event_type": f"extra-{index}"})
        snapshot = collect_runtime_snapshot(self.vault, max_items=2)
        self.assertEqual(len(snapshot["proposals"]["Memory"]), 2)
        self.assertEqual(len(snapshot["proposals"]["State"]), 2)
        self.assertEqual(len(snapshot["sessions"]), 2)
        self.assertEqual(len(snapshot["audit"]), 2)

    def test_invalid_max_items_is_refused(self) -> None:
        for value in (0, 501):
            with self.subTest(value=value), self.assertRaises(VaultBoundaryError):
                collect_runtime_snapshot(self.vault, max_items=value)


if __name__ == "__main__":
    unittest.main()

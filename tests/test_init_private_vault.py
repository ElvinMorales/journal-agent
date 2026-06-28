"""Tests for the private vault initializer."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "init-private-vault.py"
SPEC = importlib.util.spec_from_file_location("init_private_vault", SCRIPT)
assert SPEC and SPEC.loader
INITIALIZER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INITIALIZER)


class PrivateVaultInitializerTests(unittest.TestCase):
    def run_script(self, target: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--vault-root", str(target), *extra],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_dry_run_creates_no_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            result = self.run_script(target, "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(target.exists())
            self.assertIn("mode=dry-run", result.stdout)

    def test_actual_run_creates_expected_structure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            result = self.run_script(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            for relative in INITIALIZER.DIRECTORIES:
                self.assertTrue((target / relative).is_dir(), relative)
            for relative in INITIALIZER.STARTER_FILES:
                self.assertTrue((target / relative).is_file(), relative)

    def test_rerun_is_idempotent_and_does_not_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            first = self.run_script(target)
            self.assertEqual(first.returncode, 0, first.stderr)
            protected = target / "Memory" / "reflection-preferences.md"
            protected.write_text("user-owned content\n", encoding="utf-8")

            second = self.run_script(target)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(protected.read_text(encoding="utf-8"), "user-owned content\n")
            self.assertIn(f"SKIP file {protected}", second.stdout)

    def test_force_overwrites_only_managed_starter_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            self.assertEqual(self.run_script(target).returncode, 0)
            managed = target / "Memory" / "reflection-preferences.md"
            unmanaged = target / "user-note.md"
            managed.write_text("changed\n", encoding="utf-8")
            unmanaged.write_text("keep\n", encoding="utf-8")

            result = self.run_script(target, "--force")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotEqual(managed.read_text(encoding="utf-8"), "changed\n")
            self.assertEqual(unmanaged.read_text(encoding="utf-8"), "keep\n")

    def test_target_inside_repo_is_refused(self) -> None:
        target = REPO_ROOT / "private-vault-test-target"
        result = self.run_script(target)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(target.exists())
        self.assertIn("inside the public repository", result.stderr)

    def test_target_equal_to_repo_root_is_refused(self) -> None:
        result = self.run_script(REPO_ROOT)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("public repository root", result.stderr)

    def test_relative_target_is_refused(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--vault-root", "ambiguous-vault"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("absolute path", result.stderr)

    def test_memory_state_and_pending_destinations_are_separate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            self.assertEqual(self.run_script(target).returncode, 0)
            self.assertTrue((target / "Memory" / "reflection-preferences.md").is_file())
            self.assertTrue((target / "State" / "current-state.md").is_file())
            self.assertTrue((target / "Journal Mirror/Pending Updates/memory/README.md").is_file())
            self.assertTrue((target / "Journal Mirror/Pending Updates/state/README.md").is_file())

    def test_generated_files_are_generic_and_exclude_risky_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "vault"
            self.assertEqual(self.run_script(target).returncode, 0)
            generated_files = [path for path in target.rglob("*") if path.is_file()]
            relative_names = {path.relative_to(target).as_posix().lower() for path in generated_files}
            forbidden_suffixes = {".env", ".log", ".db", ".sqlite", ".sqlite3"}
            forbidden_name_parts = ("token", "secret", "connector", "config")
            self.assertTrue(generated_files)
            self.assertFalse(any(path.suffix.lower() in forbidden_suffixes for path in generated_files))
            self.assertFalse(any(part in name for name in relative_names for part in forbidden_name_parts))

            combined = "\n".join(path.read_text(encoding="utf-8") for path in generated_files).lower()
            self.assertNotIn("example journal entry", combined)
            self.assertNotIn("actual journal", combined)
            self.assertIn("approved items", combined)
            self.assertIn("nothing here is applied automatically", combined)


if __name__ == "__main__":
    unittest.main()

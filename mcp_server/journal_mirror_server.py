"""Minimal local MCP server for a user-controlled Journal Mirror vault."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Any, Iterable

from .vault_runtime import VaultBoundaryError, VaultRuntime


LOGGER = logging.getLogger("journal_mirror_mcp")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the minimal local Journal Mirror MCP server over stdio."
    )
    parser.add_argument(
        "--vault-root",
        help="Absolute initialized private-vault path; overrides JOURNAL_MIRROR_VAULT_ROOT.",
    )
    return parser.parse_args(argv)


def configured_vault_root(cli_value: str | None) -> str:
    root = cli_value or os.environ.get("JOURNAL_MIRROR_VAULT_ROOT")
    if not root:
        raise VaultBoundaryError(
            "set --vault-root or JOURNAL_MIRROR_VAULT_ROOT to an explicit private-vault path"
        )
    return root


def create_mcp_server(runtime: VaultRuntime) -> Any:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise RuntimeError(
            'The official Python MCP SDK is required. Install it with: python -m pip install "mcp[cli]"'
        ) from exc

    mcp = FastMCP("Journal Mirror")

    @mcp.tool()
    def read_selected_session_context(relative_path: str) -> dict[str, Any]:
        """Read one explicit file under Journal Mirror/Sessions, subject to size limits."""
        return runtime.read_selected_session_context(relative_path)

    @mcp.tool()
    def read_approved_memory(memory_file: str) -> dict[str, Any]:
        """Read one allowlisted approved Memory file."""
        return runtime.read_approved_memory(memory_file)

    @mcp.tool()
    def read_current_state(state_file: str) -> dict[str, Any]:
        """Read one allowlisted current State file."""
        return runtime.read_current_state(state_file)

    @mcp.tool()
    def create_pending_memory_proposal(
        proposal: str,
        rationale: str,
        source_summary: str = "",
        review_note: str = "",
    ) -> dict[str, Any]:
        """Create one inert pending Memory proposal; never write Memory."""
        return runtime.create_pending_memory_proposal(
            proposal, rationale, source_summary, review_note
        )

    @mcp.tool()
    def create_pending_state_proposal(
        proposal: str,
        rationale: str,
        review_or_stale_trigger: str,
        expiration_trigger: str,
        source_summary: str = "",
        review_note: str = "",
    ) -> dict[str, Any]:
        """Create one inert pending State proposal with required lifecycle triggers."""
        return runtime.create_pending_state_proposal(
            proposal,
            rationale,
            review_or_stale_trigger,
            expiration_trigger,
            source_summary,
            review_note,
        )

    @mcp.tool()
    def list_pending_proposal_metadata(destination: str = "all") -> dict[str, Any]:
        """List metadata, never proposal bodies, from pending proposal folders."""
        return runtime.list_pending_proposal_metadata(destination)

    @mcp.tool()
    def mark_proposal_status(
        destination: str,
        filename: str,
        status: str,
        review_note: str = "",
        approved_wording: str = "",
        approval_confirmation: str = "",
    ) -> dict[str, Any]:
        """Review one pending proposal without applying it."""
        return runtime.mark_proposal_status(
            destination,
            filename,
            status,
            review_note,
            approved_wording,
            approval_confirmation,
        )

    @mcp.tool()
    def apply_exact_approved_wording(
        destination: str,
        filename: str,
        approved_wording: str,
        target_file: str,
        approval_confirmation: str,
        approval_note: str = "",
    ) -> dict[str, Any]:
        """Append exact reviewed wording to one allowlisted destination file."""
        return runtime.apply_exact_approved_wording(
            destination,
            filename,
            approved_wording,
            target_file,
            approval_confirmation,
            approval_note,
        )

    @mcp.tool()
    def write_private_audit_entry(
        event_type: str,
        destination: str = "none",
        proposal_filename: str = "",
        note: str = "",
    ) -> dict[str, Any]:
        """Write one private metadata-only audit entry."""
        return runtime.write_private_audit_entry(
            event_type, destination, proposal_filename, note
        )

    return mcp


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stderr,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    try:
        runtime = VaultRuntime(configured_vault_root(args.vault_root))
        mcp = create_mcp_server(runtime)
    except (OSError, RuntimeError, VaultBoundaryError) as exc:
        LOGGER.error("Server startup refused: %s", exc)
        return 2

    LOGGER.info("Starting local stdio server for a validated private vault")
    mcp.run(transport="stdio")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

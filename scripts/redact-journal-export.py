from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = [
    (re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b"), "[email]"),
    (re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b"), "[phone]"),
    (re.compile(r"\b\d{1,5}\s+[A-Z][A-Za-z0-9.\s]+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd)\b"), "[address]"),
]


def redact(text: str) -> str:
    redacted = text
    for pattern, replacement in PATTERNS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: python scripts/redact-journal-export.py INPUT OUTPUT")
        return 2

    input_path = Path(argv[1])
    output_path = Path(argv[2])

    text = input_path.read_text(encoding="utf-8")
    output_path.write_text(redact(text), encoding="utf-8")
    print(f"Wrote redacted export to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

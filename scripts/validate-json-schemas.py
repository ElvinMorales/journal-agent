from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    schema_dir = Path("schemas")
    failures: list[str] = []

    for path in sorted(schema_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{path}: invalid JSON: {exc}")
            continue

        if data.get("$schema") is None:
            failures.append(f"{path}: missing $schema")
        if data.get("type") != "object":
            failures.append(f"{path}: top-level type must be object")
        if "properties" not in data:
            failures.append(f"{path}: missing properties")

    if failures:
        print("Schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(list(schema_dir.glob('*.json')))} JSON schema files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

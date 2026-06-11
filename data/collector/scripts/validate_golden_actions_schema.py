#!/usr/bin/env python3

import json
from pathlib import Path
from typing import Any, Mapping, cast

from jsonschema import Draft202012Validator


def main() -> int:
    data_dir = Path(__file__).resolve().parents[2]
    schema_path = data_dir / "schema" / "golden_action.schema.json"
    if not schema_path.exists():
        raise SystemExit(f"Schema not found: {schema_path}")

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if not isinstance(schema, (dict, bool)):
        raise SystemExit(f"Schema must be a JSON object or boolean: {schema_path}")
    validator = Draft202012Validator(cast(Mapping[str, Any] | bool, schema))
    target_paths = sorted((data_dir / "tasks").glob("*/golden_actions.json"))

    print(f"Schema: {schema_path}")
    print(f"Targets: {len(target_paths)}")

    if not target_paths:
        print("No golden_actions.json files found under data/tasks.")
        return 0

    total_errors = 0
    for path in target_paths:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"[FAIL] {path}")
            print(f"  - <root>: invalid JSON ({exc})")
            total_errors += 1
            continue

        errors = sorted(validator.iter_errors(cast(Any, payload)), key=lambda e: list(e.path))
        if not errors:
            print(f"[PASS] {path}")
            continue

        print(f"[FAIL] {path}")
        for err in errors:
            location = "/".join(str(item) for item in err.path) or "<root>"
            print(f"  - {location}: {err.message}")
        total_errors += len(errors)

    if total_errors:
        raise SystemExit(f"Schema validation failed with {total_errors} error(s).")

    print("All golden_actions.json files are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

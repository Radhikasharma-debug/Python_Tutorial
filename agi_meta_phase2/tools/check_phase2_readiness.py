#!/usr/bin/env python3
"""Readiness checks for AGI-META Phase 2 dry run artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_FILE = ROOT / "DRY_RUN_CASES.json"


def main() -> int:
    if not CASE_FILE.exists():
        print(f"ERROR: missing case matrix: {CASE_FILE}")
        return 1

    data = json.loads(CASE_FILE.read_text(encoding="utf-8"))
    cases = data.get("cases", [])

    if not (20 <= len(cases) <= 50):
        print(f"ERROR: case count {len(cases)} is outside required range [20, 50]")
        return 1

    case_ids = [c.get("case_id") for c in cases]
    if len(case_ids) != len(set(case_ids)):
        print("ERROR: duplicate case_id values found")
        return 1

    classes = {"valid": 0, "invalid": 0, "adversarial": 0}
    required_keys = {"case_id", "class", "focus", "expected"}
    for idx, case in enumerate(cases):
        missing = required_keys - set(case)
        if missing:
            print(f"ERROR: case[{idx}] missing keys: {sorted(missing)}")
            return 1
        c = case["class"]
        if c not in classes:
            print(f"ERROR: case[{idx}] has unknown class: {c}")
            return 1
        classes[c] += 1

    if classes["valid"] < 12:
        print("ERROR: insufficient valid cases; require at least 12")
        return 1
    if classes["invalid"] < 2:
        print("ERROR: insufficient invalid cases; require at least 2")
        return 1
    if classes["adversarial"] < 2:
        print("ERROR: insufficient adversarial cases; require at least 2")
        return 1

    print("OK: Phase 2 readiness checks passed")
    print(f"INFO: total_cases={len(cases)} class_breakdown={classes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

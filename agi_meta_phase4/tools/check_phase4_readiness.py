#!/usr/bin/env python3
"""Validate required Phase 4 artifacts and key section markers."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "PHASE4_FINAL_EVAL_RUNBOOK.md": [
        "Phase 4 Objective",
        "Final Evaluation Sequence",
        "Hard Fail Conditions",
    ],
    "ROBUSTNESS_AUDIT.md": [
        "Audit Packs",
        "Pass/Flag Thresholds",
        "Decision Rule",
    ],
    "TECHNICAL_REPORT_TEMPLATE.md": [
        "Abstract",
        "Results",
        "Future Work",
    ],
    "WINNING_METHOD_ANALYSIS.md": [
        "Top Submission Profile",
        "Why It Won",
        "Reproducibility Notes",
    ],
}

NOTEBOOK = ROOT / "kaggle" / "phase4_control_center.ipynb"


def main() -> int:
    missing = []
    marker_errors = []

    for name, markers in REQUIRED_FILES.items():
        path = ROOT / name
        if not path.exists():
            missing.append(str(path))
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                marker_errors.append(f"{name}: missing marker '{marker}'")

    if not NOTEBOOK.exists():
        missing.append(str(NOTEBOOK))
    else:
        try:
            nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
            if "cells" not in nb:
                marker_errors.append("phase4_control_center.ipynb: missing 'cells'")
        except json.JSONDecodeError as exc:
            marker_errors.append(f"phase4_control_center.ipynb: invalid JSON ({exc})")

    if missing or marker_errors:
        print("PHASE4_READINESS: FAIL")
        for item in missing:
            print(f"- missing: {item}")
        for item in marker_errors:
            print(f"- error: {item}")
        return 1

    print("PHASE4_READINESS: OK")
    print(f"validated_files={len(REQUIRED_FILES) + 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

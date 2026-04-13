#!/usr/bin/env python3
"""Readiness checks for AGI-META Phase 3 live operations artifacts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "PHASE3_LAUNCH_RUNBOOK.md",
    ROOT / "LEADERBOARD_INTEGRITY.md",
    ROOT / "INCIDENT_RESPONSE.md",
    ROOT / "PARTICIPANT_COMMS.md",
    ROOT / "DAILY_OPS_CHECKLIST.md",
]

REQUIRED_PHRASES = {
    ROOT / "PHASE3_LAUNCH_RUNBOOK.md": ["Hard Stop Conditions", "Operational SLAs"],
    ROOT / "LEADERBOARD_INTEGRITY.md": ["Daily Top-K Repro Audit", "Enforcement Ladder"],
    ROOT / "INCIDENT_RESPONSE.md": ["Severity Levels", "SEV-1 Immediate Actions"],
}


def main() -> int:
    missing = [str(p) for p in REQUIRED_FILES if not p.exists()]
    if missing:
        print("ERROR: missing required Phase 3 files:")
        for item in missing:
            print(f" - {item}")
        return 1

    for path, phrases in REQUIRED_PHRASES.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                print(f"ERROR: '{phrase}' not found in {path}")
                return 1

    print("OK: Phase 3 readiness artifacts present and structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

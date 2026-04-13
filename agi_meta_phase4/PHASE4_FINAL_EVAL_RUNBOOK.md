# AGI-META Phase 4 — Final Evaluation & Reporting Runbook

Status: **PREPARED**
Depends on: `agi_meta_phase1/*`, `agi_meta_phase2/*`, `agi_meta_phase3/*`.

## 1) Phase 4 Objective
Close the competition with reproducible private scoring, robustness verification, and publication-grade reporting.

## 2) Entry Criteria (Must Be True)
- Phase 3 is completed and public submissions are closed.
- Final evaluator image digest and seeds are unchanged from lock policy.
- Private split access is restricted to authorized evaluators.
- Incident log is resolved or accepted with explicit sign-off.

## 3) Final Evaluation Sequence
1. Snapshot submission table and freeze final ranking timestamp.
2. Run duplicate/submission-integrity sweep before private scoring.
3. Score all eligible submissions against private split.
4. Run deterministic rerun for Top-20 and all medal-bound positions.
5. Execute robustness audit against perturbation stress packs.
6. Produce final ranking with tie-break policy from Phase 1 metrics.
7. Generate report bundle and publish winners.

## 4) Private Scoring Requirements
- Use only locked evaluator image and pinned dependencies.
- Log per-submission scoring runtime, memory, and failure class.
- Persist per-module subscores (`P,C,R,L,T`) and penalties.
- Track deterministic rerun delta (must be <= 0.1 absolute score).

## 5) Robustness Audit Requirements
- Evaluate Top-10 on hidden perturbation stress packs.
- Run at least 3 seed variants from `SEEDS.yaml` policy family.
- Record calibration drift and transfer-retention changes.
- Flag brittle methods where rank changes > 5 positions under audit.

## 6) Publication Outputs
- `FINAL_LEADERBOARD.csv`
- `ROBUSTNESS_AUDIT_RESULTS.md`
- `TECHNICAL_REPORT.md`
- `WINNING_METHOD_ANALYSIS.md`
- `PHASE4_DECISION_LOG.md`

## 7) Hard Fail Conditions
Pause finalization and open incident if any occur:
- private scoring reproducibility violation,
- tie-break implementation mismatch with locked spec,
- unresolved exploit affecting final ranking,
- missing audit evidence for medal positions.

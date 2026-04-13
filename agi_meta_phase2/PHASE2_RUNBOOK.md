# AGI-META Phase 2 — Dry-Run Runbook

Status: **READY FOR EXECUTION**  
Depends on: `agi_meta_phase1/*` spec lock artifacts.

## 1) Phase 2 Objective
Execute a controlled internal dry run with **24 submissions** (within required 20–50 range) to verify:
1. scorer correctness,
2. runtime stability,
3. exploit resistance,
4. leaderboard rank stability.

## 2) Exit Criteria (Go/No-Go)
Phase 2 passes only if all criteria below are met:
- 100% of valid cases score successfully.
- 100% of intentionally invalid/adversarial cases are rejected with correct error class.
- p95 scoring runtime <= 18 minutes per submission.
- zero nondeterministic score drift when rerunning same artifact + seed.
- exploit tests report no critical bypasses.

## 3) Dry-Run Scope
- Total cases: 24
- Mix:
  - 16 valid submissions
  - 4 invalid schema/runtime submissions
  - 4 adversarial exploit attempts

## 4) Operational Sequence
1. Run readiness checker (`tools/check_phase2_readiness.py`).
2. Prepare dry-run batch from `DRY_RUN_CASES.json`.
3. Execute scoring pipeline over all cases.
4. Execute exploit resistance checks (`EXPLOIT_RESISTANCE.md`).
5. Populate `RESULTS_TEMPLATE.md`.
6. Declare pass/fail and decide Phase 3 launch.

## 5) Required Logs per Case
For each run, record:
- `case_id`
- submission hash
- accepted/rejected status
- rejection reason (if any)
- per-subscore (`P,C,R,L,T`)
- total penalties
- final AGI-META score
- runtime seconds
- peak memory
- deterministic rerun delta

## 6) Risk Escalation Rules
Escalate and block progression if any occur:
- score changes > 0.1 for deterministic rerun,
- rejected reason mismatches expected class,
- private split metadata exposure,
- runtime budget overrun in >= 10% of valid cases.

## 7) Deliverables
- Completed `RESULTS_TEMPLATE.md`
- updated `PHASE2_SUMMARY.md` (to be created after execution)
- issue list of defects grouped by severity (Critical/High/Medium/Low)

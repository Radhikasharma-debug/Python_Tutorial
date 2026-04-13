# AGI-META Benchmark v1.0 — BASELINES

Status: **SPEC LOCK CANDIDATE**

## 1) Required Baseline Set

### A) `accuracy_greedy`
- Objective: maximize final answer accuracy only.
- Behavior: single strategy, minimal monitoring/regulation.
- Expected profile: high `P`, weak `C/R/L/T`.

### B) `calibrated_static`
- Objective: preserve confidence calibration without adaptive switching.
- Behavior: calibrated confidence head, fixed policy.
- Expected profile: moderate `P`, strong `C`, weak `R/L`.

### C) `adaptive_bandit`
- Objective: switch among strategy arms based on online feedback.
- Behavior: bandit controller over action policies.
- Expected profile: moderate `P/C`, stronger `R`.

### D) `reflective_heuristic`
- Objective: improve after failure using structured reflection rules.
- Behavior: deterministic post-episode update heuristics.
- Expected profile: moderate `P/R`, strong `L`.

## 2) Baseline Packaging Requirements
Each baseline must ship with:
- deterministic seed support,
- command-line runner,
- inference log to schema-compatible trace,
- reproducible dependency file.

## 3) Expected Composite Ranges (Calibration Targets)
These are coarse sanity targets for dry runs (not leaderboard guarantees):
- `accuracy_greedy`: 38–52
- `calibrated_static`: 44–58
- `adaptive_bandit`: 50–64
- `reflective_heuristic`: 52–66

## 4) Evaluation Protocol
All baselines are evaluated using same official seeds and environment lock. Report means and 95% bootstrap CIs.

# AGI-META Phase 4 — Robustness Audit Protocol

## 1) Purpose
Validate that top-performing systems remain competent under hidden distribution shift and perturbation bundles, not only under leaderboard-tuned conditions.

## 2) Scope
- Mandatory: Top-10 final private leaderboard submissions.
- Optional extension: Top-25 for research reporting.

## 3) Audit Packs
1. **Shift Pack A (Template Shift):** unseen task templates.
2. **Shift Pack B (Perturbation Combo):** unseen combinations of known perturbations.
3. **Shift Pack C (Objective Timing):** unseen objective-switch timing patterns.
4. **Stress Pack D (Budget Pressure):** strict runtime/token budgets.

## 4) Metrics Captured
- Delta of `P,C,R,L,T` from private-final baseline.
- Composite AGI-META score delta.
- Calibration degradation (`ECE`, `Brier` deltas).
- Rank sensitivity across packs and seeds.

## 5) Pass/Flag Thresholds
- **Pass:** score delta <= 7 points and rank drop <= 3 positions.
- **Watch:** score delta > 7 and <= 12 or rank drop 4–5.
- **Flag:** score delta > 12 or rank drop > 5.

## 6) Required Evidence
For each audited model, include:
- submission id/hash,
- evaluator image digest,
- pack identifier and seed,
- baseline vs audit metric table,
- interpretation note with likely failure mode.

## 7) Decision Rule
A medal position remains valid only if either:
- status is **Pass** across all mandatory packs, or
- status includes **Watch** only with explicit committee sign-off and documented rationale.

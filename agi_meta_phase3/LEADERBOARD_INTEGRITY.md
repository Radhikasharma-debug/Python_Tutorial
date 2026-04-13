# AGI-META Phase 3 — Leaderboard Integrity Controls

## 1) Goals
- Preserve ranking fairness.
- Detect exploitation early.
- Ensure reproducibility of top scores.

## 2) Continuous Checks
1. **Duplicate trace fingerprinting**
   - Detect near-identical submissions across accounts.
2. **Score jump anomaly detection**
   - Flag abrupt improvements above expected envelope.
3. **Calibration/accuracy divergence**
   - Identify suspicious patterns (very high score with implausible calibration profile).
4. **Runtime telemetry consistency**
   - Compare reported budget vs measured resource usage.
5. **Deterministic rerun spot checks**
   - Re-evaluate sampled submissions with same seed.

## 3) Daily Top-K Repro Audit
- Re-run Top 20 submissions daily on fixed evaluation seeds.
- Compare rank deltas and score deltas.
- If score delta > 0.1, mark as audit-fail and investigate.

## 4) Anti-Collusion Heuristics
- shared artifact hash clusters,
- repeated uncommon error signatures,
- synchronized submission timing bursts.

## 5) Enforcement Ladder
1. Warning + clarification request
2. Temporary score hold
3. Submission invalidation
4. Account disqualification

## 6) Evidence Requirements
Any enforcement action must include:
- deterministic evidence artifact,
- policy reference,
- reviewer sign-off (2-person rule for disqualification).

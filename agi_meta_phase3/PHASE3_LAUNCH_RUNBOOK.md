# AGI-META Phase 3 — Live Competition Runbook

Status: **LAUNCH PREP**

## 1) Phase 3 Objective
Operate the public competition window with stable scoring, transparent communication, and continuous integrity monitoring.

## 2) Preconditions (Must Be True)
- Phase 1 lock is active and unchanged.
- Phase 2 dry run has passed all exit criteria.
- Incident commander and on-call rotation are assigned.
- Scoring environment image digest is pinned.

## 3) Launch Sequence (T-24h to T+2h)
1. Freeze evaluator image and publish runtime fingerprint.
2. Enable submission endpoint in limited mode (internal smoke).
3. Run three synthetic canary submissions (valid/invalid/adversarial).
4. Confirm canary expected outcomes and latency budgets.
5. Open public submissions.
6. Publish launch announcement and competition rules digest.
7. Monitor first 2 hours continuously for anomaly spikes.

## 4) Operational SLAs
- Submission queue wait p95 <= 10 minutes.
- Score availability p95 <= 20 minutes from enqueue.
- Incident acknowledgment <= 15 minutes.
- Public status update cadence <= 60 minutes during critical incidents.

## 5) Daily Cadence
- 00:00 UTC: leaderboard integrity batch checks.
- 08:00 UTC: moderator triage review.
- 16:00 UTC: score distribution drift report.
- 23:00 UTC: daily summary log and action items.

## 6) Hard Stop Conditions
Trigger temporary submission pause if any occur:
- deterministic rerun mismatch above 0.1 score points in canary set,
- private-split leakage evidence,
- exploit bypass with unfair ranking impact,
- sustained queue p95 above 30 minutes for 2 consecutive hours.

## 7) Required Outputs
- `PHASE3_DAILY_LOG.md` (append-only)
- `INCIDENT_LOG.md` (all sev levels)
- `LEADERBOARD_AUDIT_LOG.md` (daily integrity checks)

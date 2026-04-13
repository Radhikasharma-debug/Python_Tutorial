# AGI-META Phase 3 — Daily Ops Checklist

## Start of Day
- [ ] Confirm evaluator image digest unchanged.
- [ ] Verify queue and scoring services healthy.
- [ ] Run canary trio (valid, invalid, adversarial).
- [ ] Review unresolved incidents.

## Midday
- [ ] Review anomaly dashboard.
- [ ] Sample deterministic reruns from Top 20.
- [ ] Validate score distribution drift within expected band.

## End of Day
- [ ] Publish daily summary in `PHASE3_DAILY_LOG.md`.
- [ ] Update `LEADERBOARD_AUDIT_LOG.md` with audit outcomes.
- [ ] Carry over action items and on-call handoff.

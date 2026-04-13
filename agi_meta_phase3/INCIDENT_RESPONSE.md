# AGI-META Phase 3 — Incident Response Playbook

## 1) Severity Levels
- **SEV-1**: fairness/security compromised (active leakage/exploit bypass)
- **SEV-2**: scoring reliability degraded (widespread failures or queue collapse)
- **SEV-3**: partial feature issues (isolated failures, limited impact)
- **SEV-4**: cosmetic/non-blocking

## 2) Response Timeline Targets
- SEV-1 acknowledge: 15 min; mitigation: 60 min
- SEV-2 acknowledge: 30 min; mitigation: 4 h
- SEV-3 acknowledge: 4 h; mitigation: 24 h

## 3) SEV-1 Immediate Actions
1. Pause submissions.
2. Snapshot logs and evaluator image digest.
3. Disable suspected exploit path.
4. Run canary reruns on fixed seeds.
5. Publish public status note with ETA.

## 4) Incident Record Schema
Required fields:
- incident_id
- detected_at_utc
- severity
- impact_summary
- suspected_root_cause
- mitigations_applied
- participant_communication_link
- postmortem_due_date

## 5) Postmortem Requirements
Within 72 hours of closure include:
- root cause,
- timeline,
- corrective actions,
- prevention controls,
- policy/document updates.

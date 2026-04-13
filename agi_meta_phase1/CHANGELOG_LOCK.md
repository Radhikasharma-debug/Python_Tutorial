# AGI-META Phase 1 Lock Changelog

## v1.0.0 — Spec Lock Declaration
- Lock timestamp (UTC): 2026-04-13T00:00:00Z
- Scope: `SPEC.md`, `METRICS.md`, `SCHEMA.json`, `SPLITS.md`, `BASELINES.md`, `EVAL_RULES.md`, `SEEDS.yaml`
- Rationale: establish stable benchmark contract before dry-run (Phase 2).

## Change Policy After Lock
Any post-lock change must include:
1. semantic version increment,
2. date and rationale,
3. impacted files,
4. reproducibility/comparability impact note,
5. migration guidance if participant-facing.

## Compatibility Categories
- Patch (`v1.0.x`): typo/clarification only, no scoring logic change.
- Minor (`v1.x.0`): additive changes with compatibility preserved.
- Major (`vX.0.0`): scoring/split/protocol changes that break comparability.

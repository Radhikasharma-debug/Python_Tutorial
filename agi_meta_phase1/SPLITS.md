# AGI-META Benchmark v1.0 — SPLITS

Status: **SPEC LOCK CANDIDATE**

## 1) Official Ratios
- Train: 60%
- Public leaderboard: 20%
- Private leaderboard: 20%

## 2) Hidden Axes for Private Split
Private split must differ by all dimensions below:
1. task templates unseen in train/public,
2. unseen perturbation combinations,
3. unseen objective-switch timing profiles.

## 3) Generation Rules
- Split generation is seed-driven (`SEEDS.yaml`).
- No template id may appear across split boundaries.
- No isomorphic pair may be split between public and private.
- Similarity guardrail: semantic similarity between public/private prompts must remain below threshold 0.82 using organizer embedding model.

## 4) Leakage Controls
- Store private template registry in non-public artifact.
- Publish only aggregate family counts for private split.
- Validate disjointness with structural hash and semantic threshold checks.

## 5) Audit Checklist
Before leaderboard open:
- [ ] template id disjointness check passed
- [ ] perturbation combination disjointness check passed
- [ ] objective-switch profile disjointness check passed
- [ ] semantic leakage threshold check passed

## 6) Versioning
Any split regeneration after lock requires:
- split version increment,
- reason, date, and impacted benchmark comparability note.

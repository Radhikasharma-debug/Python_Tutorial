# AGI-META Benchmark v1.0 — SPEC

Status: **SPEC LOCK CANDIDATE**  
Scope: Phase 1 foundation for Kaggle hackathon benchmark construction.

## 1) Purpose
AGI-META evaluates metacognitive capability in task-solving systems across five dimensions:
- Planning
- Monitoring
- Regulation under shift
- Reflection-driven learning
- Cross-domain transfer

The benchmark score must reward robust adaptive cognition, not endpoint accuracy alone.

## 2) Episode Lifecycle (Frozen)
Each episode runs in six ordered phases.

1. **Plan**: system proposes a task plan and step-level confidence.
2. **Act**: system executes plan steps.
3. **Monitor checkpoints**: system reports confidence and action decision (`continue`/`switch`/`request_info`).
4. **Shift event** (optional): environment may inject controlled perturbation.
5. **Reflect**: system writes failure diagnosis and update rule.
6. **Transfer probe**: system solves an isomorphic task variant.

### Episode limits
- `max_plan_steps`: 8
- `max_act_steps`: 20
- `monitor_interval`: every 3 act steps (minimum 3 checkpoints per full episode)
- `max_reflection_tokens`: 220
- `confidence_range`: closed interval [0.0, 1.0]

## 3) Task Families (Frozen Taxonomy)
All episodes belong to one of the following families.

1. **Symbolic reasoning**
2. **Constrained planning**
3. **Noisy inference**
4. **Tool-use sequencing**
5. **Objective-switch adaptation**

For each family, organizers must maintain:
- canonical input schema,
- canonical output schema,
- deterministic validator,
- perturbation compatibility matrix.

## 4) Perturbation Library (Frozen)
Permitted perturbations:
- `distractor_injection`
- `context_truncation`
- `objective_flip`
- `delayed_feedback`
- `tool_dropout`

### Severity levels
- `low`
- `medium`
- `high`

### Injection policy constraints
- Max perturbations per episode: 2
- At most one `high` severity event per episode
- `objective_flip` only after first monitor checkpoint

## 5) Allowed Agent Actions (Frozen)
Trace action types are limited to:
- `plan`
- `act`
- `check`
- `switch`
- `reflect`

Runtime control decisions at monitor points are limited to:
- `continue`
- `switch`
- `request_info`

## 6) Data Splits (Contract)
- Train: 60%
- Public leaderboard: 20%
- Private leaderboard: 20%

Private split must differ from public/train by all three hidden axes:
1. unseen templates,
2. unseen perturbation pairings,
3. unseen objective-switch timing profiles.

## 7) Determinism and Reproducibility
Scoring runs must be deterministic under official seed bundle (`SEEDS.yaml`) and pinned environment.

## 8) Governance
Once lock is declared in `CHANGELOG_LOCK.md`, any modification to this spec requires:
1. version bump,
2. explicit rationale,
3. effective date,
4. impact statement on comparability.

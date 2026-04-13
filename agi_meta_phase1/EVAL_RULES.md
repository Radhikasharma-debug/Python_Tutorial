# AGI-META Benchmark v1.0 — EVAL_RULES

Status: **SPEC LOCK CANDIDATE**

## 1) Runtime Limits
- Max wall-clock time per submission: 90 minutes
- Max RAM: 16 GB
- Max per-episode execution time: 25 seconds

## 2) Environment Constraints
- Offline scoring environment (no internet during evaluation)
- Pinned runtime image and package versions
- Python version pinned in environment file

## 3) Determinism Requirements
- Submission must be deterministic under `seed_used`.
- Repeated evaluation under same seed must reproduce identical outputs bitwise where feasible.

## 4) Disallowed Behaviors
- External API calls during evaluation
- Access to private split metadata
- Hard-coded answer lookup tables keyed by episode ids
- Non-declared model artifacts downloaded at runtime

## 5) Validation and Rejection
Submission is rejected if:
- schema validation fails,
- runtime/resource limits exceeded,
- deterministic rerun check fails,
- prohibited behavior detected.

## 6) Logging Requirements
Evaluator records:
- submission hash,
- scoring seed,
- runtime stats,
- validator warnings/errors,
- final subscores and penalties.

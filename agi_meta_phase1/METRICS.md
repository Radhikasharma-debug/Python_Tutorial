# AGI-META Benchmark v1.0 — METRICS

Status: **SPEC LOCK CANDIDATE**

## 1) Composite Score
All subscores are normalized to [0, 100].

\[
\text{AGI-META} = 0.30P + 0.20C + 0.20R + 0.15L + 0.15T - \text{Penalties}
\]

Where:
- `P` = task performance
- `C` = calibration and monitoring quality
- `R` = regulation under shift
- `L` = reflection-driven learning efficiency
- `T` = cross-domain transfer

## 2) Subscore Definitions

### 2.1 Performance `P`
\[
P = 100 \cdot (0.7 \cdot \text{success_rate} + 0.3 \cdot \text{quality_margin})
\]

- `success_rate`: fraction of valid correct final answers.
- `quality_margin`: normalized closeness/utility metric from task validators.

### 2.2 Calibration/Monitoring `C`
\[
C = 100 \cdot (0.5 \cdot (1-\text{ECE}) + 0.3 \cdot (1-\text{Brier}) + 0.2 \cdot \rho_{conf,correct})
\]

Values clipped to [0,1] before scaling.

### 2.3 Regulation `R`
\[
R = 100 \cdot (0.5 \cdot (1-\text{regret_norm}) + 0.5 \cdot (1-\text{recovery_steps_norm}))
\]

- `regret_norm`: normalized excess loss after perturbation.
- `recovery_steps_norm`: normalized steps until pre-shift performance recovered.

### 2.4 Learning Efficiency `L`
\[
L = 100 \cdot \text{clip}\left(\frac{\Delta_{reflect} - \Delta_{retest}}{\text{budget_norm}+\epsilon}, 0, 1\right)
\]

- `Δ_reflect`: gain after reflection update.
- `Δ_retest`: gain from simple repeat without reflection signal.
- `budget_norm`: normalized token/compute budget used in reflection.

### 2.5 Transfer `T`
\[
T = 100 \cdot (0.7 \cdot \text{heldout_success} + 0.3 \cdot (1-\text{calibration_drift}))
\]

## 3) Penalties

### 3.1 Overconfidence penalty
\[
\text{pen}_{over} = 20 \cdot \max(0, \overline{conf_{wrong}} - 0.6)
\]

### 3.2 Non-adaptive repetition penalty
\[
\text{pen}_{rep} = 10 \cdot \text{repeat_ratio_after_failure}
\]

### 3.3 Budget overrun penalty
\[
\text{pen}_{budget} = 15 \cdot \text{overrun_fraction}
\]

\[
\text{Penalties} = \text{pen}_{over} + \text{pen}_{rep} + \text{pen}_{budget}
\]

Final score clipped to [0,100].

## 4) Tie-breakers (Frozen Order)
1. Higher `T`
2. Higher `C`
3. Lower normalized budget
4. Earlier submission timestamp

## 5) Statistical Reporting
For official leaderboard reports:
- bootstrap 95% CI (>= 1000 resamples),
- per-module subscore table,
- seed sensitivity over official eval seeds.

# Epic 122: RL360 Global Scaling

This study package is the self-contained documentation artifact for RL360 epic `#122`.
It stays inside `docs/k2-aic-exhaustive-study` and does not depend on `scripts/analysis/*`.

## Scope

- data and tables: [sections/122-data-and-tables.md](sections/122-data-and-tables.md)
- figures: [sections/122-figures.md](sections/122-figures.md)
- narrative: [sections/122-narrative.md](sections/122-narrative.md)

## Provenance

The artifacts are derived from the local AIConfigurator catalogs captured on `2026-04-23`:

- `/mnt/weka/shrd/k2m/micah.villmow/aiconfigurator/qwen35_397b_a17b/20260423T221500Z_rl_pow2_512_unfiltered`
- `/mnt/weka/shrd/k2m/micah.villmow/aiconfigurator/qwen35_397b_a17b/20260423T221500Z_rl_pow2_512_unfiltered_retry_stress256`

The first catalog covers `practical_32k_8k`, `practical_64k_8k`, and `stress_128k_16k`.
The retry catalog records the all-scale `stress_256k_32k` no-results boundary.

## High-Level Result

The agg topology is the global default for this epic.
Disagg has a narrow mid-scale win region, but it wins cluster throughput in only `4` of `27` supported head-to-head comparisons and the `256K` stress profile has no viable agg or disagg candidate at any tested scale.

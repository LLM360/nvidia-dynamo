# Epic 122 Narrative

This narrative summarizes the RL360 global-scaling findings from the local AIConfigurator catalogs dated `2026-04-23`.

## Findings

1. The agg path is globally stable.
   The selected agg layout is a repeated `8`-GPU serving replica, so cluster throughput scales linearly from `1n` through `512n` for every supported RL profile in this epic.

2. Disagg wins only in a narrow mid-scale window.
   Across the `27` supported agg-vs-disagg comparisons, disagg wins cluster throughput `4` times (`14.8%`): `practical_32k_8k` at `4n`, `8n`, and `16n`, plus `stress_128k_16k` at `8n`.

3. The strongest disagg win is still localized.
   The best head-to-head result is `practical_32k_8k` at `8n`, where disagg reaches a `1.422x` cluster-throughput ratio over agg.
   The stress-tier win is much smaller: `stress_128k_16k` reaches only `1.057x` at `8n`.

4. Practical `64K/8K` never flips to disagg.
   `practical_64k_8k` has zero disagg cluster-throughput wins; its best ratio is `0.870x` at `8n`, and the geometric-mean ratio is `0.202x`.

5. Disagg plateaus early.
   For every supported RL profile, disagg peaks by `16n` and then flattens, while agg keeps scaling linearly.
   The disagg peak-to-baseline ratios are `13.000x` for `practical_32k_8k`, `9.987x` for `practical_64k_8k`, and `12.071x` for `stress_128k_16k`.

6. Selected-GPU efficiency is better than cluster wins suggest, but not enough to change the default.
   Disagg wins selected-GPU efficiency `5` times (`18.5%`), including `stress_128k_16k` at `16n`, where it loses on cluster throughput (`0.911x`) but still beats agg on active-GPU efficiency (`1.041x`) because it leaves `12.5%` of the allocation idle.

7. The `256K` stress tier is outside the current supported envelope.
   `stress_256k_32k` returns `no_results` for both agg and disagg at every tested scale from `1n` through `512n`.

## Recommendation

Use agg as the default topology for global rollout planning in this epic.
Treat disagg as a targeted option for `practical_32k_8k` at `4n` to `16n`, and as a one-point stress exception at `stress_128k_16k` `8n`.
Do not plan around `stress_256k_32k` until the missing estimator and cache-coverage path is fixed upstream.

# Epic 122 Data And Tables

This section packages the derived tables for the RL360 global-scaling sweep.
All TSV artifacts are epic-scoped and live under `data/122_*`.

## Source Artifacts

- `data/122_global_scaling_points.tsv`: one row per `workload_profile x node_count x topology`, including cluster throughput, per-user throughput, allocated-GPU efficiency, selected-GPU efficiency, and topology shape.
- `data/122_topology_head_to_head.tsv`: paired agg-vs-disagg comparisons for each scale where both topologies produced candidate manifests.
- `data/122_topology_win_rates.tsv`: win-rate and ratio rollups by workload profile, workload tier, and overall.
- `data/122_scaling_summary.tsv`: baseline, peak, and final scale summaries for each topology.
- `data/122_stress256_boundary.tsv`: the 256K stress boundary, where both topologies returned `no_results` at every tested scale.

## Topology Win Rates

| Scope | Comparisons | Disagg cluster wins | Disagg cluster win rate | Disagg selected-GPU efficiency win rate | Geometric mean cluster ratio |
| --- | ---: | ---: | ---: | ---: | ---: |
| `practical_32k_8k` | 9 | 3 | 33.3% | 33.3% | 0.394 |
| `practical_64k_8k` | 9 | 0 | 0.0% | 0.0% | 0.202 |
| `stress_128k_16k` | 9 | 1 | 11.1% | 22.2% | 0.278 |
| `overall` | 27 | 4 | 14.8% | 18.5% | 0.281 |

## Peak Scaling Summary

| Workload profile | Topology | Baseline node | Peak node | Peak cluster tokens/s | Peak vs baseline | Final vs peak |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `practical_32k_8k` | `agg` | 1 | 512 | 375156.224 | 512.000x | 1.000x |
| `practical_32k_8k` | `disagg` | 2 | 16 | 15480.259 | 13.000x | 1.000x |
| `practical_64k_8k` | `agg` | 1 | 512 | 259949.056 | 512.000x | 1.000x |
| `practical_64k_8k` | `disagg` | 2 | 16 | 5042.995 | 9.987x | 1.000x |
| `stress_128k_16k` | `agg` | 1 | 512 | 178919.424 | 512.000x | 1.000x |
| `stress_128k_16k` | `disagg` | 2 | 16 | 5094.769 | 12.071x | 0.994x |

## 256K Boundary

`stress_256k_32k` is a clean all-scale boundary in this epic dataset.
`data/122_stress256_boundary.tsv` records `agg_status=no_results` and `disagg_status=no_results` for every tested scale from `1n` through `512n`.

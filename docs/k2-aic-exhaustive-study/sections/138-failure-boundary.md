# K2 Failure Boundary And No-Result Analysis

## Scope

This section analyzes the safe derived K2 exhaustive AIConfigurator sweep for `h200_sxm + sglang 0.5.9` and asks a narrow question: where do no-result regions represent a stable unsupported topology boundary, and where do they represent a harder backend failure that should block planning outright?

The checked-in derived dataset merges two local catalogs:

- the additive batch-band sweep over node counts `1, 2, 4, 8, 16, 32, 64, 128, 256, 512`
- the intermediate-node backfill over node counts `144, 160, 176, 192, 208, 224, 240`

That merge yields `10,200` topology rows and `5,100` agg/disagg boundary cells in [../data/138_failure_boundary_cells.tsv](../data/138_failure_boundary_cells.tsv).

## Boundary Taxonomy

The no-result region is not uniform. The derived tables normalize the sweep into three boundary classes:

| Boundary class | Cells | Ratio | Meaning |
| --- | ---: | ---: | --- |
| `supported_both` | 4560 | 89.4% | Both agg and disagg emit candidates. |
| `unsupported_disagg` | 285 | 5.6% | Agg emits a candidate, but single-node disagg emits no result CSV. |
| `failed_both` | 255 | 5.0% | Both topologies collapse into the non-wideep SGLang `TP>1 && DP>1` guard path. |

Those counts are summarized in [../data/138_failure_boundary_overview.tsv](../data/138_failure_boundary_overview.tsv) and visualized in [../figures/138_failure_boundary_mix_heatmap.png](../figures/138_failure_boundary_mix_heatmap.png).

## What The Boundary Actually Says

Two qualitatively different regions appear in the sweep:

1. The disaggregated topology is unsupported at exactly one node for every non-`stress_256k` profile.
2. The `stress_256k` profile fails across every sampled node count and every sampled load cell.

The distinction matters because it changes the operational recommendation:

- The single-node disagg region should be treated as an unsupported planning boundary, not as evidence that the entire workload shape is invalid.
- The `stress_256k` region should be treated as a hard failure boundary until the backend guard or estimator coverage changes.

The topology-specific unsupported view in [../figures/138_disagg_unsupported_ratio_heatmap.png](../figures/138_disagg_unsupported_ratio_heatmap.png) makes the first point explicit: unsupported disagg is concentrated at `1` node and disappears immediately at `2` nodes.

The ratio view in [../figures/138_failure_unsupported_ratio_pointcloud.png](../figures/138_failure_unsupported_ratio_pointcloud.png) shows that almost every node/context bucket is fully supported, with only three nonzero ratio states:

- `unsupported=1.00, failure=0.00` for the single-node non-`256K` unsupported strip
- `unsupported=0.80, failure=0.20` for the single-node `256K` mixed bucket
- `unsupported=0.00, failure=0.20` for every multi-node `256K` bucket

## Profile-Level Findings

Every profile except `stress_256k` follows the same pattern in [../data/138_failure_boundary_profile_summary.tsv](../data/138_failure_boundary_profile_summary.tsv):

- `240 / 255` cells are fully supported
- `15 / 255` cells are single-node disagg no-results
- `0 / 255` cells are hard failures

`stress_256k` is the lone outlier:

- `0 / 255` cells are supported
- `0 / 255` cells land in the disagg-only unsupported category
- `255 / 255` cells fail

This means the apparent `256K` boundary is not a generic "all 256K contexts are broken" result. `balanced_256k` and the other `~256K` observed-context profiles remain launchable above one node. The failure boundary is much narrower: it is tied to the preserved `stress_256k` shape with `isl=229376` and `osl=32768`.

## Implications For Measured Follow-Up

This boundary study suggests three concrete follow-ups for measured runtime work:

- Exclude single-node disagg from measured comparisons unless the goal is explicitly to validate the unsupported region.
- Sample directly around the `128K -> 256K` stress transition, because `stress_128k` is stable while `stress_256k` fails everywhere.
- Keep the `stress_256k` failure mode separate from ordinary unsupported planning gaps so that future estimator or backend fixes can be evaluated against a clean baseline.

In short, the safe derived sweep does not show a broad collapse of K2 AIConfigurator coverage. It shows one narrow topology boundary and one preserved hard-failure lane. Treating those as separate planning outputs is the key result of epic `#138`.

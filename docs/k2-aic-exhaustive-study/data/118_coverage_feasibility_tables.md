# Epic 118 Coverage And Feasibility Tables

Generated from the local AIConfigurator manifest catalogs and validation summaries referenced in the section narrative.

## Coverage And Feasibility Ratios

| Workload | Experiment | Covered / Total Nodes | Coverage Ratio | Feasible / Total Nodes | Feasibility Ratio | Feasibility Given Coverage | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Practical RL 32K/8K | agg | 10 / 10 | 1.000 | 10 / 10 | 1.000 | 1.000 | launchable manifest closes raw script gap |
| Practical RL 32K/8K | disagg | 9 / 10 | 0.900 | 0 / 10 | 0.000 | 0.000 | coverage exists above 1n, but raw manifests are cross-node rather than node-local |
| Practical RL 64K/8K | agg | 10 / 10 | 1.000 | 10 / 10 | 1.000 | 1.000 |  |
| Practical RL 64K/8K | disagg | 9 / 10 | 0.900 | 9 / 10 | 0.900 | 1.000 |  |
| Stress RL 128K/16K | agg | 10 / 10 | 1.000 | 10 / 10 | 1.000 | 1.000 |  |
| Stress RL 128K/16K | disagg | 9 / 10 | 0.900 | 9 / 10 | 0.900 | 1.000 |  |
| Stress RL 256K/32K | agg | 0 / 10 | 0.000 | 0 / 10 | 0.000 | 0.000 |  |
| Stress RL 256K/32K | disagg | 0 / 10 | 0.000 | 0 / 10 | 0.000 | 0.000 |  |

## Validation Evidence

| Label | Experiment | Nodes | Attempted | Succeeded | Success Ratio | Batch Req/s | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| agg_1n_local_sharedrootfs | agg | 1 | 32 | 32 | 1.0000 | 8.06 | Local one-node agg rerun using shared rootfs. |
| agg_4n_slurm_baseline | agg | 4 | 32 | 32 | 1.0000 | 4.12 | Four-node agg baseline validation. |
| disagg_4n_small_batch | disagg | 4 | 32 | 32 | 1.0000 | 1.72 | Direct AIC disagg candidate validated on a 32-request batch. |
| disagg_4n_batch8000_partial | disagg | 4 | 8000 | 1932 | 0.2415 | 2.87 | First 8k-request batch run showed partial connect-timeout failures. |
| disagg_4n_batch8000_tuned | disagg | 4 | 8000 | 8000 | 1.0000 | 6.58 | Tuned node-local disagg manifest completed the full 8k-request batch. |
| disagg_4n_batch8000_rebuilt | disagg | 4 | 8000 | 8000 | 1.0000 | 6.69 | Rebuilt tuned manifest also completed the full 8k-request batch. |

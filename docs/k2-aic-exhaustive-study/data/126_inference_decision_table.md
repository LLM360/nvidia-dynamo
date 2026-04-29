# Epic 126 Inference Decision Table

- Source catalog: `/mnt/weka/home/micah.villmow/nvidia/dynamo/.aic_local_logs/k2moe375b_xllm_h200/aiconfigurator/20260427T172219Z_k2_additive_batch_band_full/catalog/selected_points.tsv`
- Load bands considered: `15` (`load_000001` .. `load_016384`)
- Observation: every profile/node/topology selection is invariant across the 15 load bands in this additive catalog, so the table below collapses to the unique inference frontier.

| Profile | Context | Verdict | Disagg-winning nodes (`tok/s/user`) | Agg-winning nodes | Missing disagg nodes | User ratio range | GPU ratio range | Cluster ratio range |
|---|---:|---|---|---|---|---:|---:|---:|
| Balanced 128K (`balanced_128k`) | 131072 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 1.659..1.659 | 0.415..0.778 | 0.415..0.778 |
| Balanced 16K (`balanced_16k`) | 16384 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.929..0.929 | 0.492..0.922 | 0.492..0.922 |
| Balanced 1K (`balanced_1k`) | 1024 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 1.007..1.007 | 0.495..0.743 | 0.495..0.743 |
| Balanced 256K (`balanced_256k`) | 262144 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.540..0.540 | 0.662..1.242 | 0.662..1.242 |
| Balanced 2K (`balanced_2k`) | 2048 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.996..0.996 | 0.489..0.856 | 0.489..0.856 |
| Balanced 32K (`balanced_32k`) | 32768 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.923..0.923 | 0.467..0.875 | 0.467..0.875 |
| Balanced 4K (`balanced_4k`) | 4096 | mixed | 8 | 2,4,16,32,64,128,256,512 | 1 | 0.978..1.017 | 0.471..0.766 | 0.471..0.766 |
| Balanced 64K (`balanced_64k`) | 65536 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 2.140..2.140 | 0.415..0.777 | 0.415..0.777 |
| Balanced 8K (`balanced_8k`) | 8192 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.939..0.960 | 0.459..0.847 | 0.459..0.839 |
| Chat 4K / 500 (`chat_4k_500`) | 4500 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 1.377..1.412 | 0.618..0.672 | 0.618..0.661 |
| 7K / 128K (`observed_high_7k_128k`) | 138240 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 2.661..2.661 | 0.384..0.720 | 0.384..0.720 |
| 7K / 1K (`observed_high_7k_1k`) | 8192 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 1.169..1.215 | 0.565..0.781 | 0.565..0.774 |
| 0.5K / 128K (`observed_low_0p5k_128k`) | 131584 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 3.495..3.495 | 0.362..0.679 | 0.362..0.679 |
| 0.5K / 1K (`observed_low_0p5k_1k`) | 1536 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.890..0.942 | 0.500..0.889 | 0.500..0.875 |
| 1.5K / 128K (`observed_mean_1p5k_128k`) | 132608 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 3.498..3.498 | 0.363..0.681 | 0.363..0.681 |
| 1.5K / 1K (`observed_mean_1p5k_1k`) | 2560 | disagg | 2,4,8,16,32,64,128,256,512 | - | 1 | 1.028..1.065 | 0.485..0.728 | 0.485..0.721 |
| 32K / 8K (`practical_32k_8k`) | 40960 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.944..0.944 | 0.489..0.916 | 0.489..0.916 |
| 64K / 8K (`practical_64k_8k`) | 73728 | agg | - | 2,4,8,16,32,64,128,256,512 | 1 | 0.831..0.831 | 0.469..0.862 | 0.469..0.853 |
| 128K profile (`stress_128k`) | 131072 | mixed | 16,32,64 | 2,4,8,128,256,512 | 1 | 0.745..1.338 | 0.485..0.901 | 0.485..0.887 |
| 256K profile (`stress_256k`) | 262144 | no_disagg_candidate | - | - | 1,2,4,8,16,32,64,128,256,512 | -..- | -..- | -..- |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-01)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-01 | 03:13:33 | `cad3569b7` |
| Baseline  | 2025-09-30 | 03:29:47 | `a38485468` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.36% (-7.6%)                                                                                                                    | 4.94% (-14.6%)                                                                                                                                                 | 8.39% (+3.8%)                                                                                                                                                    |
| CPU Max               | 111.04% (-1.9%)                                                                                                                  | 111.29% (-6.7%)                                                                                                                                                | 113.82% (-9.5%)                                                                                                                                                  |
| RAM Median            | 44.11 MB (-0.3%)                                                                                                                 | 65.19 MB (+6.6%)                                                                                                                                               | 65.84 MB (-0.2%)                                                                                                                                                 |
| RAM Max               | 47.17 MB (-16.9%)                                                                                                                | 69.54 MB (-4.4%)                                                                                                                                               | 79.96 MB (-0.9%)                                                                                                                                                 |
| RX Total              | 103.0 KB (-0.6%)                                                                                                                 | 2.11 MB (-0.0%)                                                                                                                                                | 3.07 MB (-5.0%)                                                                                                                                                  |
| TX Total              | 587.5 KB (-1.0%)                                                                                                                 | 3.49 MB (-0.5%)                                                                                                                                                | 5.16 MB (-2.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251001T031333_cad3569b7/test_idle[waku_light_client_True]-20251001-030606.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251001T031333_cad3569b7/test_one_to_one_messages[waku_light_client_True]-20251001-031247.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251001T031333_cad3569b7/test_one_to_one_messages[waku_light_client_False]-20251001-030923.png) |

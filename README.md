# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-23)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-23 | 03:11:34 | `620d96c7a` |
| Baseline  | 2025-09-22 | 03:09:13 | `7c3969b92` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.32% (-0.4%)                                                                                                                    | 5.01% (-14.3%)                                                                                                                                                 | 8.20% (+3.6%)                                                                                                                                                    |
| CPU Max               | 139.11% (+27.9%)                                                                                                                 | 141.27% (-10.3%)                                                                                                                                               | 107.47% (-1.0%)                                                                                                                                                  |
| RAM Median            | 45.93 MB (+10.0%)                                                                                                                | 62.08 MB (-3.1%)                                                                                                                                               | 65.65 MB (+1.3%)                                                                                                                                                 |
| RAM Max               | 48.16 MB (-5.7%)                                                                                                                 | 69.08 MB (-3.2%)                                                                                                                                               | 80.71 MB (+1.7%)                                                                                                                                                 |
| RX Total              | 102.7 KB (+11.4%)                                                                                                                | 2.09 MB (+0.7%)                                                                                                                                                | 3.26 MB (+3.0%)                                                                                                                                                  |
| TX Total              | 587.0 KB (+0.3%)                                                                                                                 | 3.51 MB (+0.2%)                                                                                                                                                | 5.27 MB (+2.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250923T031134_620d96c7a/test_idle[waku_light_client_True]-20250923-030401.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250923T031134_620d96c7a/test_one_to_one_messages[waku_light_client_True]-20250923-031044.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250923T031134_620d96c7a/test_one_to_one_messages[waku_light_client_False]-20250923-030720.png) |

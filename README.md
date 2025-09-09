# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-09)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-09 | 03:12:16 | `e8dbb93f5` |
| Baseline  | 2025-09-08 | 03:11:17 | `c575471b4` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.17% (+1.2%)                                                                                                                    | 6.05% (+8.6%)                                                                                                                                                  | 8.63% (+7.9%)                                                                                                                                                    |
| CPU Max               | 135.00% (-9.0%)                                                                                                                  | 137.85% (+6.6%)                                                                                                                                                | 150.36% (-2.2%)                                                                                                                                                  |
| RAM Median            | 52.29 MB (+3.4%)                                                                                                                 | 75.20 MB (-1.1%)                                                                                                                                               | 74.52 MB (-1.7%)                                                                                                                                                 |
| RAM Max               | 55.51 MB (+9.8%)                                                                                                                 | 85.65 MB (-1.7%)                                                                                                                                               | 89.21 MB (-1.2%)                                                                                                                                                 |
| RX Total              | 89.9 KB (-5.0%)                                                                                                                  | 2.08 MB (+0.4%)                                                                                                                                                | 3.11 MB (-1.4%)                                                                                                                                                  |
| TX Total              | 568.7 KB (-1.3%)                                                                                                                 | 3.45 MB (+0.2%)                                                                                                                                                | 5.21 MB (+0.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250909T031216_e8dbb93f5/test_idle[waku_light_client_True]-20250909-030502.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250909T031216_e8dbb93f5/test_one_to_one_messages[waku_light_client_True]-20250909-031134.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250909T031216_e8dbb93f5/test_one_to_one_messages[waku_light_client_False]-20250909-030817.png) |

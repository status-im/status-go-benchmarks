# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-11)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-11 | 03:14:24 | `edf7ca6ac` |
| Baseline  | 2025-09-10 | 03:14:38 | `c827909c8` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.15% (+0.7%)                                                                                                                    | 5.73% (-3.2%)                                                                                                                                                  | 7.46% (+0.2%)                                                                                                                                                    |
| CPU Max               | 112.96% (+1.0%)                                                                                                                  | 145.99% (-6.2%)                                                                                                                                                | 110.11% (-41.9%)                                                                                                                                                 |
| RAM Median            | 45.45 MB (+7.7%)                                                                                                                 | 65.56 MB (-2.1%)                                                                                                                                               | 66.07 MB (+0.7%)                                                                                                                                                 |
| RAM Max               | 54.01 MB (-1.1%)                                                                                                                 | 79.08 MB (-1.7%)                                                                                                                                               | 78.07 MB (-2.5%)                                                                                                                                                 |
| RX Total              | 91.6 KB (+0.3%)                                                                                                                  | 2.03 MB (-0.6%)                                                                                                                                                | 3.08 MB (+1.6%)                                                                                                                                                  |
| TX Total              | 585.7 KB (+0.9%)                                                                                                                 | 3.41 MB (-0.0%)                                                                                                                                                | 5.15 MB (-0.4%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250911T031424_edf7ca6ac/test_idle[waku_light_client_True]-20250911-030703.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250911T031424_edf7ca6ac/test_one_to_one_messages[waku_light_client_True]-20250911-031342.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250911T031424_edf7ca6ac/test_one_to_one_messages[waku_light_client_False]-20250911-031021.png) |

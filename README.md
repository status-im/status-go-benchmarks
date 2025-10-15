# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-15)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-15 | 03:10:48 | `c0f75d670` |
| Baseline  | 2025-10-14 | 03:11:36 | `b3af09533` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.60% (+9.8%)                                                                                                                    | 6.02% (-2.3%)                                                                                                                                                  | 8.85% (+8.4%)                                                                                                                                                    |
| CPU Max               | 136.84% (-14.8%)                                                                                                                 | 154.22% (+18.4%)                                                                                                                                               | 178.79% (+46.0%)                                                                                                                                                 |
| RAM Median            | 48.22 MB (+12.3%)                                                                                                                | 65.63 MB (-1.1%)                                                                                                                                               | 67.49 MB (-1.0%)                                                                                                                                                 |
| RAM Max               | 54.22 MB (-0.8%)                                                                                                                 | 85.75 MB (-3.9%)                                                                                                                                               | 88.95 MB (-2.2%)                                                                                                                                                 |
| RX Total              | 102.9 KB (+0.0%)                                                                                                                 | 2.03 MB (+2.9%)                                                                                                                                                | 2.92 MB (-20.2%)                                                                                                                                                 |
| TX Total              | 582.7 KB (-1.3%)                                                                                                                 | 3.35 MB (+0.8%)                                                                                                                                                | 5.25 MB (-3.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251015T031048_c0f75d670/test_idle[waku_light_client_True]-20251015-030341.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251015T031048_c0f75d670/test_one_to_one_messages[waku_light_client_True]-20251015-031002.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251015T031048_c0f75d670/test_one_to_one_messages[waku_light_client_False]-20251015-030649.png) |

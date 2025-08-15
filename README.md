# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-15)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-15 | 21:50:18 | `dfaefeb7a` |
| Baseline  | 2025-08-15 | 11:55:37 | `8a4afcc6c` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.49% (+17.1%)                                                                                                                   | 6.03% (-6.1%)                                                                                                                                                  | 6.41% (+15.7%)                                                                                                                                                   |
| CPU Max               | 156.62% (+13.5%)                                                                                                                 | 153.63% (-9.2%)                                                                                                                                                | 111.86% (-24.1%)                                                                                                                                                 |
| RAM Median            | 51.54 MB (+3.5%)                                                                                                                 | 78.44 MB (+5.1%)                                                                                                                                               | 77.56 MB (+0.3%)                                                                                                                                                 |
| RAM Max               | 51.54 MB (+3.0%)                                                                                                                 | 90.21 MB (+3.1%)                                                                                                                                               | 90.47 MB (+1.5%)                                                                                                                                                 |
| RX Total              | 88.4 KB (-0.1%)                                                                                                                  | 2.03 MB (-1.3%)                                                                                                                                                | 2.00 MB (+0.6%)                                                                                                                                                  |
| TX Total              | 567.1 KB (-0.1%)                                                                                                                 | 3.32 MB (-2.2%)                                                                                                                                                | 3.82 MB (+1.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250815T215018_dfaefeb7a/test_idle[waku_light_client_True]-20250815-214318.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250815T215018_dfaefeb7a/test_one_to_one_messages[waku_light_client_True]-20250815-214937.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250815T215018_dfaefeb7a/test_one_to_one_messages[waku_light_client_False]-20250815-214627.png) |

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
| Contender | 2025-08-15 | 03:08:18 | `fc47f8e71` |
| Baseline  | 2025-08-14 | 21:30:50 | `fc47f8e71` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.37% (-7.0%)                                                                                                                    | 6.36% (+4.7%)                                                                                                                                                  | 6.06% (-1.0%)                                                                                                                                                    |
| CPU Max               | 132.32% (-8.9%)                                                                                                                  | 153.34% (+24.3%)                                                                                                                                               | 138.71% (-18.0%)                                                                                                                                                 |
| RAM Median            | 51.29 MB (+0.7%)                                                                                                                 | 76.71 MB (+7.0%)                                                                                                                                               | 75.99 MB (-1.8%)                                                                                                                                                 |
| RAM Max               | 55.76 MB (+9.5%)                                                                                                                 | 88.71 MB (+1.5%)                                                                                                                                               | 91.02 MB (+0.8%)                                                                                                                                                 |
| RX Total              | 87.9 KB (+2.5%)                                                                                                                  | 2.06 MB (+0.7%)                                                                                                                                                | 1.98 MB (-2.1%)                                                                                                                                                  |
| TX Total              | 564.0 KB (+0.0%)                                                                                                                 | 3.40 MB (+1.0%)                                                                                                                                                | 3.81 MB (-1.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250815T030818_fc47f8e71/test_idle[waku_light_client_True]-20250815-030110.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250815T030818_fc47f8e71/test_one_to_one_messages[waku_light_client_True]-20250815-030737.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250815T030818_fc47f8e71/test_one_to_one_messages[waku_light_client_False]-20250815-030421.png) |

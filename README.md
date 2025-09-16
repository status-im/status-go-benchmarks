# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-16)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-16 | 03:14:40 | `44f94ade3` |
| Baseline  | 2025-09-15 | 03:08:38 | `897ea8beb` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.18% (-1.8%)                                                                                                                    | 5.51% (-3.3%)                                                                                                                                                  | 7.81% (+0.7%)                                                                                                                                                    |
| CPU Max               | 109.80% (-0.1%)                                                                                                                  | 110.87% (-9.7%)                                                                                                                                                | 109.90% (+1.2%)                                                                                                                                                  |
| RAM Median            | 42.52 MB (-6.3%)                                                                                                                 | 63.04 MB (-2.5%)                                                                                                                                               | 66.15 MB (-2.4%)                                                                                                                                                 |
| RAM Max               | 50.82 MB (+3.6%)                                                                                                                 | 68.77 MB (-10.6%)                                                                                                                                              | 79.80 MB (-2.9%)                                                                                                                                                 |
| RX Total              | 90.9 KB (-1.2%)                                                                                                                  | 2.11 MB (+3.3%)                                                                                                                                                | 3.01 MB (-4.4%)                                                                                                                                                  |
| TX Total              | 585.0 KB (-0.1%)                                                                                                                 | 3.50 MB (+1.0%)                                                                                                                                                | 5.17 MB (+1.6%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250916T031440_44f94ade3/test_idle[waku_light_client_True]-20250916-030708.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250916T031440_44f94ade3/test_one_to_one_messages[waku_light_client_True]-20250916-031355.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250916T031440_44f94ade3/test_one_to_one_messages[waku_light_client_False]-20250916-031027.png) |

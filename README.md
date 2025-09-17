# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-17)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-17 | 03:19:21 | `dbadf551c` |
| Baseline  | 2025-09-16 | 03:14:40 | `44f94ade3` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.21% (+2.5%)                                                                                                                    | 5.21% (-5.4%)                                                                                                                                                  | 7.90% (+1.2%)                                                                                                                                                    |
| CPU Max               | 114.29% (+4.1%)                                                                                                                  | 113.76% (+2.6%)                                                                                                                                                | 128.19% (+16.6%)                                                                                                                                                 |
| RAM Median            | 43.08 MB (+1.3%)                                                                                                                 | 64.35 MB (+2.1%)                                                                                                                                               | 64.68 MB (-2.2%)                                                                                                                                                 |
| RAM Max               | 50.75 MB (-0.1%)                                                                                                                 | 68.83 MB (+0.1%)                                                                                                                                               | 77.30 MB (-3.1%)                                                                                                                                                 |
| RX Total              | 90.8 KB (-0.1%)                                                                                                                  | 2.09 MB (-1.0%)                                                                                                                                                | 3.47 MB (+15.0%)                                                                                                                                                 |
| TX Total              | 580.6 KB (-0.8%)                                                                                                                 | 3.51 MB (+0.1%)                                                                                                                                                | 5.42 MB (+4.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250917T031921_dbadf551c/test_idle[waku_light_client_True]-20250917-031149.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250917T031921_dbadf551c/test_one_to_one_messages[waku_light_client_True]-20250917-031836.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250917T031921_dbadf551c/test_one_to_one_messages[waku_light_client_False]-20250917-031507.png) |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-19)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-19 | 03:14:59 | `6322f2278` |
| Baseline  | 2025-08-18 | 03:08:14 | `dfaefeb7a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.40% (-2.2%)                                                                                                                    | 5.63% (-2.7%)                                                                                                                                                  | 6.12% (+6.9%)                                                                                                                                                    |
| CPU Max               | 161.21% (-3.7%)                                                                                                                  | 143.63% (+4.1%)                                                                                                                                                | 142.32% (-13.8%)                                                                                                                                                 |
| RAM Median            | 54.62 MB (+7.9%)                                                                                                                 | 73.97 MB (+0.1%)                                                                                                                                               | 75.74 MB (+0.6%)                                                                                                                                                 |
| RAM Max               | 54.62 MB (+7.9%)                                                                                                                 | 86.40 MB (-1.8%)                                                                                                                                               | 90.90 MB (-0.6%)                                                                                                                                                 |
| RX Total              | 87.3 KB (-1.0%)                                                                                                                  | 2.02 MB (-0.8%)                                                                                                                                                | 1.96 MB (-3.8%)                                                                                                                                                  |
| TX Total              | 559.8 KB (-1.5%)                                                                                                                 | 3.37 MB (-0.9%)                                                                                                                                                | 3.78 MB (-1.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250819T031459_6322f2278/test_idle[waku_light_client_True]-20250819-030755.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250819T031459_6322f2278/test_one_to_one_messages[waku_light_client_True]-20250819-031417.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250819T031459_6322f2278/test_one_to_one_messages[waku_light_client_False]-20250819-031105.png) |

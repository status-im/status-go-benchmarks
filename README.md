# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-10)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-10 | 03:14:38 | `c827909c8` |
| Baseline  | 2025-09-09 | 03:12:16 | `e8dbb93f5` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.14% (-2.3%)                                                                                                                    | 5.92% (-2.2%)                                                                                                                                                  | 7.44% (-13.8%)                                                                                                                                                   |
| CPU Max               | 111.83% (-17.2%)                                                                                                                 | 155.60% (+12.9%)                                                                                                                                               | 189.39% (+26.0%)                                                                                                                                                 |
| RAM Median            | 42.18 MB (-19.3%)                                                                                                                | 66.96 MB (-11.0%)                                                                                                                                              | 65.61 MB (-12.0%)                                                                                                                                                |
| RAM Max               | 54.62 MB (-1.6%)                                                                                                                 | 80.46 MB (-6.1%)                                                                                                                                               | 80.03 MB (-10.3%)                                                                                                                                                |
| RX Total              | 91.3 KB (+1.6%)                                                                                                                  | 2.05 MB (-1.6%)                                                                                                                                                | 3.03 MB (-2.7%)                                                                                                                                                  |
| TX Total              | 580.2 KB (+2.0%)                                                                                                                 | 3.41 MB (-1.1%)                                                                                                                                                | 5.17 MB (-0.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250910T031438_c827909c8/test_idle[waku_light_client_True]-20250910-030718.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250910T031438_c827909c8/test_one_to_one_messages[waku_light_client_True]-20250910-031356.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250910T031438_c827909c8/test_one_to_one_messages[waku_light_client_False]-20250910-031036.png) |

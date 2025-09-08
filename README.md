# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-08)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-08 | 03:11:17 | `c575471b4` |
| Baseline  | 2025-09-07 | 03:11:27 | `c575471b4` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.16% (-6.9%)                                                                                                                    | 5.57% (-16.6%)                                                                                                                                                 | 8.00% (+5.3%)                                                                                                                                                    |
| CPU Max               | 148.36% (+8.7%)                                                                                                                  | 129.29% (-4.3%)                                                                                                                                                | 153.68% (-0.9%)                                                                                                                                                  |
| RAM Median            | 50.55 MB (-12.4%)                                                                                                                | 76.02 MB (+3.2%)                                                                                                                                               | 75.83 MB (-1.4%)                                                                                                                                                 |
| RAM Max               | 50.55 MB (-12.8%)                                                                                                                | 87.09 MB (+0.8%)                                                                                                                                               | 90.27 MB (+3.0%)                                                                                                                                                 |
| RX Total              | 94.6 KB (+3.6%)                                                                                                                  | 2.07 MB (+0.6%)                                                                                                                                                | 3.16 MB (-2.7%)                                                                                                                                                  |
| TX Total              | 576.4 KB (+1.4%)                                                                                                                 | 3.44 MB (+0.7%)                                                                                                                                                | 5.20 MB (+1.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250908T031117_c575471b4/test_idle[waku_light_client_True]-20250908-030403.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250908T031117_c575471b4/test_one_to_one_messages[waku_light_client_True]-20250908-031033.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250908T031117_c575471b4/test_one_to_one_messages[waku_light_client_False]-20250908-030716.png) |

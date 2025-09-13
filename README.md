# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-13)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-13 | 03:14:24 | `897ea8beb` |
| Baseline  | 2025-09-12 | 03:31:24 | `922bc02dd` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.12% (-14.7%)                                                                                                                   | 6.06% (-12.3%)                                                                                                                                                 | 7.36% (-12.1%)                                                                                                                                                   |
| CPU Max               | 107.92% (-1.5%)                                                                                                                  | 119.06% (+8.5%)                                                                                                                                                | 152.73% (+6.3%)                                                                                                                                                  |
| RAM Median            | 45.23 MB (+1.2%)                                                                                                                 | 65.72 MB (+2.1%)                                                                                                                                               | 67.02 MB (+0.9%)                                                                                                                                                 |
| RAM Max               | 51.06 MB (-4.2%)                                                                                                                 | 76.90 MB (-4.4%)                                                                                                                                               | 80.46 MB (+0.7%)                                                                                                                                                 |
| RX Total              | 92.8 KB (+1.4%)                                                                                                                  | 2.09 MB (+1.2%)                                                                                                                                                | 3.11 MB (+2.9%)                                                                                                                                                  |
| TX Total              | 590.9 KB (+0.9%)                                                                                                                 | 3.46 MB (+0.1%)                                                                                                                                                | 5.16 MB (+0.6%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250913T031424_897ea8beb/test_idle[waku_light_client_True]-20250913-030702.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250913T031424_897ea8beb/test_one_to_one_messages[waku_light_client_True]-20250913-031338.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250913T031424_897ea8beb/test_one_to_one_messages[waku_light_client_False]-20250913-031019.png) |

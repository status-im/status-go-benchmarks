# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-13)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-13 | 10:56:18 | `d1a4de48b` |
| Baseline  | 2025-08-12 | 10:46:20 | `2856ba81c` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.24% (+11.9%)                                                                                                                   | 5.44% (-7.9%)                                                                                                                                                  | 5.15% (-0.8%)                                                                                                                                                    |
| CPU Max               | 144.35% (-10.9%)                                                                                                                 | 128.72% (-17.3%)                                                                                                                                               | 175.75% (+27.5%)                                                                                                                                                 |
| RAM Median            | 55.83 MB (+8.5%)                                                                                                                 | 75.73 MB (-1.4%)                                                                                                                                               | 75.31 MB (-4.4%)                                                                                                                                                 |
| RAM Max               | 56.08 MB (-5.9%)                                                                                                                 | 88.53 MB (+0.1%)                                                                                                                                               | 88.90 MB (-1.4%)                                                                                                                                                 |
| RX Total              | 90.0 KB (+4.8%)                                                                                                                  | 2.05 MB (-0.1%)                                                                                                                                                | 2.05 MB (+3.3%)                                                                                                                                                  |
| TX Total              | 572.7 KB (+1.3%)                                                                                                                 | 3.41 MB (+0.5%)                                                                                                                                                | 3.85 MB (+1.5%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250813T105618_d1a4de48b/test_idle[waku_light_client_True]-20250813-104907.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250813T105618_d1a4de48b/test_one_to_one_messages[waku_light_client_True]-20250813-105536.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250813T105618_d1a4de48b/test_one_to_one_messages[waku_light_client_False]-20250813-105219.png) |

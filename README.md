# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-24)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-24 | 03:08:35 | `7f5c02335` |
| Baseline  | 2025-08-23 | 03:32:13 | `7f5c02335` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.38% (-1.7%)                                                                                                                    | 6.30% (+2.7%)                                                                                                                                                  | 6.35% (+4.5%)                                                                                                                                                    |
| CPU Max               | 150.86% (+3.8%)                                                                                                                  | 151.85% (+24.7%)                                                                                                                                               | 159.47% (+4.1%)                                                                                                                                                  |
| RAM Median            | 53.68 MB (+4.7%)                                                                                                                 | 77.59 MB (-1.2%)                                                                                                                                               | 76.23 MB (-0.8%)                                                                                                                                                 |
| RAM Max               | 53.93 MB (+2.2%)                                                                                                                 | 82.90 MB (-5.3%)                                                                                                                                               | 89.90 MB (+2.8%)                                                                                                                                                 |
| RX Total              | 88.4 KB (+0.5%)                                                                                                                  | 2.07 MB (+1.3%)                                                                                                                                                | 2.01 MB (+0.6%)                                                                                                                                                  |
| TX Total              | 567.8 KB (+0.1%)                                                                                                                 | 3.43 MB (+2.7%)                                                                                                                                                | 3.79 MB (+0.4%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250824T030835_7f5c02335/test_idle[waku_light_client_True]-20250824-030121.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250824T030835_7f5c02335/test_one_to_one_messages[waku_light_client_True]-20250824-030749.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250824T030835_7f5c02335/test_one_to_one_messages[waku_light_client_False]-20250824-030432.png) |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-06)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-06 | 03:12:47 | `c575471b4` |
| Baseline  | 2025-09-05 | 03:12:22 | `a00372b9f` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.20% (-1.1%)                                                                                                                    | 5.99% (+10.9%)                                                                                                                                                 | 8.25% (+33.8%)                                                                                                                                                   |
| CPU Max               | 151.29% (+19.2%)                                                                                                                 | 125.94% (-16.9%)                                                                                                                                               | 109.57% (-29.9%)                                                                                                                                                 |
| RAM Median            | 53.77 MB (-2.4%)                                                                                                                 | 74.15 MB (+0.3%)                                                                                                                                               | 76.95 MB (+2.1%)                                                                                                                                                 |
| RAM Max               | 54.02 MB (-1.9%)                                                                                                                 | 85.40 MB (-3.1%)                                                                                                                                               | 88.90 MB (+1.4%)                                                                                                                                                 |
| RX Total              | 91.7 KB (+7.6%)                                                                                                                  | 2.05 MB (+1.0%)                                                                                                                                                | 3.10 MB (+88.8%)                                                                                                                                                 |
| TX Total              | 568.3 KB (+0.6%)                                                                                                                 | 3.40 MB (+2.1%)                                                                                                                                                | 5.16 MB (+41.6%)                                                                                                                                                 |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250906T031247_c575471b4/test_idle[waku_light_client_True]-20250906-030533.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250906T031247_c575471b4/test_one_to_one_messages[waku_light_client_True]-20250906-031201.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250906T031247_c575471b4/test_one_to_one_messages[waku_light_client_False]-20250906-030846.png) |

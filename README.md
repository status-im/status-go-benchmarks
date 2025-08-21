# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-21)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-21 | 03:18:48 | `ca19cd5de` |
| Baseline  | 2025-08-20 | 03:11:00 | `f78e935b3` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.35% (-2.6%)                                                                                                                    | 5.74% (-6.4%)                                                                                                                                                  | 6.02% (+6.4%)                                                                                                                                                    |
| CPU Max               | 133.25% (+18.4%)                                                                                                                 | 145.31% (+2.6%)                                                                                                                                                | 168.87% (+9.9%)                                                                                                                                                  |
| RAM Median            | 57.68 MB (+4.0%)                                                                                                                 | 74.34 MB (+0.6%)                                                                                                                                               | 75.55 MB (+1.3%)                                                                                                                                                 |
| RAM Max               | 57.68 MB (+4.0%)                                                                                                                 | 89.90 MB (+7.1%)                                                                                                                                               | 87.90 MB (-0.6%)                                                                                                                                                 |
| RX Total              | 86.3 KB (-2.1%)                                                                                                                  | 2.04 MB (+0.3%)                                                                                                                                                | 1.98 MB (-1.6%)                                                                                                                                                  |
| TX Total              | 563.3 KB (-0.3%)                                                                                                                 | 3.33 MB (-0.5%)                                                                                                                                                | 3.76 MB (-0.6%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250821T031848_ca19cd5de/test_idle[waku_light_client_True]-20250821-031143.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250821T031848_ca19cd5de/test_one_to_one_messages[waku_light_client_True]-20250821-031806.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250821T031848_ca19cd5de/test_one_to_one_messages[waku_light_client_False]-20250821-031454.png) |

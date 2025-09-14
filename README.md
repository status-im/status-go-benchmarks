# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-14)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-14 | 03:08:56 | `897ea8beb` |
| Baseline  | 2025-09-13 | 03:14:24 | `897ea8beb` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.07% (-4.3%)                                                                                                                    | 5.34% (-11.8%)                                                                                                                                                 | 7.43% (+1.0%)                                                                                                                                                    |
| CPU Max               | 110.95% (+2.8%)                                                                                                                  | 152.42% (+28.0%)                                                                                                                                               | 109.61% (-28.2%)                                                                                                                                                 |
| RAM Median            | 42.12 MB (-6.9%)                                                                                                                 | 64.40 MB (-2.0%)                                                                                                                                               | 64.46 MB (-3.8%)                                                                                                                                                 |
| RAM Max               | 49.97 MB (-2.1%)                                                                                                                 | 75.65 MB (-1.6%)                                                                                                                                               | 78.40 MB (-2.6%)                                                                                                                                                 |
| RX Total              | 93.2 KB (+0.5%)                                                                                                                  | 2.03 MB (-2.8%)                                                                                                                                                | 3.21 MB (+3.2%)                                                                                                                                                  |
| TX Total              | 586.4 KB (-0.8%)                                                                                                                 | 3.45 MB (-0.2%)                                                                                                                                                | 5.14 MB (-0.5%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250914T030856_897ea8beb/test_idle[waku_light_client_True]-20250914-030134.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250914T030856_897ea8beb/test_one_to_one_messages[waku_light_client_True]-20250914-030811.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250914T030856_897ea8beb/test_one_to_one_messages[waku_light_client_False]-20250914-030452.png) |

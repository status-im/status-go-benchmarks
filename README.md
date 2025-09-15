# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-15)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-15 | 03:08:38 | `897ea8beb` |
| Baseline  | 2025-09-14 | 03:08:56 | `897ea8beb` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.21% (+12.1%)                                                                                                                   | 5.70% (+6.7%)                                                                                                                                                  | 7.75% (+4.3%)                                                                                                                                                    |
| CPU Max               | 109.87% (-1.0%)                                                                                                                  | 122.84% (-19.4%)                                                                                                                                               | 108.63% (-0.9%)                                                                                                                                                  |
| RAM Median            | 45.36 MB (+7.7%)                                                                                                                 | 64.66 MB (+0.4%)                                                                                                                                               | 67.77 MB (+5.1%)                                                                                                                                                 |
| RAM Max               | 49.05 MB (-1.8%)                                                                                                                 | 76.90 MB (+1.7%)                                                                                                                                               | 82.15 MB (+4.8%)                                                                                                                                                 |
| RX Total              | 92.0 KB (-1.3%)                                                                                                                  | 2.04 MB (+0.5%)                                                                                                                                                | 3.15 MB (-1.6%)                                                                                                                                                  |
| TX Total              | 585.5 KB (-0.1%)                                                                                                                 | 3.47 MB (+0.4%)                                                                                                                                                | 5.09 MB (-0.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250915T030838_897ea8beb/test_idle[waku_light_client_True]-20250915-030116.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250915T030838_897ea8beb/test_one_to_one_messages[waku_light_client_True]-20250915-030754.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250915T030838_897ea8beb/test_one_to_one_messages[waku_light_client_False]-20250915-030433.png) |

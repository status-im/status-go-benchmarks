# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-22)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-22 | 03:09:13 | `7c3969b92` |
| Baseline  | 2025-09-21 | 03:08:56 | `7c3969b92` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.33% (+12.8%)                                                                                                                   | 5.85% (+18.9%)                                                                                                                                                 | 7.91% (-2.1%)                                                                                                                                                    |
| CPU Max               | 108.73% (-24.9%)                                                                                                                 | 157.51% (+38.3%)                                                                                                                                               | 108.54% (-2.2%)                                                                                                                                                  |
| RAM Median            | 41.75 MB (-6.2%)                                                                                                                 | 64.08 MB (+2.7%)                                                                                                                                               | 64.79 MB (-0.3%)                                                                                                                                                 |
| RAM Max               | 51.07 MB (+3.3%)                                                                                                                 | 71.40 MB (+7.9%)                                                                                                                                               | 79.35 MB (+1.9%)                                                                                                                                                 |
| RX Total              | 92.2 KB (+1.0%)                                                                                                                  | 2.08 MB (+1.0%)                                                                                                                                                | 3.16 MB (-0.8%)                                                                                                                                                  |
| TX Total              | 585.0 KB (+1.0%)                                                                                                                 | 3.50 MB (+0.0%)                                                                                                                                                | 5.16 MB (-0.6%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250922T030913_7c3969b92/test_idle[waku_light_client_True]-20250922-030139.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250922T030913_7c3969b92/test_one_to_one_messages[waku_light_client_True]-20250922-030826.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250922T030913_7c3969b92/test_one_to_one_messages[waku_light_client_False]-20250922-030459.png) |

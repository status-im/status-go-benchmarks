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
| Contender | 2025-08-13 | 16:27:34 | `00c0d1c3a` |
| Baseline  | 2025-08-13 | 16:07:29 | `d603c29b9` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.19% (-4.5%)                                                                                                                    | 6.01% (+10.9%)                                                                                                                                                 | 5.93% (+18.7%)                                                                                                                                                   |
| CPU Max               | 184.69% (+35.3%)                                                                                                                 | 108.39% (-2.7%)                                                                                                                                                | 112.02% (-23.1%)                                                                                                                                                 |
| RAM Median            | 54.08 MB (+0.3%)                                                                                                                 | 75.04 MB (-7.0%)                                                                                                                                               | 78.55 MB (+0.3%)                                                                                                                                                 |
| RAM Max               | 54.08 MB (+0.3%)                                                                                                                 | 86.46 MB (+1.8%)                                                                                                                                               | 90.65 MB (+2.2%)                                                                                                                                                 |
| RX Total              | 88.7 KB (+0.5%)                                                                                                                  | 2.05 MB (-1.4%)                                                                                                                                                | 2.01 MB (-1.8%)                                                                                                                                                  |
| TX Total              | 573.3 KB (+1.0%)                                                                                                                 | 3.40 MB (+0.1%)                                                                                                                                                | 3.82 MB (-0.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250813T162734_00c0d1c3a/test_idle[waku_light_client_True]-20250813-162024.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250813T162734_00c0d1c3a/test_one_to_one_messages[waku_light_client_True]-20250813-162653.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250813T162734_00c0d1c3a/test_one_to_one_messages[waku_light_client_False]-20250813-162335.png) |

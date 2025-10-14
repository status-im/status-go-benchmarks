# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-14)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-14 | 03:11:36 | `b3af09533` |
| Baseline  | 2025-10-13 | 03:08:44 | `49b18eb4b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.46% (-4.8%)                                                                                                                    | 6.16% (-3.2%)                                                                                                                                                  | 8.16% (-11.8%)                                                                                                                                                   |
| CPU Max               | 160.64% (-12.0%)                                                                                                                 | 130.23% (+6.3%)                                                                                                                                                | 122.50% (-19.6%)                                                                                                                                                 |
| RAM Median            | 42.94 MB (-8.2%)                                                                                                                 | 66.34 MB (-3.1%)                                                                                                                                               | 68.20 MB (-1.1%)                                                                                                                                                 |
| RAM Max               | 54.67 MB (+2.4%)                                                                                                                 | 89.27 MB (+1.7%)                                                                                                                                               | 90.96 MB (-0.5%)                                                                                                                                                 |
| RX Total              | 102.9 KB (+0.3%)                                                                                                                 | 1.97 MB (-3.7%)                                                                                                                                                | 3.66 MB (+25.1%)                                                                                                                                                 |
| TX Total              | 590.4 KB (+0.1%)                                                                                                                 | 3.32 MB (-0.9%)                                                                                                                                                | 5.43 MB (+3.8%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251014T031136_b3af09533/test_idle[waku_light_client_True]-20251014-030430.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251014T031136_b3af09533/test_one_to_one_messages[waku_light_client_True]-20251014-031049.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251014T031136_b3af09533/test_one_to_one_messages[waku_light_client_False]-20251014-030736.png) |

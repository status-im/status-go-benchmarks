# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-15)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-15 | 11:55:37 | `8a4afcc6c` |
| Baseline  | 2025-08-15 | 09:48:23 | `c929730e2` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.28% (-12.6%)                                                                                                                   | 6.41% (-2.6%)                                                                                                                                                  | 5.54% (-5.1%)                                                                                                                                                    |
| CPU Max               | 137.99% (+1.0%)                                                                                                                  | 169.16% (+28.1%)                                                                                                                                               | 147.44% (-1.8%)                                                                                                                                                  |
| RAM Median            | 49.78 MB (-4.0%)                                                                                                                 | 74.65 MB (+0.2%)                                                                                                                                               | 77.36 MB (+3.1%)                                                                                                                                                 |
| RAM Max               | 50.03 MB (-3.9%)                                                                                                                 | 87.46 MB (+3.0%)                                                                                                                                               | 89.13 MB (-0.9%)                                                                                                                                                 |
| RX Total              | 88.4 KB (+0.3%)                                                                                                                  | 2.06 MB (-0.7%)                                                                                                                                                | 1.99 MB (-1.5%)                                                                                                                                                  |
| TX Total              | 567.7 KB (-0.2%)                                                                                                                 | 3.40 MB (-0.1%)                                                                                                                                                | 3.78 MB (+0.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250815T115537_8a4afcc6c/test_idle[waku_light_client_True]-20250815-114830.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250815T115537_8a4afcc6c/test_one_to_one_messages[waku_light_client_True]-20250815-115457.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250815T115537_8a4afcc6c/test_one_to_one_messages[waku_light_client_False]-20250815-115140.png) |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-07)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-07 | 03:10:09 | `c3bd89f1c` |
| Baseline  | 2025-10-06 | 03:10:13 | `d7310c53b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.54% (+9.6%)                                                                                                                    | 5.46% (-2.3%)                                                                                                                                                  | 7.95% (-9.9%)                                                                                                                                                    |
| CPU Max               | 148.21% (-17.0%)                                                                                                                 | 152.14% (+19.7%)                                                                                                                                               | 167.99% (+15.6%)                                                                                                                                                 |
| RAM Median            | 44.38 MB (+0.4%)                                                                                                                 | 67.75 MB (+1.3%)                                                                                                                                               | 67.73 MB (-0.2%)                                                                                                                                                 |
| RAM Max               | 54.42 MB (+6.8%)                                                                                                                 | 87.80 MB (+1.9%)                                                                                                                                               | 89.73 MB (-1.6%)                                                                                                                                                 |
| RX Total              | 102.2 KB (-3.0%)                                                                                                                 | 2.01 MB (+0.2%)                                                                                                                                                | 2.83 MB (-3.6%)                                                                                                                                                  |
| TX Total              | 588.6 KB (-0.2%)                                                                                                                 | 3.37 MB (+0.8%)                                                                                                                                                | 5.17 MB (+2.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251007T031009_c3bd89f1c/test_idle[waku_light_client_True]-20251007-030305.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251007T031009_c3bd89f1c/test_one_to_one_messages[waku_light_client_True]-20251007-030918.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251007T031009_c3bd89f1c/test_one_to_one_messages[waku_light_client_False]-20251007-030611.png) |

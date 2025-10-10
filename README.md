# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-10)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-10 | 03:09:23 | `daef4971a` |
| Baseline  | 2025-10-09 | 03:09:43 | `938029050` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.41% (-4.3%)                                                                                                                    | 6.47% (+13.2%)                                                                                                                                                 | 7.99% (-10.9%)                                                                                                                                                   |
| CPU Max               | 124.82% (-35.2%)                                                                                                                 | 119.45% (-5.3%)                                                                                                                                                | 157.63% (-13.3%)                                                                                                                                                 |
| RAM Median            | 49.37 MB (+0.1%)                                                                                                                 | 65.58 MB (-4.4%)                                                                                                                                               | 69.55 MB (+1.9%)                                                                                                                                                 |
| RAM Max               | 55.08 MB (-0.8%)                                                                                                                 | 88.68 MB (-2.2%)                                                                                                                                               | 91.10 MB (-0.2%)                                                                                                                                                 |
| RX Total              | 102.7 KB (-0.1%)                                                                                                                 | 2.03 MB (-0.7%)                                                                                                                                                | 3.00 MB (+5.2%)                                                                                                                                                  |
| TX Total              | 583.0 KB (+0.1%)                                                                                                                 | 3.34 MB (+0.3%)                                                                                                                                                | 5.12 MB (-2.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251010T030923_daef4971a/test_idle[waku_light_client_True]-20251010-030221.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251010T030923_daef4971a/test_one_to_one_messages[waku_light_client_True]-20251010-030835.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251010T030923_daef4971a/test_one_to_one_messages[waku_light_client_False]-20251010-030525.png) |

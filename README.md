# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-12)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-12 | 03:08:27 | `49b18eb4b` |
| Baseline  | 2025-10-11 | 03:09:46 | `49b18eb4b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.47% (+6.6%)                                                                                                                    | 5.37% (-9.5%)                                                                                                                                                  | 9.02% (+0.4%)                                                                                                                                                    |
| CPU Max               | 151.12% (-9.0%)                                                                                                                  | 127.86% (+8.9%)                                                                                                                                                | 187.40% (+1.4%)                                                                                                                                                  |
| RAM Median            | 43.89 MB (+2.2%)                                                                                                                 | 68.66 MB (+4.7%)                                                                                                                                               | 68.40 MB (+1.2%)                                                                                                                                                 |
| RAM Max               | 54.54 MB (+9.5%)                                                                                                                 | 87.98 MB (-1.2%)                                                                                                                                               | 92.55 MB (+4.0%)                                                                                                                                                 |
| RX Total              | 103.2 KB (+1.3%)                                                                                                                 | 2.01 MB (-0.1%)                                                                                                                                                | 2.81 MB (-31.8%)                                                                                                                                                 |
| TX Total              | 588.7 KB (+0.6%)                                                                                                                 | 3.32 MB (-1.2%)                                                                                                                                                | 5.17 MB (-8.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251012T030827_49b18eb4b/test_idle[waku_light_client_True]-20251012-030130.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251012T030827_49b18eb4b/test_one_to_one_messages[waku_light_client_True]-20251012-030743.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251012T030827_49b18eb4b/test_one_to_one_messages[waku_light_client_False]-20251012-030435.png) |

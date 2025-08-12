# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-12)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-12 | 10:46:20 | `2856ba81c` |
| Baseline  | 2025-08-11 | 18:39:52 | `ad6772f`   |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.11% (-16.9%)                                                                                                                   | 5.91% (-9.2%)                                                                                                                                                  | 5.20% (-20.1%)                                                                                                                                                   |
| CPU Max               | 162.07% (+4.9%)                                                                                                                  | 155.69% (-2.4%)                                                                                                                                                | 137.80% (-4.8%)                                                                                                                                                  |
| RAM Median            | 51.45 MB (-3.0%)                                                                                                                 | 76.84 MB (+1.7%)                                                                                                                                               | 78.78 MB (+5.1%)                                                                                                                                                 |
| RAM Max               | 59.58 MB (+6.3%)                                                                                                                 | 88.46 MB (+5.4%)                                                                                                                                               | 90.15 MB (+6.8%)                                                                                                                                                 |
| RX Total              | 85.9 KB (-0.8%)                                                                                                                  | 2.05 MB (-0.9%)                                                                                                                                                | 1.99 MB (-4.2%)                                                                                                                                                  |
| TX Total              | 565.2 KB (-1.1%)                                                                                                                 | 3.40 MB (-1.6%)                                                                                                                                                | 3.80 MB (-3.5%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250812T104620_2856ba81c/test_idle[waku_light_client_True]-20250812-103911.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250812T104620_2856ba81c/test_one_to_one_messages[waku_light_client_True]-20250812-104541.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250812T104620_2856ba81c/test_one_to_one_messages[waku_light_client_False]-20250812-104225.png) |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-31)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-31 | 03:10:46 | `d03b7b5ed` |
| Baseline  | 2025-08-30 | 03:12:42 | `d03b7b5ed` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.39% (+2.5%)                                                                                                                    | 5.56% (-3.2%)                                                                                                                                                  | 5.46% (-6.6%)                                                                                                                                                    |
| CPU Max               | 131.84% (-3.6%)                                                                                                                  | 134.27% (-10.7%)                                                                                                                                               | 151.40% (+17.4%)                                                                                                                                                 |
| RAM Median            | 47.83 MB (-6.8%)                                                                                                                 | 74.92 MB (+0.5%)                                                                                                                                               | 75.68 MB (-2.4%)                                                                                                                                                 |
| RAM Max               | 49.83 MB (-2.9%)                                                                                                                 | 90.71 MB (+3.2%)                                                                                                                                               | 90.21 MB (+5.0%)                                                                                                                                                 |
| RX Total              | 87.9 KB (+2.9%)                                                                                                                  | 2.05 MB (+0.0%)                                                                                                                                                | 1.97 MB (-3.1%)                                                                                                                                                  |
| TX Total              | 567.6 KB (+1.6%)                                                                                                                 | 3.36 MB (+0.4%)                                                                                                                                                | 3.81 MB (+0.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250831T031046_d03b7b5ed/test_idle[waku_light_client_True]-20250831-030344.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250831T031046_d03b7b5ed/test_one_to_one_messages[waku_light_client_True]-20250831-031003.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250831T031046_d03b7b5ed/test_one_to_one_messages[waku_light_client_False]-20250831-030652.png) |

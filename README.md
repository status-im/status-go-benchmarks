# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-07)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-07 | 03:11:27 | `c575471b4` |
| Baseline  | 2025-09-06 | 03:12:47 | `c575471b4` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.24% (+3.6%)                                                                                                                    | 6.67% (+11.4%)                                                                                                                                                 | 7.60% (-7.9%)                                                                                                                                                    |
| CPU Max               | 136.52% (-9.8%)                                                                                                                  | 135.06% (+7.2%)                                                                                                                                                | 155.01% (+41.5%)                                                                                                                                                 |
| RAM Median            | 57.72 MB (+7.4%)                                                                                                                 | 73.64 MB (-0.7%)                                                                                                                                               | 76.91 MB (-0.1%)                                                                                                                                                 |
| RAM Max               | 57.97 MB (+7.3%)                                                                                                                 | 86.40 MB (+1.2%)                                                                                                                                               | 87.65 MB (-1.4%)                                                                                                                                                 |
| RX Total              | 91.3 KB (-0.5%)                                                                                                                  | 2.06 MB (+0.4%)                                                                                                                                                | 3.24 MB (+4.7%)                                                                                                                                                  |
| TX Total              | 568.5 KB (+0.0%)                                                                                                                 | 3.42 MB (+0.4%)                                                                                                                                                | 5.11 MB (-0.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250907T031127_c575471b4/test_idle[waku_light_client_True]-20250907-030416.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250907T031127_c575471b4/test_one_to_one_messages[waku_light_client_True]-20250907-031046.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250907T031127_c575471b4/test_one_to_one_messages[waku_light_client_False]-20250907-030729.png) |

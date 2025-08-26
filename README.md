# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-26)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-26 | 03:15:37 | `77be24219` |
| Baseline  | 2025-08-25 | 03:08:48 | `7f5c02335` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.33% (-2.3%)                                                                                                                    | 5.70% (-7.1%)                                                                                                                                                  | 5.83% (-6.5%)                                                                                                                                                    |
| CPU Max               | 150.64% (+34.6%)                                                                                                                 | 152.36% (-2.4%)                                                                                                                                                | 161.74% (+11.8%)                                                                                                                                                 |
| RAM Median            | 52.15 MB (+3.6%)                                                                                                                 | 76.77 MB (+4.4%)                                                                                                                                               | 73.91 MB (-1.3%)                                                                                                                                                 |
| RAM Max               | 55.97 MB (+0.6%)                                                                                                                 | 87.65 MB (+1.4%)                                                                                                                                               | 92.02 MB (+3.7%)                                                                                                                                                 |
| RX Total              | 85.4 KB (-1.1%)                                                                                                                  | 2.04 MB (-1.2%)                                                                                                                                                | 1.70 MB (-14.7%)                                                                                                                                                 |
| TX Total              | 557.8 KB (-2.3%)                                                                                                                 | 3.36 MB (-2.2%)                                                                                                                                                | 3.69 MB (-2.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250826T031537_77be24219/test_idle[waku_light_client_True]-20250826-030826.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250826T031537_77be24219/test_one_to_one_messages[waku_light_client_True]-20250826-031452.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250826T031537_77be24219/test_one_to_one_messages[waku_light_client_False]-20250826-031139.png) |

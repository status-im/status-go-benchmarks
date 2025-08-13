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
| Contender | 2025-08-13 | 15:26:42 | `fc453d5eb` |
| Baseline  | 2025-08-13 | 13:23:10 | `cc234c1ad` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.23% (-16.0%)                                                                                                                   | 6.34% (+10.6%)                                                                                                                                                 | 5.56% (+2.2%)                                                                                                                                                    |
| CPU Max               | 139.90% (+0.3%)                                                                                                                  | 174.93% (+34.9%)                                                                                                                                               | 120.33% (-12.1%)                                                                                                                                                 |
| RAM Median            | 55.83 MB (+3.2%)                                                                                                                 | 78.15 MB (+0.1%)                                                                                                                                               | 78.13 MB (+1.4%)                                                                                                                                                 |
| RAM Max               | 56.08 MB (-10.0%)                                                                                                                | 88.77 MB (+0.3%)                                                                                                                                               | 91.36 MB (-1.0%)                                                                                                                                                 |
| RX Total              | 85.7 KB (-2.9%)                                                                                                                  | 2.05 MB (+0.9%)                                                                                                                                                | 2.02 MB (+0.1%)                                                                                                                                                  |
| TX Total              | 565.1 KB (-0.5%)                                                                                                                 | 3.39 MB (+1.0%)                                                                                                                                                | 3.84 MB (+1.5%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250813T152642_fc453d5eb/test_idle[waku_light_client_True]-20250813-151933.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250813T152642_fc453d5eb/test_one_to_one_messages[waku_light_client_True]-20250813-152601.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250813T152642_fc453d5eb/test_one_to_one_messages[waku_light_client_False]-20250813-152245.png) |

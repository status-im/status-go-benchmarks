# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-21)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-21 | 03:08:56 | `7c3969b92` |
| Baseline  | 2025-09-20 | 03:29:55 | `7c3969b92` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.18% (-16.4%)                                                                                                                   | 4.92% (-10.5%)                                                                                                                                                 | 8.08% (-2.5%)                                                                                                                                                    |
| CPU Max               | 144.74% (-9.6%)                                                                                                                  | 113.89% (-2.7%)                                                                                                                                                | 111.01% (-2.2%)                                                                                                                                                  |
| RAM Median            | 44.52 MB (+1.5%)                                                                                                                 | 62.41 MB (-3.9%)                                                                                                                                               | 65.02 MB (+2.6%)                                                                                                                                                 |
| RAM Max               | 49.43 MB (+0.5%)                                                                                                                 | 66.18 MB (-9.5%)                                                                                                                                               | 77.90 MB (-6.0%)                                                                                                                                                 |
| RX Total              | 91.3 KB (-0.1%)                                                                                                                  | 2.06 MB (-0.8%)                                                                                                                                                | 3.19 MB (-6.6%)                                                                                                                                                  |
| TX Total              | 579.2 KB (-0.2%)                                                                                                                 | 3.50 MB (+0.9%)                                                                                                                                                | 5.19 MB (-0.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250921T030856_7c3969b92/test_idle[waku_light_client_True]-20250921-030121.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250921T030856_7c3969b92/test_one_to_one_messages[waku_light_client_True]-20250921-030809.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250921T030856_7c3969b92/test_one_to_one_messages[waku_light_client_False]-20250921-030440.png) |

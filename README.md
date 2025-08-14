# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-14)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-14 | 21:30:50 | `fc47f8e71` |
| Baseline  | 2025-08-13 | 19:13:55 | `493fd1b03` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.47% (+22.9%)                                                                                                                   | 6.07% (+1.7%)                                                                                                                                                  | 6.12% (+4.2%)                                                                                                                                                    |
| CPU Max               | 145.18% (+5.4%)                                                                                                                  | 123.36% (-18.3%)                                                                                                                                               | 169.11% (+17.3%)                                                                                                                                                 |
| RAM Median            | 50.91 MB (+2.4%)                                                                                                                 | 71.72 MB (-3.0%)                                                                                                                                               | 77.41 MB (+1.7%)                                                                                                                                                 |
| RAM Max               | 50.91 MB (-1.3%)                                                                                                                 | 87.40 MB (+0.4%)                                                                                                                                               | 90.34 MB (+4.2%)                                                                                                                                                 |
| RX Total              | 85.8 KB (-1.7%)                                                                                                                  | 2.05 MB (+0.2%)                                                                                                                                                | 2.02 MB (-0.4%)                                                                                                                                                  |
| TX Total              | 564.0 KB (-0.5%)                                                                                                                 | 3.36 MB (-0.5%)                                                                                                                                                | 3.85 MB (+0.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250814T213050_fc47f8e71/test_idle[waku_light_client_True]-20250814-212343.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250814T213050_fc47f8e71/test_one_to_one_messages[waku_light_client_True]-20250814-213007.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250814T213050_fc47f8e71/test_one_to_one_messages[waku_light_client_False]-20250814-212653.png) |

# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-23)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-23 | 03:32:13 | `7f5c02335` |
| Baseline  | 2025-08-22 | 03:17:43 | `278582a5e` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.40% (-1.4%)                                                                                                                    | 6.14% (-1.7%)                                                                                                                                                  | 6.08% (+2.8%)                                                                                                                                                    |
| CPU Max               | 145.35% (-8.5%)                                                                                                                  | 121.78% (-17.6%)                                                                                                                                               | 153.26% (-8.0%)                                                                                                                                                  |
| RAM Median            | 51.29 MB (+7.2%)                                                                                                                 | 78.51 MB (+7.0%)                                                                                                                                               | 76.88 MB (+2.3%)                                                                                                                                                 |
| RAM Max               | 52.78 MB (+6.5%)                                                                                                                 | 87.52 MB (-2.6%)                                                                                                                                               | 87.47 MB (-3.6%)                                                                                                                                                 |
| RX Total              | 88.0 KB (+2.8%)                                                                                                                  | 2.04 MB (-0.2%)                                                                                                                                                | 2.00 MB (-0.2%)                                                                                                                                                  |
| TX Total              | 567.5 KB (+0.2%)                                                                                                                 | 3.34 MB (-1.4%)                                                                                                                                                | 3.78 MB (-1.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250823T033213_7f5c02335/test_idle[waku_light_client_True]-20250823-032505.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250823T033213_7f5c02335/test_one_to_one_messages[waku_light_client_True]-20250823-033129.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250823T033213_7f5c02335/test_one_to_one_messages[waku_light_client_False]-20250823-032815.png) |

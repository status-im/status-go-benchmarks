# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-25)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-25 | 03:08:48 | `7f5c02335` |
| Baseline  | 2025-08-24 | 03:08:35 | `7f5c02335` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.36% (-1.7%)                                                                                                                    | 6.14% (-2.6%)                                                                                                                                                  | 6.24% (-1.8%)                                                                                                                                                    |
| CPU Max               | 111.92% (-25.8%)                                                                                                                 | 156.05% (+2.8%)                                                                                                                                                | 144.69% (-9.3%)                                                                                                                                                  |
| RAM Median            | 50.33 MB (-6.2%)                                                                                                                 | 73.56 MB (-5.2%)                                                                                                                                               | 74.86 MB (-1.8%)                                                                                                                                                 |
| RAM Max               | 55.62 MB (+3.1%)                                                                                                                 | 86.40 MB (+4.2%)                                                                                                                                               | 88.71 MB (-1.3%)                                                                                                                                                 |
| RX Total              | 86.4 KB (-2.3%)                                                                                                                  | 2.07 MB (-0.2%)                                                                                                                                                | 1.99 MB (-0.9%)                                                                                                                                                  |
| TX Total              | 571.2 KB (+0.6%)                                                                                                                 | 3.44 MB (+0.1%)                                                                                                                                                | 3.80 MB (+0.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250825T030848_7f5c02335/test_idle[waku_light_client_True]-20250825-030131.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250825T030848_7f5c02335/test_one_to_one_messages[waku_light_client_True]-20250825-030802.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250825T030848_7f5c02335/test_one_to_one_messages[waku_light_client_False]-20250825-030446.png) |

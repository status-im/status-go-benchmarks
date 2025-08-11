# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-11)

| Run       | Date       | Time     | Commit    |
|-----------|------------|----------|-----------|
| Contender | 2025-08-11 | 18:39:52 | `ad6772f` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                          | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                         | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.33%                                                                                                                          | 6.51%                                                                                                                                                        | 6.51%                                                                                                                                                          |
| CPU Max               | 154.50%                                                                                                                        | 159.51%                                                                                                                                                      | 144.68%                                                                                                                                                        |
| RAM Median            | 53.07 MB                                                                                                                       | 75.52 MB                                                                                                                                                     | 74.94 MB                                                                                                                                                       |
| RAM Max               | 56.03 MB                                                                                                                       | 83.96 MB                                                                                                                                                     | 84.40 MB                                                                                                                                                       |
| RX Total              | 86.6 KB                                                                                                                        | 2.07 MB                                                                                                                                                      | 2.07 MB                                                                                                                                                        |
| TX Total              | 571.6 KB                                                                                                                       | 3.45 MB                                                                                                                                                      | 3.93 MB                                                                                                                                                        |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250811T183952_ad6772f/test_idle[waku_light_client_True]-20250811-183233.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250811T183952_ad6772f/test_one_to_one_messages[waku_light_client_True]-20250811-183916.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250811T183952_ad6772f/test_one_to_one_messages[waku_light_client_False]-20250811-183553.png) |

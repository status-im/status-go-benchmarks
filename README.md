# status-go-benchmarks

Benchmark metrics with 60-day history and latest comparison.

## 60-Day History

| Metric History                                                     | Metric History                                               |
|--------------------------------------------------------------------|--------------------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png)             | ![cpu_max_history.png](docs/cpu_max_history.png)             |
| ![ram_median_history.png](docs/ram_median_history.png)             | ![ram_max_history.png](docs/ram_max_history.png)             |
| ![rx_total_history.png](docs/rx_total_history.png)                 | ![tx_total_history.png](docs/tx_total_history.png)           |
| ![goroutines_count_history.png](docs/goroutines_count_history.png) | ![threads_count_history.png](docs/threads_count_history.png) |

## Latest Report (2026-06-12)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2026-06-12 | 03:18:24 | `e7de956ab` |
| Baseline  | 2026-06-11 | 03:18:02 | `5f1d67c4a` |

| Metric                | test_idle<br>[waku_light_client_False]   | test_idle<br>[waku_light_client_True]   | test_one_to_one_messages<br>[waku_light_client_True]   | test_one_to_one_messages<br>[waku_light_client_False]   |
|-----------------------|------------------------------------------|-----------------------------------------|--------------------------------------------------------|---------------------------------------------------------|
| CPU Median            | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| CPU Max               | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| RAM Median            | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| RAM Max               | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| RX Total              | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| TX Total              | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| Goroutines count      | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| Threads count         | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |
| **Performance Chart** | N/A                                      | N/A                                     | N/A                                                    | N/A                                                     |

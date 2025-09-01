# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-01)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-01 | 03:10:59 | `d03b7b5ed` |
| Baseline  | 2025-08-31 | 03:10:46 | `d03b7b5ed` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.37% (-1.2%)                                                                                                                    | 5.45% (-2.0%)                                                                                                                                                  | 5.73% (+4.9%)                                                                                                                                                    |
| CPU Max               | 129.60% (-1.7%)                                                                                                                  | 154.05% (+14.7%)                                                                                                                                               | 137.73% (-9.0%)                                                                                                                                                  |
| RAM Median            | 56.15 MB (+17.4%)                                                                                                                | 74.65 MB (-0.4%)                                                                                                                                               | 75.59 MB (-0.1%)                                                                                                                                                 |
| RAM Max               | 56.15 MB (+12.7%)                                                                                                                | 87.40 MB (-3.7%)                                                                                                                                               | 91.96 MB (+1.9%)                                                                                                                                                 |
| RX Total              | 87.1 KB (-0.9%)                                                                                                                  | 2.03 MB (-1.1%)                                                                                                                                                | 1.98 MB (+0.3%)                                                                                                                                                  |
| TX Total              | 558.3 KB (-1.6%)                                                                                                                 | 3.35 MB (-0.4%)                                                                                                                                                | 3.75 MB (-1.8%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250901T031059_d03b7b5ed/test_idle[waku_light_client_True]-20250901-030351.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250901T031059_d03b7b5ed/test_one_to_one_messages[waku_light_client_True]-20250901-031011.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250901T031059_d03b7b5ed/test_one_to_one_messages[waku_light_client_False]-20250901-030659.png) |

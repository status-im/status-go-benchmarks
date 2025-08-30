# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-30)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-30 | 03:12:42 | `d03b7b5ed` |
| Baseline  | 2025-08-29 | 03:12:23 | `78449f196` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.35% (-3.1%)                                                                                                                    | 5.74% (+1.5%)                                                                                                                                                  | 5.84% (+1.5%)                                                                                                                                                    |
| CPU Max               | 136.82% (+4.1%)                                                                                                                  | 150.27% (+32.1%)                                                                                                                                               | 128.98% (-22.3%)                                                                                                                                                 |
| RAM Median            | 51.31 MB (+2.5%)                                                                                                                 | 74.58 MB (+0.3%)                                                                                                                                               | 77.55 MB (+0.1%)                                                                                                                                                 |
| RAM Max               | 51.31 MB (+2.5%)                                                                                                                 | 87.90 MB (+2.1%)                                                                                                                                               | 85.90 MB (-5.6%)                                                                                                                                                 |
| RX Total              | 85.5 KB (-1.2%)                                                                                                                  | 2.05 MB (+1.5%)                                                                                                                                                | 2.04 MB (+2.6%)                                                                                                                                                  |
| TX Total              | 558.4 KB (-1.5%)                                                                                                                 | 3.35 MB (-0.2%)                                                                                                                                                | 3.81 MB (+0.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250830T031242_d03b7b5ed/test_idle[waku_light_client_True]-20250830-030531.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250830T031242_d03b7b5ed/test_one_to_one_messages[waku_light_client_True]-20250830-031155.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250830T031242_d03b7b5ed/test_one_to_one_messages[waku_light_client_False]-20250830-030844.png) |

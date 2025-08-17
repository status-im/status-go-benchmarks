# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-17)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-17 | 03:08:19 | `dfaefeb7a` |
| Baseline  | 2025-08-16 | 03:08:10 | `dfaefeb7a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.39% (-0.1%)                                                                                                                    | 6.40% (+0.3%)                                                                                                                                                  | 5.78% (-4.3%)                                                                                                                                                    |
| CPU Max               | 144.81% (+3.3%)                                                                                                                  | 140.00% (-9.1%)                                                                                                                                                | 168.10% (+12.6%)                                                                                                                                                 |
| RAM Median            | 49.58 MB (-4.7%)                                                                                                                 | 75.02 MB (-0.0%)                                                                                                                                               | 75.12 MB (-2.5%)                                                                                                                                                 |
| RAM Max               | 49.58 MB (-10.0%)                                                                                                                | 89.52 MB (+0.7%)                                                                                                                                               | 91.02 MB (+2.4%)                                                                                                                                                 |
| RX Total              | 88.2 KB (+0.5%)                                                                                                                  | 2.07 MB (+1.8%)                                                                                                                                                | 2.01 MB (+1.0%)                                                                                                                                                  |
| TX Total              | 567.8 KB (+1.3%)                                                                                                                 | 3.40 MB (+1.5%)                                                                                                                                                | 3.75 MB (-1.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250817T030819_dfaefeb7a/test_idle[waku_light_client_True]-20250817-030111.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250817T030819_dfaefeb7a/test_one_to_one_messages[waku_light_client_True]-20250817-030736.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250817T030819_dfaefeb7a/test_one_to_one_messages[waku_light_client_False]-20250817-030420.png) |

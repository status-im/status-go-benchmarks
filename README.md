# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-16)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-16 | 03:08:10 | `dfaefeb7a` |
| Baseline  | 2025-08-15 | 21:50:18 | `dfaefeb7a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.39% (-6.8%)                                                                                                                    | 6.38% (+5.9%)                                                                                                                                                  | 6.04% (-5.8%)                                                                                                                                                    |
| CPU Max               | 140.17% (-10.5%)                                                                                                                 | 154.00% (+0.2%)                                                                                                                                                | 149.27% (+33.4%)                                                                                                                                                 |
| RAM Median            | 52.04 MB (+1.0%)                                                                                                                 | 75.04 MB (-4.3%)                                                                                                                                               | 77.02 MB (-0.7%)                                                                                                                                                 |
| RAM Max               | 55.11 MB (+6.9%)                                                                                                                 | 88.90 MB (-1.5%)                                                                                                                                               | 88.90 MB (-1.7%)                                                                                                                                                 |
| RX Total              | 87.8 KB (-0.6%)                                                                                                                  | 2.04 MB (+0.1%)                                                                                                                                                | 1.99 MB (-0.2%)                                                                                                                                                  |
| TX Total              | 560.2 KB (-1.2%)                                                                                                                 | 3.35 MB (+0.9%)                                                                                                                                                | 3.82 MB (-0.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250816T030810_dfaefeb7a/test_idle[waku_light_client_True]-20250816-030106.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250816T030810_dfaefeb7a/test_one_to_one_messages[waku_light_client_True]-20250816-030728.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250816T030810_dfaefeb7a/test_one_to_one_messages[waku_light_client_False]-20250816-030415.png) |

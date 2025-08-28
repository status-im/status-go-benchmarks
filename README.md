# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-28)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-28 | 03:14:19 | `bfa6eba7b` |
| Baseline  | 2025-08-27 | 03:11:34 | `f164658bb` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.42% (+4.2%)                                                                                                                    | 6.43% (+8.3%)                                                                                                                                                  | 6.43% (+6.2%)                                                                                                                                                    |
| CPU Max               | 169.53% (+16.5%)                                                                                                                 | 157.42% (-3.4%)                                                                                                                                                | 125.07% (-20.2%)                                                                                                                                                 |
| RAM Median            | 52.09 MB (+1.5%)                                                                                                                 | 74.95 MB (+0.5%)                                                                                                                                               | 75.16 MB (-0.6%)                                                                                                                                                 |
| RAM Max               | 52.09 MB (+1.5%)                                                                                                                 | 88.90 MB (-1.2%)                                                                                                                                               | 91.46 MB (-1.1%)                                                                                                                                                 |
| RX Total              | 85.9 KB (+0.3%)                                                                                                                  | 2.03 MB (-0.9%)                                                                                                                                                | 1.99 MB (+1.0%)                                                                                                                                                  |
| TX Total              | 566.2 KB (+1.1%)                                                                                                                 | 3.34 MB (-1.1%)                                                                                                                                                | 3.83 MB (+0.8%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250828T031419_bfa6eba7b/test_idle[waku_light_client_True]-20250828-030718.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250828T031419_bfa6eba7b/test_one_to_one_messages[waku_light_client_True]-20250828-031335.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250828T031419_bfa6eba7b/test_one_to_one_messages[waku_light_client_False]-20250828-031025.png) |

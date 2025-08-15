# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-15)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-15 | 09:48:23 | `c929730e2` |
| Baseline  | 2025-08-15 | 03:08:18 | `fc47f8e71` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.46% (+6.4%)                                                                                                                    | 6.59% (+3.6%)                                                                                                                                                  | 5.84% (-3.7%)                                                                                                                                                    |
| CPU Max               | 136.61% (+3.2%)                                                                                                                  | 132.07% (-13.9%)                                                                                                                                               | 150.13% (+8.2%)                                                                                                                                                  |
| RAM Median            | 51.83 MB (+1.1%)                                                                                                                 | 74.48 MB (-2.9%)                                                                                                                                               | 75.02 MB (-1.3%)                                                                                                                                                 |
| RAM Max               | 52.08 MB (-6.6%)                                                                                                                 | 84.90 MB (-4.3%)                                                                                                                                               | 89.90 MB (-1.2%)                                                                                                                                                 |
| RX Total              | 88.2 KB (+0.3%)                                                                                                                  | 2.08 MB (+0.5%)                                                                                                                                                | 2.02 MB (+2.2%)                                                                                                                                                  |
| TX Total              | 568.6 KB (+0.8%)                                                                                                                 | 3.40 MB (+0.2%)                                                                                                                                                | 3.77 MB (-1.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250815T094823_c929730e2/test_idle[waku_light_client_True]-20250815-094115.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250815T094823_c929730e2/test_one_to_one_messages[waku_light_client_True]-20250815-094743.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250815T094823_c929730e2/test_one_to_one_messages[waku_light_client_False]-20250815-094427.png) |

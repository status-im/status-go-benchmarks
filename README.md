# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-22)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-22 | 03:17:43 | `278582a5e` |
| Baseline  | 2025-08-21 | 03:18:48 | `ca19cd5de` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.42% (+5.6%)                                                                                                                    | 6.25% (+8.9%)                                                                                                                                                  | 5.91% (-1.7%)                                                                                                                                                    |
| CPU Max               | 158.91% (+19.3%)                                                                                                                 | 147.77% (+1.7%)                                                                                                                                                | 166.57% (-1.4%)                                                                                                                                                  |
| RAM Median            | 47.83 MB (-17.1%)                                                                                                                | 73.34 MB (-1.3%)                                                                                                                                               | 75.18 MB (-0.5%)                                                                                                                                                 |
| RAM Max               | 49.58 MB (-14.0%)                                                                                                                | 89.90 MB (0%)                                                                                                                                                  | 90.73 MB (+3.2%)                                                                                                                                                 |
| RX Total              | 85.6 KB (-0.8%)                                                                                                                  | 2.05 MB (+0.3%)                                                                                                                                                | 2.00 MB (+1.0%)                                                                                                                                                  |
| TX Total              | 566.1 KB (+0.5%)                                                                                                                 | 3.39 MB (+1.7%)                                                                                                                                                | 3.82 MB (+1.5%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250822T031743_278582a5e/test_idle[waku_light_client_True]-20250822-031034.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250822T031743_278582a5e/test_one_to_one_messages[waku_light_client_True]-20250822-031657.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250822T031743_278582a5e/test_one_to_one_messages[waku_light_client_False]-20250822-031344.png) |

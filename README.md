# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-30)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-30 | 03:29:47 | `a38485468` |
| Baseline  | 2025-09-23 | 03:11:34 | `620d96c7a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.48% (+11.5%)                                                                                                                   | 5.78% (+15.3%)                                                                                                                                                 | 8.08% (-1.4%)                                                                                                                                                    |
| CPU Max               | 113.16% (-18.7%)                                                                                                                 | 119.33% (-15.5%)                                                                                                                                               | 125.84% (+17.1%)                                                                                                                                                 |
| RAM Median            | 44.23 MB (-3.7%)                                                                                                                 | 61.17 MB (-1.5%)                                                                                                                                               | 65.98 MB (+0.5%)                                                                                                                                                 |
| RAM Max               | 56.77 MB (+17.9%)                                                                                                                | 72.73 MB (+5.3%)                                                                                                                                               | 80.65 MB (-0.1%)                                                                                                                                                 |
| RX Total              | 103.7 KB (+0.9%)                                                                                                                 | 2.11 MB (+1.0%)                                                                                                                                                | 3.23 MB (-0.8%)                                                                                                                                                  |
| TX Total              | 593.7 KB (+1.1%)                                                                                                                 | 3.51 MB (-0.0%)                                                                                                                                                | 5.27 MB (+0.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250930T032947_a38485468/test_idle[waku_light_client_True]-20250930-032223.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250930T032947_a38485468/test_one_to_one_messages[waku_light_client_True]-20250930-032900.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250930T032947_a38485468/test_one_to_one_messages[waku_light_client_False]-20250930-032538.png) |

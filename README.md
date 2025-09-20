# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-20)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-20 | 03:29:55 | `7c3969b92` |
| Baseline  | 2025-09-19 | 03:13:17 | `4edf1bed1` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.41% (+28.2%)                                                                                                                   | 5.50% (+12.5%)                                                                                                                                                 | 8.29% (+10.2%)                                                                                                                                                   |
| CPU Max               | 160.05% (+14.9%)                                                                                                                 | 117.02% (+9.5%)                                                                                                                                                | 113.52% (+5.1%)                                                                                                                                                  |
| RAM Median            | 43.86 MB (-2.7%)                                                                                                                 | 64.98 MB (+0.5%)                                                                                                                                               | 63.35 MB (-3.3%)                                                                                                                                                 |
| RAM Max               | 49.20 MB (-7.6%)                                                                                                                 | 73.10 MB (+7.8%)                                                                                                                                               | 82.90 MB (+5.4%)                                                                                                                                                 |
| RX Total              | 91.4 KB (+0.1%)                                                                                                                  | 2.07 MB (-0.5%)                                                                                                                                                | 3.41 MB (+8.3%)                                                                                                                                                  |
| TX Total              | 580.6 KB (-0.7%)                                                                                                                 | 3.47 MB (-0.9%)                                                                                                                                                | 5.21 MB (-1.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250920T032955_7c3969b92/test_idle[waku_light_client_True]-20250920-032229.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250920T032955_7c3969b92/test_one_to_one_messages[waku_light_client_True]-20250920-032909.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250920T032955_7c3969b92/test_one_to_one_messages[waku_light_client_False]-20250920-032546.png) |

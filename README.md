# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-02)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-02 | 16:13:45 | `106d03f09` |
| Baseline  | 2025-10-01 | 03:13:33 | `cad3569b7` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.54% (+13.2%)                                                                                                                   | 6.14% (+24.4%)                                                                                                                                                 | 8.90% (+6.1%)                                                                                                                                                    |
| CPU Max               | 119.15% (+7.3%)                                                                                                                  | 125.60% (+12.9%)                                                                                                                                               | 155.68% (+36.8%)                                                                                                                                                 |
| RAM Median            | 41.40 MB (-6.2%)                                                                                                                 | 66.83 MB (+2.5%)                                                                                                                                               | 68.06 MB (+3.4%)                                                                                                                                                 |
| RAM Max               | 55.91 MB (+18.5%)                                                                                                                | 87.78 MB (+26.2%)                                                                                                                                              | 90.90 MB (+13.7%)                                                                                                                                                |
| RX Total              | 103.6 KB (+0.6%)                                                                                                                 | 2.05 MB (-3.1%)                                                                                                                                                | 3.00 MB (-2.1%)                                                                                                                                                  |
| TX Total              | 590.0 KB (+0.4%)                                                                                                                 | 3.35 MB (-4.1%)                                                                                                                                                | 5.18 MB (+0.4%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251002T161345_106d03f09/test_idle[waku_light_client_True]-20251002-154635.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251002T161345_106d03f09/test_one_to_one_messages[waku_light_client_True]-20251002-155252.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251002T161345_106d03f09/test_one_to_one_messages[waku_light_client_False]-20251002-154942.png) |

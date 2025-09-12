# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-12)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-12 | 03:31:24 | `922bc02dd` |
| Baseline  | 2025-09-11 | 03:14:24 | `edf7ca6ac` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.32% (+14.5%)                                                                                                                   | 6.90% (+20.5%)                                                                                                                                                 | 8.37% (+12.2%)                                                                                                                                                   |
| CPU Max               | 109.52% (-3.0%)                                                                                                                  | 109.77% (-24.8%)                                                                                                                                               | 143.68% (+30.5%)                                                                                                                                                 |
| RAM Median            | 44.70 MB (-1.7%)                                                                                                                 | 64.40 MB (-1.8%)                                                                                                                                               | 66.42 MB (+0.5%)                                                                                                                                                 |
| RAM Max               | 53.27 MB (-1.4%)                                                                                                                 | 80.46 MB (+1.7%)                                                                                                                                               | 79.90 MB (+2.3%)                                                                                                                                                 |
| RX Total              | 91.5 KB (-0.1%)                                                                                                                  | 2.07 MB (+1.6%)                                                                                                                                                | 3.02 MB (-1.8%)                                                                                                                                                  |
| TX Total              | 585.8 KB (+0.0%)                                                                                                                 | 3.45 MB (+1.3%)                                                                                                                                                | 5.13 MB (-0.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250912T033124_922bc02dd/test_idle[waku_light_client_True]-20250912-032410.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250912T033124_922bc02dd/test_one_to_one_messages[waku_light_client_True]-20250912-033042.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250912T033124_922bc02dd/test_one_to_one_messages[waku_light_client_False]-20250912-032726.png) |

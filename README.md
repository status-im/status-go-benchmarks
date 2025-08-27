# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-27)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-27 | 03:11:34 | `f164658bb` |
| Baseline  | 2025-08-26 | 03:15:37 | `77be24219` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.36% (+2.9%)                                                                                                                    | 5.94% (+4.1%)                                                                                                                                                  | 6.05% (+3.8%)                                                                                                                                                    |
| CPU Max               | 145.52% (-3.4%)                                                                                                                  | 162.95% (+7.0%)                                                                                                                                                | 156.67% (-3.1%)                                                                                                                                                  |
| RAM Median            | 51.33 MB (-1.6%)                                                                                                                 | 74.59 MB (-2.8%)                                                                                                                                               | 75.62 MB (+2.3%)                                                                                                                                                 |
| RAM Max               | 51.33 MB (-8.3%)                                                                                                                 | 89.96 MB (+2.6%)                                                                                                                                               | 92.52 MB (+0.5%)                                                                                                                                                 |
| RX Total              | 85.6 KB (+0.2%)                                                                                                                  | 2.05 MB (+0.4%)                                                                                                                                                | 1.97 MB (+16.3%)                                                                                                                                                 |
| TX Total              | 560.1 KB (+0.4%)                                                                                                                 | 3.38 MB (+0.5%)                                                                                                                                                | 3.80 MB (+2.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250827T031134_f164658bb/test_idle[waku_light_client_True]-20250827-030428.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250827T031134_f164658bb/test_one_to_one_messages[waku_light_client_True]-20250827-031049.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250827T031134_f164658bb/test_one_to_one_messages[waku_light_client_False]-20250827-030734.png) |

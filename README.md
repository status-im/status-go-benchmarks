# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-06)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-06 | 03:10:13 | `d7310c53b` |
| Baseline  | 2025-10-05 | 03:08:26 | `3386609cd` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.40% (-9.7%)                                                                                                                    | 5.59% (-11.0%)                                                                                                                                                 | 8.82% (-2.6%)                                                                                                                                                    |
| CPU Max               | 178.49% (+14.3%)                                                                                                                 | 127.09% (-12.9%)                                                                                                                                               | 145.36% (+17.6%)                                                                                                                                                 |
| RAM Median            | 44.21 MB (-8.0%)                                                                                                                 | 66.85 MB (-0.9%)                                                                                                                                               | 67.89 MB (+0.0%)                                                                                                                                                 |
| RAM Max               | 50.96 MB (-13.4%)                                                                                                                | 86.13 MB (-1.2%)                                                                                                                                               | 91.16 MB (-0.4%)                                                                                                                                                 |
| RX Total              | 105.3 KB (+2.1%)                                                                                                                 | 2.01 MB (-1.7%)                                                                                                                                                | 2.94 MB (+3.3%)                                                                                                                                                  |
| TX Total              | 589.5 KB (+0.1%)                                                                                                                 | 3.34 MB (-0.6%)                                                                                                                                                | 5.07 MB (-1.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251006T031013_d7310c53b/test_idle[waku_light_client_True]-20251006-030304.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251006T031013_d7310c53b/test_one_to_one_messages[waku_light_client_True]-20251006-030925.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251006T031013_d7310c53b/test_one_to_one_messages[waku_light_client_False]-20251006-030612.png) |

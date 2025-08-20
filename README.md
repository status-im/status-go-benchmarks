# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-20)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-20 | 03:11:00 | `f78e935b3` |
| Baseline  | 2025-08-19 | 03:14:59 | `6322f2278` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.38% (-1.0%)                                                                                                                    | 6.13% (+9.0%)                                                                                                                                                  | 5.66% (-7.6%)                                                                                                                                                    |
| CPU Max               | 112.56% (-30.2%)                                                                                                                 | 141.64% (-1.4%)                                                                                                                                                | 153.67% (+8.0%)                                                                                                                                                  |
| RAM Median            | 55.43 MB (+1.5%)                                                                                                                 | 73.88 MB (-0.1%)                                                                                                                                               | 74.57 MB (-1.5%)                                                                                                                                                 |
| RAM Max               | 55.43 MB (+1.5%)                                                                                                                 | 83.96 MB (-2.8%)                                                                                                                                               | 88.46 MB (-2.7%)                                                                                                                                                 |
| RX Total              | 88.1 KB (+0.9%)                                                                                                                  | 2.03 MB (+0.4%)                                                                                                                                                | 2.01 MB (+2.6%)                                                                                                                                                  |
| TX Total              | 565.2 KB (+1.0%)                                                                                                                 | 3.35 MB (-0.5%)                                                                                                                                                | 3.78 MB (+0.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250820T031100_f78e935b3/test_idle[waku_light_client_True]-20250820-030352.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250820T031100_f78e935b3/test_one_to_one_messages[waku_light_client_True]-20250820-031017.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250820T031100_f78e935b3/test_one_to_one_messages[waku_light_client_False]-20250820-030703.png) |

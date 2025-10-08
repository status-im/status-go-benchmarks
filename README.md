# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-08)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-08 | 03:08:30 | `c3bd89f1c` |
| Baseline  | 2025-10-07 | 03:10:09 | `c3bd89f1c` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.51% (-1.7%)                                                                                                                    | 7.33% (+34.3%)                                                                                                                                                 | 8.85% (+11.3%)                                                                                                                                                   |
| CPU Max               | 144.22% (-2.7%)                                                                                                                  | 168.25% (+10.6%)                                                                                                                                               | 147.42% (-12.2%)                                                                                                                                                 |
| RAM Median            | 44.84 MB (+1.0%)                                                                                                                 | 67.25 MB (-0.7%)                                                                                                                                               | 67.13 MB (-0.9%)                                                                                                                                                 |
| RAM Max               | 54.13 MB (-0.5%)                                                                                                                 | 89.95 MB (+2.5%)                                                                                                                                               | 88.40 MB (-1.5%)                                                                                                                                                 |
| RX Total              | 103.3 KB (+1.1%)                                                                                                                 | 2.05 MB (+1.7%)                                                                                                                                                | 2.86 MB (+1.0%)                                                                                                                                                  |
| TX Total              | 588.3 KB (-0.0%)                                                                                                                 | 3.38 MB (+0.5%)                                                                                                                                                | 5.16 MB (-0.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251008T030830_c3bd89f1c/test_idle[waku_light_client_True]-20251008-030126.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251008T030830_c3bd89f1c/test_one_to_one_messages[waku_light_client_True]-20251008-030741.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251008T030830_c3bd89f1c/test_one_to_one_messages[waku_light_client_False]-20251008-030433.png) |

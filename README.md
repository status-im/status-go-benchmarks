# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-04)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-04 | 03:11:22 | `3386609cd` |
| Baseline  | 2025-10-02 | 16:13:45 | `106d03f09` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.49% (-3.7%)                                                                                                                    | 6.70% (+9.0%)                                                                                                                                                  | 9.41% (+5.8%)                                                                                                                                                    |
| CPU Max               | 159.88% (+34.2%)                                                                                                                 | 122.58% (-2.4%)                                                                                                                                                | 162.28% (+4.2%)                                                                                                                                                  |
| RAM Median            | 46.97 MB (+13.5%)                                                                                                                | 66.47 MB (-0.5%)                                                                                                                                               | 66.83 MB (-1.8%)                                                                                                                                                 |
| RAM Max               | 51.84 MB (-7.3%)                                                                                                                 | 86.18 MB (-1.8%)                                                                                                                                               | 90.04 MB (-0.9%)                                                                                                                                                 |
| RX Total              | 103.2 KB (-0.4%)                                                                                                                 | 2.06 MB (+0.7%)                                                                                                                                                | 2.83 MB (-5.8%)                                                                                                                                                  |
| TX Total              | 588.9 KB (-0.2%)                                                                                                                 | 3.37 MB (+0.6%)                                                                                                                                                | 5.22 MB (+0.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251004T031122_3386609cd/test_idle[waku_light_client_True]-20251004-030417.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251004T031122_3386609cd/test_one_to_one_messages[waku_light_client_True]-20251004-031033.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251004T031122_3386609cd/test_one_to_one_messages[waku_light_client_False]-20251004-030724.png) |

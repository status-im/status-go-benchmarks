# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-05)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-05 | 03:08:26 | `3386609cd` |
| Baseline  | 2025-10-04 | 03:11:22 | `3386609cd` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.56% (+4.8%)                                                                                                                    | 6.27% (-6.3%)                                                                                                                                                  | 9.06% (-3.7%)                                                                                                                                                    |
| CPU Max               | 156.14% (-2.3%)                                                                                                                  | 145.99% (+19.1%)                                                                                                                                               | 123.57% (-23.9%)                                                                                                                                                 |
| RAM Median            | 48.03 MB (+2.3%)                                                                                                                 | 67.45 MB (+1.5%)                                                                                                                                               | 67.88 MB (+1.6%)                                                                                                                                                 |
| RAM Max               | 58.85 MB (+13.5%)                                                                                                                | 87.21 MB (+1.2%)                                                                                                                                               | 91.52 MB (+1.6%)                                                                                                                                                 |
| RX Total              | 103.1 KB (-0.1%)                                                                                                                 | 2.05 MB (-0.7%)                                                                                                                                                | 2.85 MB (+0.7%)                                                                                                                                                  |
| TX Total              | 589.0 KB (+0.0%)                                                                                                                 | 3.36 MB (-0.2%)                                                                                                                                                | 5.17 MB (-1.1%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251005T030826_3386609cd/test_idle[waku_light_client_True]-20251005-030122.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251005T030826_3386609cd/test_one_to_one_messages[waku_light_client_True]-20251005-030738.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251005T030826_3386609cd/test_one_to_one_messages[waku_light_client_False]-20251005-030428.png) |

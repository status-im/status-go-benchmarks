# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-13)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-13 | 03:08:44 | `49b18eb4b` |
| Baseline  | 2025-10-12 | 03:08:27 | `49b18eb4b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.53% (+4.3%)                                                                                                                    | 6.36% (+18.4%)                                                                                                                                                 | 9.26% (+2.7%)                                                                                                                                                    |
| CPU Max               | 182.64% (+20.9%)                                                                                                                 | 122.56% (-4.1%)                                                                                                                                                | 152.35% (-18.7%)                                                                                                                                                 |
| RAM Median            | 46.79 MB (+6.6%)                                                                                                                 | 68.43 MB (-0.3%)                                                                                                                                               | 68.94 MB (+0.8%)                                                                                                                                                 |
| RAM Max               | 53.36 MB (-2.1%)                                                                                                                 | 87.78 MB (-0.2%)                                                                                                                                               | 91.38 MB (-1.3%)                                                                                                                                                 |
| RX Total              | 102.6 KB (-0.6%)                                                                                                                 | 2.05 MB (+1.6%)                                                                                                                                                | 2.93 MB (+4.1%)                                                                                                                                                  |
| TX Total              | 590.0 KB (+0.2%)                                                                                                                 | 3.35 MB (+0.9%)                                                                                                                                                | 5.23 MB (+1.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251013T030844_49b18eb4b/test_idle[waku_light_client_True]-20251013-030137.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251013T030844_49b18eb4b/test_one_to_one_messages[waku_light_client_True]-20251013-030757.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251013T030844_49b18eb4b/test_one_to_one_messages[waku_light_client_False]-20251013-030445.png) |

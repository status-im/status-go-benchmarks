# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-09)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-09 | 03:09:43 | `938029050` |
| Baseline  | 2025-10-08 | 03:08:30 | `c3bd89f1c` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.47% (-2.8%)                                                                                                                    | 5.71% (-22.1%)                                                                                                                                                 | 8.97% (+1.4%)                                                                                                                                                    |
| CPU Max               | 192.71% (+33.6%)                                                                                                                 | 126.18% (-25.0%)                                                                                                                                               | 181.84% (+23.4%)                                                                                                                                                 |
| RAM Median            | 49.30 MB (+9.9%)                                                                                                                 | 68.61 MB (+2.0%)                                                                                                                                               | 68.23 MB (+1.7%)                                                                                                                                                 |
| RAM Max               | 55.50 MB (+2.5%)                                                                                                                 | 90.63 MB (+0.8%)                                                                                                                                               | 91.26 MB (+3.2%)                                                                                                                                                 |
| RX Total              | 102.8 KB (-0.6%)                                                                                                                 | 2.04 MB (-0.3%)                                                                                                                                                | 2.85 MB (-0.4%)                                                                                                                                                  |
| TX Total              | 582.1 KB (-1.0%)                                                                                                                 | 3.33 MB (-1.4%)                                                                                                                                                | 5.26 MB (+1.9%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251009T030943_938029050/test_idle[waku_light_client_True]-20251009-030242.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251009T030943_938029050/test_one_to_one_messages[waku_light_client_True]-20251009-030855.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251009T030943_938029050/test_one_to_one_messages[waku_light_client_False]-20251009-030547.png) |

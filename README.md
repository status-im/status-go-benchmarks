# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-18)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-18 | 03:08:14 | `dfaefeb7a` |
| Baseline  | 2025-08-17 | 03:08:19 | `dfaefeb7a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.43% (+2.8%)                                                                                                                    | 5.78% (-9.7%)                                                                                                                                                  | 5.72% (-1.0%)                                                                                                                                                    |
| CPU Max               | 167.34% (+15.6%)                                                                                                                 | 137.93% (-1.5%)                                                                                                                                                | 165.11% (-1.8%)                                                                                                                                                  |
| RAM Median            | 50.62 MB (+2.1%)                                                                                                                 | 73.90 MB (-1.5%)                                                                                                                                               | 75.28 MB (+0.2%)                                                                                                                                                 |
| RAM Max               | 50.62 MB (+2.1%)                                                                                                                 | 87.96 MB (-1.7%)                                                                                                                                               | 91.46 MB (+0.5%)                                                                                                                                                 |
| RX Total              | 88.2 KB (-0.0%)                                                                                                                  | 2.04 MB (-1.5%)                                                                                                                                                | 2.04 MB (+1.2%)                                                                                                                                                  |
| TX Total              | 568.1 KB (+0.1%)                                                                                                                 | 3.40 MB (-0.2%)                                                                                                                                                | 3.83 MB (+2.2%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250818T030814_dfaefeb7a/test_idle[waku_light_client_True]-20250818-030109.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250818T030814_dfaefeb7a/test_one_to_one_messages[waku_light_client_True]-20250818-030733.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250818T030814_dfaefeb7a/test_one_to_one_messages[waku_light_client_False]-20250818-030418.png) |

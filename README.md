# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-29)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-29 | 03:12:23 | `78449f196` |
| Baseline  | 2025-08-28 | 03:14:19 | `bfa6eba7b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.40% (-1.8%)                                                                                                                    | 5.66% (-12.1%)                                                                                                                                                 | 5.76% (-10.4%)                                                                                                                                                   |
| CPU Max               | 131.43% (-22.5%)                                                                                                                 | 113.77% (-27.7%)                                                                                                                                               | 166.10% (+32.8%)                                                                                                                                                 |
| RAM Median            | 50.05 MB (-3.9%)                                                                                                                 | 74.39 MB (-0.8%)                                                                                                                                               | 77.48 MB (+3.1%)                                                                                                                                                 |
| RAM Max               | 50.05 MB (-3.9%)                                                                                                                 | 86.09 MB (-3.2%)                                                                                                                                               | 90.96 MB (-0.5%)                                                                                                                                                 |
| RX Total              | 86.5 KB (+0.7%)                                                                                                                  | 2.02 MB (-0.5%)                                                                                                                                                | 1.99 MB (-0.4%)                                                                                                                                                  |
| TX Total              | 567.2 KB (+0.2%)                                                                                                                 | 3.36 MB (+0.5%)                                                                                                                                                | 3.78 MB (-1.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250829T031223_78449f196/test_idle[waku_light_client_True]-20250829-030516.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250829T031223_78449f196/test_one_to_one_messages[waku_light_client_True]-20250829-031135.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250829T031223_78449f196/test_one_to_one_messages[waku_light_client_False]-20250829-030824.png) |

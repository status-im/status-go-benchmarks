# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-10-11)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-10-11 | 03:09:46 | `49b18eb4b` |
| Baseline  | 2025-10-10 | 03:09:23 | `daef4971a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.37% (-2.4%)                                                                                                                    | 5.93% (-8.3%)                                                                                                                                                  | 8.98% (+12.4%)                                                                                                                                                   |
| CPU Max               | 166.07% (+33.1%)                                                                                                                 | 117.41% (-1.7%)                                                                                                                                                | 184.81% (+17.2%)                                                                                                                                                 |
| RAM Median            | 42.96 MB (-13.0%)                                                                                                                | 65.59 MB (+0.0%)                                                                                                                                               | 67.62 MB (-2.8%)                                                                                                                                                 |
| RAM Max               | 49.79 MB (-9.6%)                                                                                                                 | 89.02 MB (+0.4%)                                                                                                                                               | 88.96 MB (-2.3%)                                                                                                                                                 |
| RX Total              | 101.9 KB (-0.8%)                                                                                                                 | 2.02 MB (-0.5%)                                                                                                                                                | 4.12 MB (+37.4%)                                                                                                                                                 |
| TX Total              | 585.1 KB (+0.4%)                                                                                                                 | 3.36 MB (+0.6%)                                                                                                                                                | 5.62 MB (+9.8%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20251011T030946_49b18eb4b/test_idle[waku_light_client_True]-20251011-030241.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20251011T030946_49b18eb4b/test_one_to_one_messages[waku_light_client_True]-20251011-030854.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20251011T030946_49b18eb4b/test_one_to_one_messages[waku_light_client_False]-20251011-030545.png) |

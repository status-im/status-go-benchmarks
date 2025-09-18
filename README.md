# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-18)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-18 | 03:13:15 | `840adb83d` |
| Baseline  | 2025-09-17 | 03:19:21 | `dbadf551c` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.34% (+10.6%)                                                                                                                   | 5.17% (-0.9%)                                                                                                                                                  | 7.17% (-9.3%)                                                                                                                                                    |
| CPU Max               | 111.95% (-2.0%)                                                                                                                  | 112.83% (-0.8%)                                                                                                                                                | 112.11% (-12.5%)                                                                                                                                                 |
| RAM Median            | 46.38 MB (+7.7%)                                                                                                                 | 64.26 MB (-0.1%)                                                                                                                                               | 66.42 MB (+2.7%)                                                                                                                                                 |
| RAM Max               | 49.50 MB (-2.5%)                                                                                                                 | 73.15 MB (+6.3%)                                                                                                                                               | 81.60 MB (+5.6%)                                                                                                                                                 |
| RX Total              | 91.0 KB (+0.2%)                                                                                                                  | 2.04 MB (-2.3%)                                                                                                                                                | 3.13 MB (-9.5%)                                                                                                                                                  |
| TX Total              | 579.2 KB (-0.2%)                                                                                                                 | 3.44 MB (-1.9%)                                                                                                                                                | 5.19 MB (-4.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250918T031315_840adb83d/test_idle[waku_light_client_True]-20250918-030551.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250918T031315_840adb83d/test_one_to_one_messages[waku_light_client_True]-20250918-031229.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250918T031315_840adb83d/test_one_to_one_messages[waku_light_client_False]-20250918-030908.png) |

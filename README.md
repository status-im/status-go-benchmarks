# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-03)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-03 | 03:14:45 | `5a7fbaae7` |
| Baseline  | 2025-09-02 | 03:11:34 | `32943ca33` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.34% (-4.4%)                                                                                                                    | 6.38% (+11.1%)                                                                                                                                                 | 6.01% (+3.1%)                                                                                                                                                    |
| CPU Max               | 161.25% (+4.6%)                                                                                                                  | 115.03% (-28.6%)                                                                                                                                               | 127.77% (-0.1%)                                                                                                                                                  |
| RAM Median            | 53.58 MB (+5.4%)                                                                                                                 | 73.73 MB (-1.6%)                                                                                                                                               | 76.29 MB (+3.2%)                                                                                                                                                 |
| RAM Max               | 53.58 MB (+5.4%)                                                                                                                 | 87.15 MB (-4.3%)                                                                                                                                               | 89.90 MB (-2.6%)                                                                                                                                                 |
| RX Total              | 88.3 KB (+2.5%)                                                                                                                  | 2.04 MB (-0.7%)                                                                                                                                                | 2.06 MB (+3.9%)                                                                                                                                                  |
| TX Total              | 567.6 KB (+0.7%)                                                                                                                 | 3.37 MB (-0.5%)                                                                                                                                                | 3.79 MB (+1.3%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250903T031445_5a7fbaae7/test_idle[waku_light_client_True]-20250903-030737.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250903T031445_5a7fbaae7/test_one_to_one_messages[waku_light_client_True]-20250903-031359.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250903T031445_5a7fbaae7/test_one_to_one_messages[waku_light_client_False]-20250903-031047.png) |

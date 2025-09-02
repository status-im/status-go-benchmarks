# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-09-02)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-09-02 | 03:11:34 | `32943ca33` |
| Baseline  | 2025-09-01 | 03:10:59 | `d03b7b5ed` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.40% (+2.3%)                                                                                                                    | 5.74% (+5.5%)                                                                                                                                                  | 5.84% (+1.9%)                                                                                                                                                    |
| CPU Max               | 154.23% (+19.0%)                                                                                                                 | 161.17% (+4.6%)                                                                                                                                                | 127.96% (-7.1%)                                                                                                                                                  |
| RAM Median            | 50.84 MB (-9.5%)                                                                                                                 | 74.93 MB (+0.4%)                                                                                                                                               | 73.90 MB (-2.2%)                                                                                                                                                 |
| RAM Max               | 50.84 MB (-9.5%)                                                                                                                 | 91.05 MB (+4.2%)                                                                                                                                               | 92.27 MB (+0.3%)                                                                                                                                                 |
| RX Total              | 86.1 KB (-1.1%)                                                                                                                  | 2.06 MB (+1.5%)                                                                                                                                                | 1.98 MB (-0.0%)                                                                                                                                                  |
| TX Total              | 563.5 KB (+0.9%)                                                                                                                 | 3.39 MB (+1.1%)                                                                                                                                                | 3.75 MB (-0.0%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250902T031134_32943ca33/test_idle[waku_light_client_True]-20250902-030422.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250902T031134_32943ca33/test_one_to_one_messages[waku_light_client_True]-20250902-031046.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250902T031134_32943ca33/test_one_to_one_messages[waku_light_client_False]-20250902-030732.png) |

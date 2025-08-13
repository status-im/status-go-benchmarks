# status-go-benchmarks

Benchmark metrics with 30-day history and latest comparison.

## 30-Day History

| Metric History                                         | Metric History                                     |
|--------------------------------------------------------|----------------------------------------------------|
| ![cpu_median_history.png](docs/cpu_median_history.png) | ![cpu_max_history.png](docs/cpu_max_history.png)   |
| ![ram_median_history.png](docs/ram_median_history.png) | ![ram_max_history.png](docs/ram_max_history.png)   |
| ![rx_total_history.png](docs/rx_total_history.png)     | ![tx_total_history.png](docs/tx_total_history.png) |

## Latest Report (2025-08-13)

| Run       | Date       | Time     | Commit      |
|-----------|------------|----------|-------------|
| Contender | 2025-08-13 | 13:23:10 | `cc234c1ad` |
| Baseline  | 2025-08-13 | 10:56:18 | `d1a4de48b` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.47% (+18.8%)                                                                                                                   | 5.73% (+5.3%)                                                                                                                                                  | 5.44% (+5.6%)                                                                                                                                                    |
| CPU Max               | 139.52% (-3.3%)                                                                                                                  | 129.70% (+0.8%)                                                                                                                                                | 136.84% (-22.1%)                                                                                                                                                 |
| RAM Median            | 54.08 MB (-3.1%)                                                                                                                 | 78.07 MB (+3.1%)                                                                                                                                               | 77.05 MB (+2.3%)                                                                                                                                                 |
| RAM Max               | 62.32 MB (+11.1%)                                                                                                                | 88.52 MB (-0.0%)                                                                                                                                               | 92.27 MB (+3.8%)                                                                                                                                                 |
| RX Total              | 88.3 KB (-1.9%)                                                                                                                  | 2.04 MB (-0.7%)                                                                                                                                                | 2.02 MB (-1.4%)                                                                                                                                                  |
| TX Total              | 568.1 KB (-0.8%)                                                                                                                 | 3.36 MB (-1.6%)                                                                                                                                                | 3.78 MB (-1.8%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250813T132310_cc234c1ad/test_idle[waku_light_client_True]-20250813-131604.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250813T132310_cc234c1ad/test_one_to_one_messages[waku_light_client_True]-20250813-132230.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250813T132310_cc234c1ad/test_one_to_one_messages[waku_light_client_False]-20250813-131915.png) |

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
| Contender | 2025-08-13 | 19:13:55 | `493fd1b03` |
| Baseline  | 2025-08-13 | 16:27:34 | `00c0d1c3a` |

| Metric                | test_idle<br>[waku_light_client_True]                                                                                            | test_one_to_one_messages<br>[waku_light_client_True]                                                                                                           | test_one_to_one_messages<br>[waku_light_client_False]                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Median            | 1.20% (+0.4%)                                                                                                                    | 5.97% (-0.6%)                                                                                                                                                  | 5.88% (-0.9%)                                                                                                                                                    |
| CPU Max               | 137.69% (-25.4%)                                                                                                                 | 151.06% (+39.4%)                                                                                                                                               | 144.17% (+28.7%)                                                                                                                                                 |
| RAM Median            | 49.71 MB (-8.1%)                                                                                                                 | 73.91 MB (-1.5%)                                                                                                                                               | 76.09 MB (-3.1%)                                                                                                                                                 |
| RAM Max               | 51.58 MB (-4.6%)                                                                                                                 | 87.03 MB (+0.7%)                                                                                                                                               | 86.71 MB (-4.3%)                                                                                                                                                 |
| RX Total              | 87.2 KB (-1.6%)                                                                                                                  | 2.04 MB (-0.1%)                                                                                                                                                | 2.02 MB (+0.7%)                                                                                                                                                  |
| TX Total              | 566.5 KB (-1.2%)                                                                                                                 | 3.38 MB (-0.7%)                                                                                                                                                | 3.85 MB (+0.7%)                                                                                                                                                  |
| **Performance Chart** | ![test_idle[waku_light_client_True]](benchmarks/20250813T191355_493fd1b03/test_idle[waku_light_client_True]-20250813-190648.png) | ![test_one_to_one_messages[waku_light_client_True]](benchmarks/20250813T191355_493fd1b03/test_one_to_one_messages[waku_light_client_True]-20250813-191315.png) | ![test_one_to_one_messages[waku_light_client_False]](benchmarks/20250813T191355_493fd1b03/test_one_to_one_messages[waku_light_client_False]-20250813-191000.png) |

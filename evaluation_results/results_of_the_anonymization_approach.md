# Anonymization of the (year_of_birth, sex, municipality) QID

It contains the results for the anonymization approach provided in the src directory the datasets published in https://github.com/isislab-unisa/driver-license-datasets.
The best results are provided by a local recording (only affecting rows related to the singletons exposed by the (year_of_birth, sex, municipality) QID) and the generalization of the municipality (and sex) column(s).
|                                 |                 | Valle Aosta | Umbria | Molise |
|--------------------------------:|-----------------|:-----------:|:------:|:------:|
|                        original | Singleton #     |        1684 |    869 |   2569 |
|                                 | Singleton %     |           2 |      0 |      1 |
|                                 | Size            |       87642 | 597492 | 198524 |
|                                 | Removed         |         178 |    249 |    212 |
|                                 | Distinct values |        9174 |  13391 |  16628 |
|                                 | Original size   |       87464 | 597243 | 198312 |
|                                 |                 |             |        |        |
|                         sex_all | Singleton #     |         621 |    295 |    909 |
|                                 | Singleton %     |           1 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |        5166 |   7101 |   9490 |
|                                 | % of singleton  |       0.71% |  0.05% |  0.46% |
|                                 |                 |             |        |        |
|                   sex_singleton | Singleton #     |        1264 |    745 |   2129 |
|                                 | Singleton %     |           1 |      0 |      1 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |        1684 |    869 |   2569 |
|                                 | Distinct values |        8964 |  13329 |  16408 |
|                                 | % of singleton  |       1.45% |  0.12% |  1.07% |
|                                 |                 |             |        |        |
|                municipality_all | Singleton #     |           4 |      6 |      7 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 414584 | 198312 |
|                                 | Distinct values |         167 |    338 |    324 |
|                                 | % of singleton  |          0% |     0% |     0% |
|                                 |                 |             |        |        |
|          municipality_singleton | Singleton #     |           4 |      7 |      7 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |        1679 |    860 |   2556 |
|                                 | Distinct values |        7501 |  12539 |  14078 |
|                                 | % of singleton  |          0% |     0% |     0% |
|                                 |                 |             |        |        |
|                      year_range | Singleton #     |         198 |    127 |    325 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |        2739 |   3641 |   4806 |
|                                 | % of singleton  |       0.23% |  0.02% |  0.16% |
|                                 |                 |             |        |        |
|                       year_mean | Singleton #     |           9 |      1 |      3 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       81476 | 556875 | 184111 |
|                                 | Distinct values |         607 |    736 |   1089 |
|                                 | % of singleton  |       0.01% |     0% |     0% |
|                                 |                 |             |        |        |
|            sex_municipality_all | Singleton #     |           1 |      1 |      7 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |          85 |    171 |    324 |
|                                 | % of singleton  |          0% |     0% |     0% |
|                                 |                 |             |        |        |
|      sex_municipality_singleton | Singleton #     |           1 |     32 |      3 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |        1684 |    868 |   2569 |
|                                 | Distinct values |        7785 |  12680 |  14446 |
|                                 | % of singleton  |          0% |  0.01% |     0% |
|                                 |                 |             |        |        |
|              sex_all_year_range | Singleton #     |          70 |     48 |    116 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |        1442 |   1895 |   2606 |
|                                 | % of singleton  |          0% |  0.01% |  0.06% |
|                                 |                 |             |        |        |
|               sex_all_year_mean | Singleton #     |           5 |      0 |      1 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |         308 |    368 |    545 |
|                                 | % of singleton  |       0.08% |  0.01% |  0.06% |
|                                 |                 |             |        |        |
|     year_range_municipality_all | Singleton #     |           0 |      0 |      0 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |          43 |     44 |     84 |
|                                 | % of singleton  |           0 |      0 |      0 |
|                                 |                 |             |        |        |
|      year_mean_municipality_all | Singleton #     |           0 |      0 |      0 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       85948 | 584794 | 194932 |
|                                 | Distinct values |        8817 |      8 |     16 |
|                                 | % of singleton  |           0 |      0 |      0 |
|                                 |                 |             |        |        |
| sex_municipality_all_year_range | Singleton #     |           0 |      0 |      0 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |          22 |     44 |     43 |
|                                 | % of singleton  |           0 |      0 |      0 |
|                                 |                 |             |        |        |
|  sex_municipality_all_year_mean | Singleton #     |           0 |      0 |      0 |
|                                 | Singleton %     |           0 |      0 |      0 |
|                                 | Removed tuples  |           0 |      0 |      0 |
|                                 | Modified tuples |       87464 | 597243 | 198312 |
|                                 | Distinct values |           4 |      8 |      8 |
|                                 | % of singleton  |           0 |      0 |      0 |
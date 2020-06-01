# QID and esposed singletons

It contains the best QID (minimum number of columns that exposes the greatest number of singletons) detected by the src/privacy_checker.py on the datasets published in https://github.com/isislab-unisa/driver-license-datasets.

|         *Region*        | *Original Size* | *Removed Rows* | *Dataset Size* |              *Best QID*             | *Number of Singletons* | *Percentage of Singletons* | *Distinct values* | *Execution Time (s)* |
|:---------------------:|:-------------:|:------------:|:------------:|:---------------------------------:|:--------------------:|:------------------------:|:---------------:|:------------------:|
| Puglia                |       2478643 |         3023 |      2475620 | [Birth_year, Municipality,Gender] |                 1859 |                    0.08% |           37439 |               0.49 |
| Toscana               |       2499005 |         1322 |      2497683 | [Birth_year, Municipality,Gender] |                 2028 |                    0.08% |           41908 |               0.48 |
| Emilia Romagna        |       2985475 |         1803 |      2983672 | [Birth_year, Municipality,Gender] |                 2642 |                    0.09% |           51575 |               1.02 |
| Sicilia               |       3130564 |         4921 |      3125643 | [Birth_year, Municipality,Gender] |                 3483 |                    0.11% |           55922 |               1.03 |
| Lazio                 |       3746346 |         2107 |      3744239 | [Birth_year, Municipality,Gender] |                 4980 |                    0.13% |           51809 |               1.09 |
| Umbria                |        597492 |          249 |       597243 | [Birth_year, Municipality,Gender] |                  869 |                    0.15% |           13391 |               0.12 |
| Veneto                |       3319136 |         3271 |      3315865 | [Birth_year, Municipality,Gender] |                 4835 |                    0.15% |           85265 |               1.06 |
| Campania              |       3351485 |         1454 |      3350031 | [Birth_year, Municipality,Gender] |                 5498 |                    0.16% |           75377 |               1.13 |
| Marche                |       1049335 |         1030 |      1048305 | [Birth_year, Municipality,Gender] |                 2535 |                    0.24% |           33021 |               0.21 |
| Lombardia             |       6444079 |         6867 |      6437212 | [Birth_year, Municipality,Gender] |                18948 |                    0.29% |          210853 |               2.32 |
| Friuli Venezia Giulia |        828475 |         1034 |       827441 | [Birth_year, Municipality,Gender] |                 2688 |                    0.32% |           30528 |               0.16 |
| Calabria              |       1178562 |         1913 |      1176649 | [Birth_year, Municipality,Gender] |                 4904 |                    0.42% |           54024 |               0.24 |
| Basilicata            |        358073 |          160 |       357913 | [Birth_year, Municipality,Gender] |                 1537 |                    0.43% |           17360 |               0.07 |
| Liguria               |        974859 |         1053 |       973806 | [Birth_year, Municipality,Gender] |                 4374 |                    0.45% |           31416 |               0.18 |
| Sardegna              |       1040609 |          599 |      1040010 | [Birth_year, Municipality,Gender] |                 5631 |                    0.54% |           48351 |               0.21 |
| Abruzzo               |        870683 |         6751 |       863932 | [Birth_year, Municipality,Gender] |                 5221 |                    0.60% |           39102 |               0.02 |
| Piemonte              |       2899772 |         2554 |      2897218 | [Birth_year, Municipality,Gender] |                25211 |                    0.87% |          154041 |               0.06 |
| Trentino              |        692328 |         1758 |       690570 | [Birth_year, Municipality,Gender] |                 6410 |                    0.93% |           46488 |               0.15 |
| Molise                |        198525 |          213 |       198312 | [Birth_year, Municipality,Gender] |                 2569 |                    1.30% |           16628 |               0.04 |
| Valle Aosta           |         87643 |          179 |        87464 | [Birth_year, Municipality,Gender] |                 1684 |                    1.93% |            9174 |               0.02 |
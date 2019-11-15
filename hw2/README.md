#### CS541 - Artificial Intelligence
#### Student: Ovidiu Mura
#### Email: mura@pdx.edu
#### Date: Nov 14, 2019
#### Assignment 2: Heart Anomalies
##### Requirements: https://github.com/pdx-cs-ai/heart-anomaly-hw

I built Naive Bayesian and k-Nearest-Neighboar machine learners to diagnose heart anomalies from radiology datasests.

Naive Bayesian results:

orig 142/187(0.76)  10/15(0.67)  132/172(0.77)
itg 145/187(0.78)  15/15(1.0)  130/172(0.76)
resplit 78/90(0.87)  17/19(0.89)  61/71(0.86)
resplit-itg 63/90(0.7)  17/19(0.89)  46/71(0.65)
spect 142/187(0.76)  10/15(0.67)  132/172(0.77)

k-Nearest-Neighbor results:

orig 139/187(0.74)  10/15(0.67)  129/172(0.75)
itg 126/187(0.67)  12/15(0.8)  114/172(0.66)
resplit 75/90(0.83)  14/19(0.74)  61/71(0.86)
resplit-itg 64/90(0.71)  18/19(0.95)  46/71(0.65)
spect 139/187(0.74)  10/15(0.67)  129/172(0.75)


#### To diagnose heart anomalies from the given dataset, please execute the following command:
###### $> make
####
#### The make command will execute all 2 goals, each goal executing all the 5 datasets (train/test)
#### nb - goal will execute the Naive Bayesian, knn - goal will execute the k-Nearest-Neighbor
####

Abstract: Both learners are implemented in Python3 programming language. In this application, the accuracy
on normal instances, `true positive rate`, is more important. The best results are given by the resplit dataset for both learners nb and knn.

Comparing Naive Bayesian (nb) results with k-Nearest-Neighbor (knn) results:


| accuracy | orig | itg | resplit | resplit-itg | spect |
| --- | --- | --- | --- | --- | --- |
| naive bayesian | 0.76 | 0.78 | 0.87 | 0.7 | 0.76 |
| k-nearest-neighbor | 0.74 | 0.67 | 0.83 | 0.71 | 0.74 |
| `best performance` | nb | nb | nb | knn | nb |


| `true negative rate` | orig | itg | resplit | resplit-itg | spect |
| --- | --- | --- | --- | --- | --- |
| naive bayesian | 0.67 | 1.0 | 0.89 | 0.89 | 0.67 |
| k-nearest-neighbor | 0.67 | 0.8 | 0.74 | 0.95 | 0.67 |
| `best performance` | = | nb | nb | knn | nb |


| `true positive rate` | orig | itg | resplit | resplit-itg | spect |
| --- | --- | --- | --- | --- | --- |
| naive bayesian | 0.77 | 0.76 | 0.86 | 0.65 | 0.77 |
| k-nearest-neighbor | 0.75 | 0.66 | 0.86 | 0.65 | 0.75 |
| `best performance` | nb | nb | = | = | nb |


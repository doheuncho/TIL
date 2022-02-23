# Description

* Binary classification of p2p loan's customer defaults

# Evaluation

* F1 macro
* Private 100%

# Data

* 76 cols
* 100000 rows for train data
* 35816 rows for test data

# My works
* change unnecessary one-hot encode columns to one feature
* remove duplicated features
* remove outliar
* K-Fold Cross Validation with F1 macro score
* LOFO(Leave One Feature Out)

# My score

* Public : 0.7158(27 / 58)
* Private : 0.7128(8 / 58)

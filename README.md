# Next basket recommendation

The task of next basket recommendation is to predict a content of customers basket at their future purchase.

Task has been assigned as a competition among the students who took the Algorithms of data mining course at Faculty of 
Information Technology @ Czech Technical University in Prague.

### Scoring function

The competition has been divided into 2 rounds. The difference between rounds is the used scoring function.
1st round scoring function is Jaccard similarity coefficient

$J(A,B) = \frac{ |A \cap B| }{ |A \cup B| }$,

where A is a real basket and B is a predicted one. Final score is a mean of $J(A,B)$ over all predictions.
2nd round scoring function is Generalized Jaccard similarity coefficient over multisets

$J_g(A,B) = \frac{ \sum_i min(a_i, b_i) }{ \sum_i max(a_i, b_i) }$,

where A is a real basket and B is a predicted one. Final score is a mean of $J_g(A,B)$ over all predictions. Generalized
jaccard index takes into account cases where there is multiple occurrences of same products in one basket. Therefore the
scoring function is stricter.

### Solutions

**Top frequency** solution to this problem is in jupyter notebook [here](top-frequency.ipynb).

------------------------

Score in 1st rnd: TBA

Score in 2nd rnd: TBA

---------------------------

**Multilabel classification** solution to this problem is in jupyter notebook [here](multilabel-classification.ipynb).

------------------------

Score in 1st rnd: TBA

Score in 2nd rnd: TBA

---------------------------

Unfortunately I cannot provide the data for the problem as to avoid any legal issues. The data has been provided by
a external company in collaboration with the university.

```python
from Levenshtein import distance as levenshtein_distance

BASE_SENTENCE = "This is a base sentence to compare to."
YOUR_ATTRIBUTE = "text
WEIGHTS = (1, 1, 1) # Optional, for (insertion, deletion, substitution).

def fn_levenshtein_distance(record):
    str_01 = BASE_SENTENCE
    str_02 = record[YOUR_ATTRIBUTE].text
    
    weights = WEIGHTS

    if weights is not None:
        weights_tuple = (
            weights["insertion"],
            weights["deletion"],
            weights["substitution"],
        )
        ls_distance = levenshtein_distance(str_01, str_02, weights=weights_tuple)
    else:
        ls_distance = levenshtein_distance(str_01, str_02)
    return ls_distance
```
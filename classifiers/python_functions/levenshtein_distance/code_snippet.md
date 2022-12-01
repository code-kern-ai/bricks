```python
from Levenshtein import distance as levenshtein_distance

YOUR_BASE_SENTENCE: str = "This is a base sentence to compare to."
YOUR_ATTRIBUTE: str = "text"
YOUR_WEIGHTS = (1, 1, 1) # Optional, for (insertion, deletion, substitution).

def fn_levenshtein_distance(record):
    str_01 = YOUR_BASE_SENTENCE
    str_02 = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    
    weights = YOUR_WEIGHTS

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
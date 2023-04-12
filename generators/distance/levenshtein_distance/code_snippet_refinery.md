```python
from Levenshtein import distance as levenshtein_distance

BASE_SENTENCE: str = "This is a base sentence to compare to."
ATTRIBUTE: str = "headline" #only text attributes
WEIGHT_INSERTION: int = 1 # Optional
WEIGHT_DELETION: int = 1 # Optional
WEIGHT_SUBSTITUTION: int = 1 # Optional

def levenshtein_distance(record):
    str_01 = BASE_SENTENCE
    str_02 = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    
    if WEIGHT_INSERTION is not None and WEIGHT_DELETION is not None and WEIGHT_SUBSTITUTION is not None:
        weights_tuple = (
            WEIGHT_INSERTION,
            WEIGHT_DELETION,
            WEIGHT_SUBSTITUTION,
        )
        ls_distance = levenshtein_distance(str_01, str_02, weights=weights_tuple)
    else:
        ls_distance = levenshtein_distance(str_01, str_02)
    return ls_distance
```
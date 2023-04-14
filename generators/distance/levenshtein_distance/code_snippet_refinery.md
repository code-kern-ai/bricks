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
    
    weights_tuple = [1,1,1]
    if WEIGHT_INSERTION is not None:
        weights_tuple[0] = WEIGHT_INSERTION
    if WEIGHT_DELETION is not None:
        weights_tuple[1] = WEIGHT_DELETION
    if WEIGHT_SUBSTITUTION is not None:
        weights_tuple[2] = WEIGHT_SUBSTITUTION
    return levenshtein_distance(str_01, str_02, weights=tuple(weights_tuple))
```
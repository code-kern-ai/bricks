```python
from Levenshtein import distance as levenshtein_distance

YOUR_BASE_SENTENCE: str = "This is a base sentence to compare to."
YOUR_ATTRIBUTE: str = "headline" #only text attributes
YOUR_WEIGHT_INSERTION: int = 1 # Optional
YOUR_WEIGHT_DELETION: int = 1 # Optional
YOUR_WEIGHT_SUBSTITUTION: int = 1 # Optional

def levenshtein_distance_func(record):
    str_01 = YOUR_BASE_SENTENCE
    str_02 = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    
    if YOUR_WEIGHT_INSERTION is not None and YOUR_WEIGHT_DELETION is not None and YOUR_WEIGHT_SUBSTITUTION is not None:
        weights_tuple = (
            YOUR_WEIGHT_INSERTION,
            YOUR_WEIGHT_DELETION,
            YOUR_WEIGHT_SUBSTITUTION,
        )
        ls_distance = levenshtein_distance(str_01, str_02, weights=weights_tuple)
    else:
        ls_distance = levenshtein_distance(str_01, str_02)
    return ls_distance
```
```python
from typing import Dict
from Levenshtein import distance as levenshtein_distance

def fn_levenshtein_distance(record: Dict[str, Any]):
    str_01 = record["text_first"] 
    str_02 = record["text_second"]
    
    weights = record.get("weights")

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
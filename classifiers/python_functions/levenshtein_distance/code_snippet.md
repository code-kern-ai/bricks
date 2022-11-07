```python
from typing import Dict
from Levenshtein import distance as levenshtein_distance

def fn_levenshtein_distance(record: Dict[str, Any]):
    str_01 = record["text_first"] 
    str_02 = record["text_second"]
    weights = record["weights"]

    if weights is not None:
        ls_distance = levenshtein_distance(str_01, str_02, weights=weights)
    else:
        ls_distance = levenshtein_distance(str_01, str_02)
    return {"Levenshtein distance": ls_distance}
```
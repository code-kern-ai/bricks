```python
from typing import List, Tuple
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "work of art"

def work_of_art_extraction(record) -> List[Tuple[str, int, int]]:
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield YOUR_LABEL, entity.start, entity.end
```
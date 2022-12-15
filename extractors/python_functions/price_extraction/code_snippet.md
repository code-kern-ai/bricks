```python
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "price"

def price_extractor(record) -> List[Tuple[str, int, int]]:
    doc = record[YOUR_ATTRIBUTE] # SpaCy doc

    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            yield YOUR_LABEL, entity.start, entity.end
```
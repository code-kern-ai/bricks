```python
from typing import Dict, List, Tuple, Any

def price_extractor(record: Dict[str, Any]) -> List[Tuple[str, int, int]]:
    text = record["text"]

    for entity in text.ents:
        if entity.label_ == 'MONEY':
            yield "price", entity.start, entity.end
```
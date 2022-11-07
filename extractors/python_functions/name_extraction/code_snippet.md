```python
from typing import Dict, Any, List, Tuple

def name_extraction(record: Dict[str, Any]) -> List[Tuple[str, int, int]]:
    """
    Returns a dictionary of the extracted names from a given text.
    """

    text = record["your-text"]
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            yield "person", entity.start, entity.end
```
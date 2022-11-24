```python
from typing import Dict, Any, List, Tuple

def org_extraction(record: Dict[str, Any]) -> List[Tuple[str, int, int]]:
    """
    Returns a dictionary of the extracted orgs from a given text.
    """

    text = record["your-text"]
    for entity in doc.ents:
        if entity.label_ == "ORG":
            yield "org", entity.start, entity.end
```
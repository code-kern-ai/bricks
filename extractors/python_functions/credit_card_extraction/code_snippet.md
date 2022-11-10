```python
from typing import Dict, Any, List, Tuple
import re

def credit_extractor(record: Dict[str, Any]) -> List[Tuple[str, int, int]]:
    regex = re.compile(
        r"(\d{4}[-\s]?){3}\d{3,4}"
    )
    
    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
        yield "creditCard", span.start, span.end
```
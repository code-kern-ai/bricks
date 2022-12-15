```python
import re
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "IP-address"

def ip_extractor(record) -> List[Tuple[str, int, int]]:
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```
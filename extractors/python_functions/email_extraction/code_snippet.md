```python
import re
from typing import List, Tuple

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "email"

def email_extractor(record) -> List[Tuple[str, int, int]]:
    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```
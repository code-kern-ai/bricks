```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "IP-address"

def ip_extraction(record):
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
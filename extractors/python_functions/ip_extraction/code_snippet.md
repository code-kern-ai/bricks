```python
import re

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "ipAddress"

def ip_extractor(record):
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield "ip_address", span.start, span.end
```
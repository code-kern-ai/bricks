```python
import re

YOUR_ATTRIBUTE: str = "your-text"
YOUR_LABEL: str = "isbn"

def isbn_ext(record):
    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
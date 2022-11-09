```python
import re

def isbn_ext(record):

    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")

    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
        yield "isbn", span.start, span.end
```
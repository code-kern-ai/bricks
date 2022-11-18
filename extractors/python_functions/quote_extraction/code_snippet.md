```python
import re

def quote_extraction(record):
    
    regex = re.compile(r"\".*?\"")

    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
        yield "quote", span.start, span.end
```
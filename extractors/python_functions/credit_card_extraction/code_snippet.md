```python
import re

YOUR_ATTRIBUTE = "your-text"

def credit_extractor(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to use .text to the the string.

    regex = re.compile(
        r"(\d{4}[-\s]?){3}\d{3,4}"
    )
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield "creditCard", span.start, span.end
```
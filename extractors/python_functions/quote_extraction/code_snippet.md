```python
import re

YOUR_ATTRIBUTE: str = "text" # Choose any available attribute her
YOUR_LABEL: str = "quote"

def quote_extraction(record):
    regex = re.compile(r"\".*?\"")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
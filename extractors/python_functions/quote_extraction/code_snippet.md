```python
import re

YOUR_ATTRIBUTE = "your-text" # Choose any available attribute her

def quote_extraction(record):
    regex = re.compile(r"\".*?\"")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield "quote", span.start, span.end
```
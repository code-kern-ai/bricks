```python
import re

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "hashtag"

def hashtag_extractor(record):
    regex = re.compile(r"#(\w+)")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
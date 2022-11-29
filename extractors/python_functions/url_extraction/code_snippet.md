```python
import re

YOUR_ATTRIBUTE: str = "text" # Choose any available attribute here.
YOUR_LABEL: str = "url"

def url_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")

    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
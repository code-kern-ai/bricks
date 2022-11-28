```python
import re

YOUR_ATTRIBUTE = "your-text"

def email_extractor(record):
    regex = re.compile(r"#(\w+)")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    emails = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        emails.append([span.start, span.end, span.text])
```
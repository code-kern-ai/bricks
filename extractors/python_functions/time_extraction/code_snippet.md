```python
import re

YOUR_ATTRIBUTE = "your-text" # Choose any available attribute here

def time_extraction(record):
    regex = re.compile(
        r"(?:(?:[0-9]{1,2}(?::[0-9]{1,2}(?::[0-9]{1,2}:?)?)?)(?:(?: )?am|(?: )?pm|(?: )?AM|(?: )?PM)?)"
    )
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield "time", span.start, span.end
```
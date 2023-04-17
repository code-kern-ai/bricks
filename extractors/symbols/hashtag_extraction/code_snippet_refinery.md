```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "hashtag"

def hashtag_extraction(record):
    regex = re.compile(r"#(\w*)")
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
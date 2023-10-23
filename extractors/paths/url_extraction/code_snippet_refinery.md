```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "url"

def url_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    regex_pattern = re.compile(r"(?:(?:(?:https?|ftp):\/\/){1})?[\w\-\/?=%.]{3,}\.[\/\w\-&?=%.]{2,}")

    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
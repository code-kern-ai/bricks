```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "bic"

def bic_extraction(record):
    regex = re.compile(r'\b[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z2-9][A-NP-Z0-9]([X]{3,3}|[A-WY-Z0-9]{1,1}[A-Z0-9]{2,2}|\s|\W|$)')
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
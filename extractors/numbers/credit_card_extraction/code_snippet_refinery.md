```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "cardNumber"

def credit_card_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to use .text to the string.

    regex = re.compile(
        r"(\d{4}[-\s]?){3}\d{3,4}"
    )
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
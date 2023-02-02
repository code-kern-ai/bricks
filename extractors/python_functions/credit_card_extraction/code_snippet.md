```python
import re

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "cardNumber"

def credit_card_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to use .text to the string.

    regex = re.compile(
        r"(\d{4}[-\s]?){3}\d{3,4}"
    )
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```
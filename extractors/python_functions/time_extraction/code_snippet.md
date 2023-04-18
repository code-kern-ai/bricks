```python
import re

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "time"

def time_extraction(record):
    regex = re.compile(
        r"\b(1[0-2]|[1-9])\s*[apAP][. ]*[mM]\.?|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?(?:(?:\s?[ap](?:\.m\.)?)|(?:\s?[AP](?:\.M\.)?)))|(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?"
    )
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```
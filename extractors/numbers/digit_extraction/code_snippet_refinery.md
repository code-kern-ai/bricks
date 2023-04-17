```python
import re

ATTRIBUTE: str = "text" # only text attributes
MAX_NUMBER_LENGTH: int = 4 #maximum amount of digits to be considered relevant 
LABEL: str = "digit"

def digit_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string
    number = MAX_NUMBER_LENGTH

    num_string = "{"+f"{number}"+"}"
    regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```

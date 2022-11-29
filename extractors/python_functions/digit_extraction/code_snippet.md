```python
import re

YOUR_ATTRIBUTE: str = "text"
YOUR_NUM_AMOUNT: int = 4
YOUR_LABEL: str = "digit"

def digit_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string
    number = YOUR_NUM_AMOUNT

    num_string = "{"+f"{number}"+"}"
    regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```

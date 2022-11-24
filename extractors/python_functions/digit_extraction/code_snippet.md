```python
import re

YOUR_ATTRIBUTE = "text"
YOUR_NUM_AMOUNT = 4

def digit_extraction(record):
    text = record[YOUR_ATTRIBUTE].text
    number = YOUR_NUM_AMOUNT

    num_string = "{"+f"{number}"+"}"
    regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")

    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield "Number", span.start, span.end
```

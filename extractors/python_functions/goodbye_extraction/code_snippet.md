```python
import re

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "goodbye"

def goodbye_extraction(record):
    regex = re.compile(r"((?:(good|Good)(?:[ ])?)?(bye|Bye)|Ciao|ciao|(?:(see you|See you)(?:[ ]?)(tomorrow|later|soon)?))")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
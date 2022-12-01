```python
import re

#currently only english language is supported here
#reach out to us if this should be extended for other languages

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "goodbye"

def goodbye_extraction(record):
    regex = re.compile(r"((?:(good|Good)(?:[ ])?)?(bye|Bye)|Ciao|ciao|(?:(see you|See you)(?:[ ]?)(tomorrow|later|soon)?))")
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
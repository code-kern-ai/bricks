```python
import re

#currently only english language is supported here
#reach out to us if this should be extended for other languages

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "goodbye"

def goodbye_extraction(record):
    regex = re.compile(r"((?:((?i)good)(?:[ ])?)?((?i)bye)|(?i)Ciao|(?:((?i)see you)(?:[ ]?)((?i)tomorrow|later|soon)?))")
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
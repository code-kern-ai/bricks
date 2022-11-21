```python
import re

def goodbye_extraction(record):

    regex = re.compile(r"((?:(good|Good)(?:[ ])?)?(bye|Bye)|Ciao|ciao|(?:(see you|See you)(?:[ ]?)(tomorrow|later|soon)?))")
    
    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
        yield "goodbye", span.start, span.end
```
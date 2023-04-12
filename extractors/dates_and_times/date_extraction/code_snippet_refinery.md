```python
import re

#currently only english language is supported here
#reach out to us if this should be extended for other languages

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "date"

def date_extraction(record):
    regex = re.compile(
        r"(?:[0-9]{1,2}|[0-9]{4}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )

    for match in regex.finditer(record[ATTRIBUTE].text):
        start, end = match.span()
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end
```
```python
import re

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "date"

def date_extractor(record):
    regex = re.compile(
        r"(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )

    for match in regex.finditer(record[YOUR_ATTRIBUTE].text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield YOUR_LABEL, span.start, span.end
```
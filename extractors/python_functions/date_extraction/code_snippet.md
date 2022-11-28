```python
import re

YOUR_ATTRIBUTE = "your-text"

def date_extractor(record):
    regex = re.compile(
        r"(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.

    dates = []
    for match in regex.finditer(record[YOUR_ATTRIBUTE].text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        dates.append(["date", span.start, span.end])
```
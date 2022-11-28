```python
import re

YOUR_ATTRIBUTE = "your-text"

def ip_extractor(request):
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    regex.findall(text)

    text = request[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    ip_addresses = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = record[YOUR_ATTRIBUTE].char_span(start, end)
        yield "ip_address", span.start, span.end

    return {"ip_addresses": ip_addresses}
```
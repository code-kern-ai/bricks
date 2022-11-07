```python
from typing import Dict, Any, List, Tuple

def email_extractor(record: Dict[str, Any]) -> List[Tuple[str, int, int]]:
    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")

    emails = []
    for match in regex.finditer(record["your-text"].text):
        start, end = match.span()
        span = record["your-text"].char_span(start, end)
        emails.append([span.start, span.end, span.text])
```
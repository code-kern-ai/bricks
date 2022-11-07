```python
from typing import Dict, Any
from pydantic import BaseModel
import re

def ip_extractor(request: Dict[str, Any]):
    text = request["text"]
    nlp = spacy.load(request["spacyTokenizer"])
    doc = nlp(text)
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    regex.findall(text)

    ip_addresses = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        ip_addresses.append([span.start, span.end, span.text])

    return {"ip_addresses": ip_addresses}
```
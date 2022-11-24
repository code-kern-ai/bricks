```python
import spacy
import re

def ip_extractor(request):
    text = request["text"]
    nlp = spacy.load(request["spacyTokenizer"])
    doc = nlp(text)
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    regex.findall(text)

    ip_addresses = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        ip_addresses.append(["ip_address", span.start, span.end])

    return {"ip_addresses": ip_addresses}
```
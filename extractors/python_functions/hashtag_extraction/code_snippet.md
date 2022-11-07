```python
from typing import Dict, Any
from extractors.util.spacy import SpacySingleton
import re

def hash_ext(record: Dict[str, Any]):
    text = record["text"]
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    regex = re.compile(r"#(\w+)")
    regex.findall(text)

    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"spans": spans}
```
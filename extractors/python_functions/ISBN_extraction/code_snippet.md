```python
from typing import Dict
import spacy
import re

def isbn_extractor() -> Dict:
    text = "I wish to have this book issued. It's ISBN number is 978-2-0074-4301-1."
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")

    isbn = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        isbn.append([span.start, span.end, span.text])

    return {"isbn": isbn}
```
```python
import re
from typing import Dict
import spacy

def isbn_ext(text: str = None) -> Dict:
    if text is None:
        text = "I wish to issue this book whose ISBN is 78-0-3563-82542-0. And also this one whose ISBN is 69-087-647-01."
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
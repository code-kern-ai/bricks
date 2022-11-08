```python
from typing import Dict
import spacy

def book_extraction(text: str = None) -> Dict:
    if text is None:
        text = "The book was called Mystery of the Floridian Porter."
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    books = []
    for entity in doc.ents:
        if entity.label_ == 'WORK_OF_ART':
            books.append((entity.start, entity.end, entity))

    return {"books": books}

```
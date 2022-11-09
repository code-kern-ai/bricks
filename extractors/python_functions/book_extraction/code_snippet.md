```python
from typing import Dict
import spacy

def book_extraction(record):
    for entity in record["your-text"].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield "book", entity.start, entity.end
```
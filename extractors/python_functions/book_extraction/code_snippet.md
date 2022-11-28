```python
import spacy

YOUR_ATTRIBUTE = "your-text"

def book_extraction(record):
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield "book", entity.start, entity.end
```
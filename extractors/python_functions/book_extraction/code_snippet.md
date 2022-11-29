```python
YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "book"

def book_extraction(record):
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield YOUR_LABEL, entity.start, entity.end
```
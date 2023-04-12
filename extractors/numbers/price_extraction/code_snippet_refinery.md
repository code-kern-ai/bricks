```python
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "price"

def price_extraction(record):
    doc = record[ATTRIBUTE] # SpaCy doc

    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            yield LABEL, entity.start, entity.end
```
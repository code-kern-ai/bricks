```python
YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "price"

def price_extractor(record):
    text = record[YOUR_ATTRIBUTE]

    for entity in text.ents:
        if entity.label_ == 'MONEY':
            yield YOUR_LABEL, entity.start, entity.end
```
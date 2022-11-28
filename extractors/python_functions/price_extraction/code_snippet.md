```python
YOUR_ATTRIBUTE = "your-text"

def price_extractor(record):
    text = record[YOUR_ATTRIBUTE]

    for entity in text.ents:
        if entity.label_ == 'MONEY':
            yield "price", entity.start, entity.end
```
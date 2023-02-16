```python
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "price"

def price_extraction(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    doc = record[YOUR_ATTRIBUTE] # SpaCy doc

    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            yield YOUR_LABEL, entity.start, entity.end
```
```python
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "name"

def person_extraction(record):
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == "PERSON":
            yield YOUR_LABEL, entity.start, entity.end
```
```python
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "name"

def person_extraction(record):
    for entity in record[ATTRIBUTE].ents:
        if entity.label_ == "PERSON":
            yield LABEL, entity.start, entity.end
```
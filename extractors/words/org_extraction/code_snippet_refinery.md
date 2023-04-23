```python
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "ORG"

def org_extraction(record):
    for entity in record[ATTRIBUTE].ents:
        if entity.label_ == "ORG":
            yield LABEL, entity.start, entity.end
```
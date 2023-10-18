```python
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "location"

def location_extraction(record):
    for ent in record[ATTRIBUTE].ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            yield LABEL, ent.start, ent.end
```
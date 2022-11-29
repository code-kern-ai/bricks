```python
YOUR_ATTRIBUTE: str = "text" # Choose any available attribute here
YOUR_LABEL: str = "ORG"

def org_extraction(record):
    
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == "ORG":
            yield YOUR_LABEL, entity.start, entity.end
```
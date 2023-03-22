```python
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "work of art"

def work_of_art_extraction(record):
    for entity in record[YOUR_ATTRIBUTE].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield YOUR_LABEL, entity.start, entity.end
```
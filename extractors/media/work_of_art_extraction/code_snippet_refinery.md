```python
ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "work of art"

def work_of_art_extraction(record):
    for entity in record[ATTRIBUTE].ents:
        if entity.label_ == 'WORK_OF_ART':
            yield LABEL, entity.start, entity.end
```
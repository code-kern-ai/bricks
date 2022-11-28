```python
YOUR_ATTRIBUTE = "your-text" # Choose any available attribute here

def name_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    for entity in record[YOUR_ATRRIBUTE].ents:
        if entity.label_ == "PERSON":
            yield "person", entity.start, entity.end
```
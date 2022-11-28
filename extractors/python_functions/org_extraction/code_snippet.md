```python
YOUR_ATTRIBUTE = "your-text" # Choose any available attribute here

def org_extraction(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to extract the text.
    for entity in doc.ents:
        if entity.label_ == "ORG":
            yield "org", entity.start, entity.end
```
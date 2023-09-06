```python
ATTRIBUTE: str = "text" # only text attributes

def reading_time(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    return len(text)
```
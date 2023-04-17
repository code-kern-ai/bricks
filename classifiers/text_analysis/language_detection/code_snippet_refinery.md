```python
from langdetect import detect

ATTRIBUTE: str = "text" #only text attributes

def language_detection(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    return detect(text) # e.g. "en"
```
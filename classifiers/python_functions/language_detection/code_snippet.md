```python
from langdetect import detect

YOUR_ATTRIBUTE = "text"

def language_detection(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    language = detect(text)
    return language # e.g. "en"
```
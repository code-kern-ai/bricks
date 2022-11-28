```python
from langdetect import detect

YOUR_ATTRIBUTE = "text"

def language_detection(record):
    text = record[YOUR_ATTRIBUTE].text
    language = detect(text)
    return language # e.g. "en"
```
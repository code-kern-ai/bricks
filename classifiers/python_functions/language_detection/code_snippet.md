```python
from langdetect import detect

YOUR_ATTRIBUTE: str = "text" #only text attributes

def language_detection(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    language = detect(text)
    return language # e.g. "en"
```
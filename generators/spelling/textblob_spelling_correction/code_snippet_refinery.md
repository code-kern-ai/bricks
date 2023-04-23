```python
from textblob import TextBlob

ATTRIBUTE: str = "text" # only text attributes

def textblob_spelling_correction(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
    textblob_text = TextBlob(text)
    return str(textblob_text.correct())
```
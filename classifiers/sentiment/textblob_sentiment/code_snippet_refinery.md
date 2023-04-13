```python
from textblob import TextBlob

ATTRIBUTE: str = "text" # only text attributes

def textblob_sentiment(record):
    blob = TextBlob(record[ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return lookup_label(blob.sentiment.polarity)

def lookup_label(score:float) -> str:
    if score < -.6:
        return "very negative"
    if score < -.2:
        return "negative"
    if score < .2:
        return "neutral"
    if score < .6:
        return "positive"
    return "very positive"
```
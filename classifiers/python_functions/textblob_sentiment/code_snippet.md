```python
from textblob import TextBlob
from typing import Dict

YOUR_ATTRIBUTE: str = "text"

def setall(d, keys, value):
    for k in keys:
        d[k] = value

MAX_SCORE: int = 100
MIN_SCORE: int = -100

OUTCOMES: Dict = {}
setall(OUTCOMES, range(60, MAX_SCORE + 1), "very positive")
setall(OUTCOMES, range(20, 60), "positive")
setall(OUTCOMES, range(-20, 20), "neutral")
setall(OUTCOMES, range(-60, -20), "negative")
setall(OUTCOMES, range(MIN_SCORE, -60), "very negative")

def get_mapping_sentiment(score):
    if score < MIN_SCORE:
        return OUTCOMES[MIN_SCORE]
    return OUTCOMES[int(score)]

def textblob_sentiment(record):
    blob = TextBlob(record[YOUR_ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return get_mapping_sentiment(blob.sentiment.polarity * 100)
```
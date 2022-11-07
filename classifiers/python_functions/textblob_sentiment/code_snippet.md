```python
from textblob import TextBlob

def setall(d, keys, value):
    for k in keys:
        d[k] = value

MAX_SCORE = 100
MIN_SCORE = -100

OUTCOMES = {}
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
    blob = TextBlob(record["your-text"])
    return get_mapping_sentiment(blob.sentiment.polarity * 100)
```
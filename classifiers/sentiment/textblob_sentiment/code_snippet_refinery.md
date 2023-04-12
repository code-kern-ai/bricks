```python
# expects labeling task to have labels ["very positive", "positive" ,"neutral", "negative", "very negative"]
from textblob import TextBlob

ATTRIBUTE: str = "text" # only text attributes
MAX_SCORE: int = 100
MIN_SCORE: int = -100

def textblob_sentiment(record):
    blob = TextBlob(record[ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return get_mapping_sentiment(blob.sentiment.polarity * 100)


def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_sentiment(score):
    if score < MIN_SCORE:
        return outcomes[MIN_SCORE]
    if score > MAX_SCORE:
        return outcomes[MAX_SCORE]
    return outcomes[int(score)]

outcomes = {}
set_all(outcomes, range(60, MAX_SCORE + 1), "very positive")
set_all(outcomes, range(20, 60), "positive")
set_all(outcomes, range(-20, 20), "neutral")
set_all(outcomes, range(-60, -20), "negative")
set_all(outcomes, range(MIN_SCORE, -60), "very negative")
```
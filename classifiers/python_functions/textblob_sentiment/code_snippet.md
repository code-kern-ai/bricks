```python
# expects labeling task to have labels ["very positive", "positive" ,"neutral", "negative", "very negative"]
from textblob import TextBlob

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_MAX_SCORE: int = 100
YOUR_MIN_SCORE: int = -100

def textblob_sentiment(record):
    blob = TextBlob(record[YOUR_ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return get_mapping_sentiment(blob.sentiment.polarity * 100)


def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_sentiment(score):
    if score < -100:
        return outcomes[-100]
    if score > 100:
        return outcomes[100]
    return outcomes[int(score)]

outcomes = {}
set_all(outcomes, range(60, 100 + 1), "very positive")
set_all(outcomes, range(20, 60), "positive")
set_all(outcomes, range(-20, 20), "neutral")
set_all(outcomes, range(-60, -20), "negative")
set_all(outcomes, range(-100, -60), "very negative")

```
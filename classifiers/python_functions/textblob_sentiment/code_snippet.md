```python
# expects labeling task to have labels ["very positive", "positive" ,"neutral", "negative", "very negative"]
from textblob import TextBlob
from typing import Dict

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
    if score < YOUR_MIN_SCORE:
        return outcomes[YOUR_MIN_SCORE]
    if score > YOUR_MAX_SCORE:
        return outcomes[YOUR_MAX_SCORE]
    return outcomes[int(score)]

outcomes: Dict = {}
set_all(outcomes, range(60, YOUR_MAX_SCORE + 1), "very positive")
set_all(outcomes, range(20, 60), "positive")
set_all(outcomes, range(-20, 20), "neutral")
set_all(outcomes, range(-60, -20), "negative")
set_all(outcomes, range(YOUR_MIN_SCORE, -60), "very negative")

```
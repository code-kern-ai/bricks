```python
# expects labeling task to have labels ["very positive", "positive" ,"neutral", "negative", "very negative"]
from textblob import TextBlob

record_dict = {
    "your_attribute": "Replace this with your text attribute
}

def textblob_sentiment(record):
    blob = TextBlob(record["your_attribute"])
    return get_mapping_sentiment(blob.sentiment.polarity * 100)


def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_sentiment(score):
    if score < 0:
        return outcomes[0]
    if score > 100:
        return outcomes[100]
    return outcomes[int(score)]

outcomes = {}
set_all(outcomes, range(60, YOUR_MAX_SCORE + 1), "very positive")
set_all(outcomes, range(20, 60), "positive")
set_all(outcomes, range(-20, 20), "neutral")
set_all(outcomes, range(-60, -20), "negative")
set_all(outcomes, range(YOUR_MIN_SCORE, -60), "very negative")

```
```python
# expects labeling task to have labels ["very positive", "positive" ,"neutral", "negative", "very negative"]
from textblob import TextBlob

# replace this list with a list containing your data
text = ["I hate this.", "Meh it's ok.", "I love this!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text
}

# main function
def textblob_sentiment(record: dict) -> dict:
    sentiments = []
    for entry in record["your_text"]:
        blob = TextBlob(entry)
        sentiments.append(get_mapping_sentiment(blob.sentiment.polarity * 100))
    return {"sentiments": sentiments}

# helper funtion to set the outcomes
def set_all(d, keys, value):
    for k in keys:
        d[k] = value

# helper function to map sentimens 
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
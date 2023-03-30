```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# replace this list with a list containing your data
text = ["I hate this.", "Meh it's ok.", "I love this!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "mode": "classification", # use "scores" to get a float output of the sentiment 
}

def vader_sentiment(record: dict) -> dict:
    analyzer = SentimentIntensityAnalyzer()

    sentiment = []
    for entry in record["your_text"]:
        vs = analyzer.polarity_scores(entry)
        if record["mode"] == "classification":
            if vs["compound"] >= 0.05:
                sentiment.append("positive")
            elif vs["compound"] > -0.05: 
                sentiment.append("neutral")
            elif vs["compound"] <= -0.05:
                sentiment.append("negative")
        elif record["mode"] == "scores": 
            sentiment.append(vs)
    return {"sentiments": sentiment}
```
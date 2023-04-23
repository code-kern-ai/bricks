```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# replace this list with a list containing your data
text = ["I hate this.", "Meh it's ok.", "I love this!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
}

def vader_sentiment_classifier(record: dict) -> dict:
    analyzer = SentimentIntensityAnalyzer()

    sentiment = []
    for entry in record["your_text"]:
        vs = analyzer.polarity_scores(entry)
        if vs["compound"] >= 0.05:
            sentiment.append("positive")
        elif vs["compound"] > -0.05: 
            sentiment.append("neutral")
        elif vs["compound"] <= -0.05:
            sentiment.append("negative")
    return {"sentiments": sentiment}
```
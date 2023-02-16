```python
from vaderSentiment import SentimentIntensityAnalyzer

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_MODE: str = "classification" # choose "scores" to only get the sentiment scores as floats

def vader_sentiment(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    analyzer = SentimentIntensityAnalyzer()
    text = record[YOUR_ATTRIBUTE].text

    vs = analyzer.polarity_scores(text)
    if YOUR_MODE == "classification":
        if vs["compound"] >= 0.05:
            return {"sentiment": "positive"}
        elif vs["compound"] > -0.05: 
            return {"sentiment": "neutral"}
        elif vs["compound"] <= -0.05:
            return {"sentiment": "negative"}
    elif YOUR_MODE == "scores": 
        return {"sentiment_scores": vs}

```
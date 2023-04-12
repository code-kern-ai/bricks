```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

ATTRIBUTE: str = "text" # only text attributes
MODE: str = "classification" # choose "scores" to only get the sentiment scores as floats

def vader_sentiment(record):
    analyzer = SentimentIntensityAnalyzer()
    text = record[ATTRIBUTE].text

    vs = analyzer.polarity_scores(text)
    if MODE == "classification":
        if vs["compound"] >= 0.05:
            return "positive"
        elif vs["compound"] > -0.05: 
            return "neutral"
        elif vs["compound"] <= -0.05:
            return "negative"
    elif MODE == "scores": 
        return vs
```
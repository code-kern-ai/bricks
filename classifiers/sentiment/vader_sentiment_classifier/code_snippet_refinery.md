```python
# expects labeling task to have labels ["positive" ,"neutral", "negative"]
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

ATTRIBUTE: str = "headline" # only text attributes

def vader_sentiment_classifier(record):
    analyzer = SentimentIntensityAnalyzer()
    text = record[ATTRIBUTE].text

    vs = analyzer.polarity_scores(text)
    if vs["compound"] >= 0.05:
        return "positive"
    elif vs["compound"] > -0.05: 
        return "neutral"
    elif vs["compound"] <= -0.05:
        return "negative"
```
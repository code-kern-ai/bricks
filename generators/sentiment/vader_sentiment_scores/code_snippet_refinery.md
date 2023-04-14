```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

ATTRIBUTE: str = "text" # only text attributes

def vader_sentiment_scores(record):
    analyzer = SentimentIntensityAnalyzer()
    text = record[ATTRIBUTE].text

    vs = analyzer.polarity_scores(text)
    return json.dumps(vs)
```
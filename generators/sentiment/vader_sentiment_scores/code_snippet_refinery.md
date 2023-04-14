```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

ATTRIBUTE: str = "text" # only text attributes

def vader_sentiment_scores(record):
    analyzer = SentimentIntensityAnalyzer()
    return json.dumps(analyzer.polarity_scores(record[ATTRIBUTE].text))
```
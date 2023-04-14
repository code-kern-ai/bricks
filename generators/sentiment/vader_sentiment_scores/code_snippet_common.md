```python
from typing import Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader_sentiment_scores(text: str) -> Dict[str, float]:
    """ Vader sentiment scores for text
    @param text: The text to analyze.results.
    @return: Dict of scores (neg, neu, pos, compound)
    """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["I hate this.", "Meh it's ok.", "I love this!"]
    
    for text in texts:
        print(f"The sentiment sores of {text} are: {vader_sentiment_scores(text)}")
example_integration() 
```
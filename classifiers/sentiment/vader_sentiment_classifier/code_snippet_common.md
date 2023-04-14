```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader_sentiment_classifier(text: str) -> str:    
    """
    @param text: text you want to analyze
    @return: either 'negative', 'neutral' or 'positive' depending on the score
    """
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    return lookup_label(vs["compound"])

def lookup_label(score:float) -> str:
    if score <= -0.05:
        return "negative"
    if score < 0.05:
        return "neutral"
    return "positive"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["I hate this!","This is a negative example.","I don't know how this is.", "This is a fine example.", "I love this!"]
    for text in texts:
        print(f"the sentiment of \"{text}\" is \"{vader_sentiment_classifier(text)}\"")

example_integration()
```
```python
from textblob import TextBlob

def textblob_sentiment(text: str) -> str:
    """
    @param text: text you want to analyze
    @return: either 'very negative', 'negative', 'neutral', 'positive' or 'very positive' depending on the score
    """
    blob = TextBlob(text)
    return lookup_label(blob.sentiment.polarity)

def lookup_label(score:float) -> str:
    if score < -.6:
        return "very negative"
    if score < -.2:
        return "negative"
    if score < .2:
        return "neutral"
    if score < .6:
        return "positive"
    return "very positive"


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["I hate this!","This is a negative example.","I don't know how this is.", "This is a fine example.", "I love this!"]
    for text in texts:
        print(f"the sentiment of \"{text}\" is \"{textblob_sentiment(text)}\"")

example_integration()

```
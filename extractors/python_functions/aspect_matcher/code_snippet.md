```python
from textblob import TextBlob

YOUR_ATTRIBUTE: str = "details"
YOUR_WINDOW: int = 4 # choose any window size here
YOUR_SENSITIVITY: float = 0.5 # choose any value between 0 and 1
NEGATIVE_LABEL: str = "negative"
POSITIVE_LABEL: str = "positive"

def aspect_matcher(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (YOUR_WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (YOUR_WINDOW // 2) + 1)
        window_doc = record[YOUR_ATTRIBUTE][left_bound: right_bound]
        sentiment = TextBlob(window_doc.text).polarity
        if sentiment < -(1 - YOUR_SENSITIVITY):
            yield NEGATIVE_LABEL, chunk.start, chunk.end
        elif sentiment > (1 - YOUR_SENSITIVITY):
            yield POSITIVE_LABEL, chunk.start, chunk.end
```
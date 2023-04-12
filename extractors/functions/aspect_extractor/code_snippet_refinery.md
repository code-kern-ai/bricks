```python
from textblob import TextBlob

ATTRIBUTE: str = "details" # only text attributes
WINDOW: int = 4 # choose any window size here
SENSITIVITY: float = 0.5 # choose any value between 0 and 1
NEGATIVE_LABEL: str = "negative"
POSITIVE_LABEL: str = "positive"

def aspect_extraction(record):
    for chunk in record[ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (WINDOW // 2) + 1)
        window_doc = record[ATTRIBUTE][left_bound: right_bound]
        sentiment = TextBlob(window_doc.text).polarity
        if sentiment < -(1 - SENSITIVITY):
            yield NEGATIVE_LABEL, chunk.start, chunk.end
        elif sentiment > (1 - SENSITIVITY):
            yield POSITIVE_LABEL, chunk.start, chunk.end
```
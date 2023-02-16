```python
from textblob import TextBlob

YOUR_ATTRIBUTE: str = "details" # only text attributes
YOUR_WINDOW: int = 4 # choose any window size here
YOUR_SENSITIVITY: float = 0.5 # choose any value between 0 and 1
YOUR_NEGATIVE_LABEL: str = "negative"
YOUR_POSITIVE_LABEL: str = "positive"

def aspect_extraction(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (YOUR_WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (YOUR_WINDOW // 2) + 1)
        window_doc = record[YOUR_ATTRIBUTE][left_bound: right_bound]
        sentiment = TextBlob(window_doc.text).polarity
        if sentiment < -(1 - YOUR_SENSITIVITY):
            yield YOUR_NEGATIVE_LABEL, chunk.start, chunk.end
        elif sentiment > (1 - YOUR_SENSITIVITY):
            yield YOUR_POSITIVE_LABEL, chunk.start, chunk.end
```
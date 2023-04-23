```python
from textblob import TextBlob
import spacy

# replace this list with a list containing your data
text = ["It has a really great battery life, but I hate the window size...", "I love the screen size, but the battery life is terrible..."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "window": 4,
    "sensitivity": 0.5,
    "negative_label": "negative",
    "positive_label": "positive"
}

def aspect_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    window_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for chunk in doc.noun_chunks:
            left_bound = max(chunk.sent.start, chunk.start - (record["window"] // 2) +1)
            right_bound = min(chunk.sent.end, chunk.end + (record["window"] // 2) + 1)
            window_doc = doc[left_bound: right_bound]
            sentiment = TextBlob(window_doc.text).polarity
            if sentiment < -(1 - record["sensitivity"]):
                window_positions.append({f"text_{text_id}": [record["negative_label"], chunk.start, chunk.end]})
            elif sentiment > (1 - record["sensitivity"]):
                window_positions.append({f"text_{text_id}": [record["positive_label"], chunk.start, chunk.end]})
        text_id += 1
    return {"extractions": window_positions}
```
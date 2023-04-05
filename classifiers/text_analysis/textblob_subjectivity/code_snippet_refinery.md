```python
# expects labeling task to have labels ["subjective", "rather subjective" ,"neutral", "rather objective", "objective"]
from textblob import TextBlob

YOUR_ATTRIBUTE: str = "text" # only text attributes

def textblob_subjectivity(record):    
    blob = TextBlob(record[YOUR_ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return get_mapping_subjectivity(blob.sentiment.subjectivity * 100)

def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_subjectivity(score):
    if score < 0:
        return outcomes[0]
    if score > 100:
        return outcomes[100]
    return outcomes[int(score)]


outcomes = {}
set_all(outcomes, range(80, 100 + 1), "subjective")
set_all(outcomes, range(60, 80), "rather subjective")
set_all(outcomes, range(40, 60), "neutral")
set_all(outcomes, range(20, 40), "rather objective")
set_all(outcomes, range(0, 20), "objective")
```
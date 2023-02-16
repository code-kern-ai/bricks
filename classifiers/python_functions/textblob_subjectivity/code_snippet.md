```python
# expects labeling task to have labels ["subjective", "rather subjective" ,"neutral", "rather objective", "objective"]
from textblob import TextBlob


YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_MAX_SCORE: int = 100
YOUR_MIN_SCORE: int = 0

def textblob_subjectivity(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    blob = TextBlob(record[YOUR_ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return get_mapping_subjectivity(blob.sentiment.subjectivity * 100)

def set_all(d, keys, value):
    for k in keys:
        d[k] = value

def get_mapping_subjectivity(score):
    if score < YOUR_MIN_SCORE:
        return outcomes[YOUR_MIN_SCORE]
    if score > YOUR_MAX_SCORE:
        return outcomes[YOUR_MAX_SCORE]
    return outcomes[int(score)]


outcomes = {}
set_all(outcomes, range(80, YOUR_MAX_SCORE + 1), "subjective")
set_all(outcomes, range(60, 80), "rather subjective")
set_all(outcomes, range(40, 60), "neutral")
set_all(outcomes, range(20, 40), "rather objective")
set_all(outcomes, range(YOUR_MIN_SCORE, 20), "objective")
```
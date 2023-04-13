```python
from textblob import TextBlob

ATTRIBUTE: str = "text" # only text attributes

def textblob_subjectivity(record):    
    blob = TextBlob(record[ATTRIBUTE].text) # SpaCy document, hence we need to call .text to get the string
    return lookup_label(blob.sentiment.subjectivity)

def lookup_label(score:float) -> str:
    if score < .2:
        return "objective"
    if score < .4:
        return "rather objective"
    if score < .6:
        return "neutral"
    if score < .8:
        return "rather subjective"     
    return "subjective"

```
```python
#expects labeling task to have labels ["anger", "fear", "anticipation", "trust", "surprise", "sadness", "joy", "disgust"]
from LeXmo import LeXmo

ATTRIBUTE: str = "text" # only text attributes

def emotionality_detection(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    emo = LeXmo.LeXmo(text)
    del emo["text"]
    del emo["positive"]
    del emo["negative"]
    emo = max(emo, key=emo.get)

    return emo 
```
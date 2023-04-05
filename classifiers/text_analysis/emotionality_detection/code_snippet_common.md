```python
# expects labeling task to have labels ["anger", "fear", "anticipation", "trust", "surprise", "sadness", "joy", "disgust"]
from LeXmo import LeXmo

# replace this list with a list containing your data
text = ["I really don't want to do it I am scared.", "Oh my goodness it was the best evening ever, hype!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
}

def emotionality_detection(record):
    emotions = []
    for entry in record["your_text"]:
        emo = LeXmo.LeXmo(entry)
        emo.pop("text", None)
        emo = max(emo, key=emo.get)
        emotions.append(emo)
    return {"emotions": emotions} 
```
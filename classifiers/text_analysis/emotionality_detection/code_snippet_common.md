```python
from LeXmo import LeXmo

def emotionality_detection(text:str) -> str:
    """
    @param text: text to check
    @return: either 'anger', 'fear', 'anticipation', 'trust', 'surprise', 'sadness', 'joy' or 'disgust' depending on the score
    """
    emo = LeXmo.LeXmo(text)
    del emo["text"]
    del emo["positive"]
    del emo["negative"]
    emo = max(emo, key=emo.get)
    return emo
    
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["I am scared to continue.", "Oh my goodness it was the best evening ever, hype!"]
    for text in texts:
        print(f"\"{text}\" has emotion: {emotionality_detection(text)}")

example_integration()
```
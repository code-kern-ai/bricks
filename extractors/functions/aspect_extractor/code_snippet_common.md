```python
from typing import List, Tuple
from textblob import TextBlob
import spacy

def aspect_extraction(text:str, window:int, sensitivity:float, positive_label:str, negative_label:str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    window_positions = []        
    for chunk in doc.noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (window // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (window // 2) + 1)
        window_doc = doc[left_bound: right_bound]
        sentiment = TextBlob(window_doc.text).polarity
        if sentiment < -(1 - sensitivity):
            window_positions.append((negative_label, chunk.start, chunk.end))
        elif sentiment > (1 - sensitivity):
            window_positions.append((positive_label, chunk.start, chunk.end))
    return window_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["It has a really great battery life, but I hate the window size...", "I love the screen size, but the battery life is terrible...", "Tasty pancake recipe"]
    window = 4
    sensitivity = 0.5
    positive_label = "negative"
    negative_label = "positive"
    for text in texts:
        found = aspect_extraction(text, window, sensitivity, positive_label, negative_label)
        if found:
            print(f"text: \"{text}\" has {found[0][0]} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {positive_label} or {negative_label}")

example_integration()
```
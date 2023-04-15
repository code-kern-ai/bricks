```python
from textblob import TextBlob

def textblob_subjectivity(text:str): 
    """
    @param text: text to check
    @return: either 'very difficult', 'difficult', 'fairly difficult', 'standard', 'fairly easy', 'easy' or 'very easy' depending on the score
    """
    blob = TextBlob(text) 
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

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["These are the worst fries every.", "Trees are made of wood."]
    for text in texts:
        print(f"\"{text}\" is {textblob_subjectivity(text)}")

example_integration()
```
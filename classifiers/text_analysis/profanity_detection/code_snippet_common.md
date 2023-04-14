```python
from better_profanity import profanity

def profanity_detection(text:str,return_label_profane:str,return_label_not_profane:str) -> str:    
    """
    @param text: text to check
    @param return_label_profane: label to return if the text contains profanity
    @param return_label_not_profane: label to return if the text does not contains profanity
    @return: either return_label_profane or return_label_not_profane
    """
    if profanity.contains_profanity(text):
        return return_label_profane
    else:
        return return_label_not_profane

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["You suck man!.", "Thanks have a nice day."]
    label_profane= "profanity"
    label_not_profane= "no profanity"
    for text in texts:
        print(f"\"{text}\" contains {profanity_detection(text,label_profane,label_not_profane)}")

example_integration()
```
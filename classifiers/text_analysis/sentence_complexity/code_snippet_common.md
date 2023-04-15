```python
import textstat

def sentence_complexity(text:str)->str:    
    """
    @param text: text to check
    @return: either 'very difficult', 'difficult', 'fairly difficult', 'standard', 'fairly easy', 'easy' or 'very easy' depending on the score
    """
    return lookup_label(textstat.flesch_reading_ease(text))

def lookup_label(score:int) -> str:
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Doctors from Stockhold University invent cure for rare disease.", "Mary had a little lamb."]
    target_language = "en"
    textstat.set_lang("en") #en, de, es, fr, it, nl, ru
    for text in texts:
        print(f"\"{text}\" is {sentence_complexity(text)}")

example_integration()
```
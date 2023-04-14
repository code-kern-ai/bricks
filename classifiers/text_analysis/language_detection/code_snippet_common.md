```python
from langdetect import detect

def language_detection(text:str)->str:    
    """
    @param text: text to check
    @return: language iso code. Full list here https://github.com/Mimino666/langdetect#languages
    """
    return detect(text)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["This is an english sentence.", "Dies ist ein Text in Deutsch."]
    for text in texts:
        print(f"\"{text}\" is written in {language_detection(text)}")

example_integration()
```
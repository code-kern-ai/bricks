```python
import textstat

def reading_time(text:str)->float:
    """ 
    @param text: text we check the reading time for
    @return: reading time in seconds
    """
    return textstat.reading_time(text, ms_per_char=14.69)
    
# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

    for text in texts:
        print(f"the text \"{text}\" will take around {reading_time(text)} sec")
example_integration() 
```
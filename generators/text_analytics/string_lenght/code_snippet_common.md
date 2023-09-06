```python

def string_lenght(text:str)->int:
    """ 
    @param text: text we check the lenght for
    @return: lenght of the text
    """
    return len(text)
    
# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

    for text in texts:
        print(f"the text \"{text}\" has a lenght of {string_lenght(text)} characters.")
example_integration() 
```
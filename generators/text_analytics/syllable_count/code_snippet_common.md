```python
import textstat

def syllable_count(text: str) -> int:
    return textstat.syllable_count(text)

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for text in texts:
        print(f"the text \"{text}\" has {syllable_count(text)} syllables")
example_integration() 
```
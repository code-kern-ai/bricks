```python
from textblob import TextBlob

def textblob_spelling_correction(text: str) -> str:
    """
    @param text: text to correct
    @return: corrected text
    """
    textblob_text = TextBlob(text)
    return str(textblob_text.correct())

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This text contaisn some speling errors."]

    for text in texts:
        print(f"the corrected version of \"{text}\" is: {textblob_spelling_correction(text)}")
example_integration() 

```
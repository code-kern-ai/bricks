```python
from translate import Translator

def language_translator(text: str,original_language:str,target_language:str) -> str:
    """ 
    @param text: text we want to translate
    @param original_language: only iso format
    @param target_language: only iso format
    @return: translated text
    """
    translator = Translator(from_lang=original_language, to_lang=target_language)
    return translator.translate(text)

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    original_language = "en"
    target_language = "de"
    for text in texts:
        print(f"the text \"{text}\" in {target_language} is {language_translator(text,original_language,target_language)}")
example_integration() 
```
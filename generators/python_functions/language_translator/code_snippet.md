```python
from translate import Translator

YOUR_ATTRIBUTE: str = "text" #only text attributes
YOUR_ORIGINAL_LANGUAGE: str = "en" #only iso format
YOUR_TARGET_LANGUAGE: str = "de" #only iso format

def language_translator(record) -> str:

    string_to_translate = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    translator = Translator(from_lang=YOUR_ORIGINAL_LANGUAGE, to_lang=YOUR_TARGET_LANGUAGE)
    translation = translator.translate(string_to_translate)
    return translation
```

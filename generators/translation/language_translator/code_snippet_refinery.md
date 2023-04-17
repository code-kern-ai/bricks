```python
from translate import Translator

ATTRIBUTE: str = "text" #only text attributes
ORIGINAL_LANGUAGE: str = "en" #only iso format
TARGET_LANGUAGE: str = "de" #only iso format

def language_translator(record):

    string_to_translate = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get string.

    translator = Translator(from_lang=ORIGINAL_LANGUAGE, to_lang=TARGET_LANGUAGE)
    translation = translator.translate(string_to_translate)
    return translation
```

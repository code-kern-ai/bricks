```python
from translate import Translator

YOUR_ATTRIBUTE = "text"

def language_translator(record):

    origin_lang = "en"
    target_lang = "de" 
    string_to_translate = record[YOUR_ATTRIBUTE].text

    translator = Translator(from_lang=origin_lang, to_lang=target_lang)
    translation = translator.translate(string_to_translate)
    yield translation
```
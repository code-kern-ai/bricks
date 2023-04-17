```python
from translate import Translator

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "origin_language": "en", # change this to the language of your texts
    "target_language": "de" # change this to the language you want to translate to
}

def language_translator(record: dict) -> dict:
    translations = []
    for entry in record["your_text"]:     
        translator = Translator(from_lang=record["origin_language"], to_lang=record["target_language"])
        translation = translator.translate(entry)
        translations.append(translation)
    return {"translations": translations}
```
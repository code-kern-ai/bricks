```python
from langdetect import detect

# replace this list with a list containing your data
text = ["This is an english sentence.", "Dies ist ein Text in Deutsch."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def language_detection(record):
    detected_languages = []
    for entry in record["text"]:
        language = detect(entry)
        detected_languages.append(language)
    return {"detected_languages": detected_languages}
```
```python
from textblob import TextBlob

# replace this list with a list containing your data
text = ["His text contaisn some speling errors."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def textblob_spelling_correction(record):
    corrected_texts = []
    for entry in record["text"]:
        textblob_text = TextBlob(entry)
        corrected_texts.append(str(textblob_text.correct()))
    return {"correctedText": corrected_texts}
```
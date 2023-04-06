```python
import textstat

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def syllable_count(record):
    syllable_list = []
    for entry in record["text"]:
        syllable_list.append(textstat.syllable_count(entry))
    return {"syllables": syllable_list}
```
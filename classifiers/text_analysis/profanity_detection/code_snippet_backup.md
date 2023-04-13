```python
from better_profanity import profanity

# replace this list with a list containing your data
text = ["You suck man!.", "Thanks have a nice day."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label_profane": "profane",
    "label_not_profane": "not_profane",
}

def profanity_detection(record):
    detected_profanity = []
    for entry in record["text"]:
        if profanity.contains_profanity(entry):
            detected_profanity.append(record["label_profane"])
        else:
            detected_profanity.append(record["label_not_profane"])
    return {"profanity": detected_profanity}
```
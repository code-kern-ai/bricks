```python
import spacy

# replace this list with a list containing your data
text = ["My name is James Bond.", "Harry met Jane on a sunny afternoon."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "label": "name",
}

def person_extraction(record: dict) -> dict:
    nlp = spacy.load("en_core_web_sm")

    name_positions = []
    text_id = 0
    for entity in record["your_text"]:
        doc = nlp(entity)
        if entity.label_ == "PERSON":
            name_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return name_positions
```
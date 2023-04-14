```python
import spacy 

# replace this list with a list containing your data
text = ["Search of Lost Time is a great book by Marcel Proust."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "work of art",
}

def work_of_art_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    artwork_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for entity in doc.ents:
            if entity.label_ == 'WORK_OF_ART':
                artwork_positions.append({f"text_{text_id}" :[record["label"], entity.start, entity.end]})
        text_id += 1
    return {"extractions": artwork_positions}
```
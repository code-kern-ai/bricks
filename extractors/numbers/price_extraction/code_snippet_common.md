```python
import spacy 

# replace this list with a list containing your data
text = ["A desktop with i7 processor costs 950 dollars in the US."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "money",
}

def price_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    price_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for entity in doc.ents:
            if entity.label_ == "MONEY":
                price_positions.append({f"text_{text_id}" :[record["label"], entity.start, entity.end]})
        text_id += 1
    return {"extractions": price_positions}
```
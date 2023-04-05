```python
import spacy 

# replace this list with a list containing your data
text = ["We are developers from Kern.ai."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "org",
}

def org_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    org_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for entity in doc.ents:
            if entity.label_ == "ORG":
                org_positions.append({f"text_{text_id}" :[record["label"], entity.start, entity.end]})
        text_id += 1
    return {"extractions": org_positions}
```
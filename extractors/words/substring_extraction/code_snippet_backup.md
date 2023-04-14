```python
import spacy

# replace this list with a list containing your data
text = ["Italians eat a lot of pasta, often with tomatoes."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "substring",
    "substring": "Italians eat a lot of pasta"
}

def substring_extraction(record):
    nlp = spacy.load("en_core_web_sm")
    substring = record["substring"]

    substring_position = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)

        start_index = entry.find(substring)
        end_index = start_index + len(substring)

        if start_index != -1:
            span = doc.char_span(start_index, end_index, alignment_mode="expand")
            substring_position.append({f"text_{text_id}": [record["label"], span.start, span.end]}) 
        text_id += 1
    return {"extractions": substring_position}
```
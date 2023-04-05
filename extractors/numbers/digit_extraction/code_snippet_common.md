```python
import re
import spacy

# replace this list with a list containing your data
text = ["My PIN is 1337."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "digit",
    "digit_length": 4
}

def digit_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    digit_positions = []
    text_id = 0
    for entry in record["text"]:
        digit_length = record["digit_length"]

        num_string = "{"+f"{digit_length}"+"}"
        regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")
        
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            digit_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": digit_positions}
```
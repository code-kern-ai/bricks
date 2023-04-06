```python
import re
import spacy

# replace this list with a list containing your data
text = ["My IBAN is DE89370400440532013000."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "iban",
}

def iban_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    iban_positions = []
    text_id = 0
    for entry in record["text"]:
        regex = re.compile(r"[A-Z]{2}\d{2} ?\d{4} ?\d{4} ?\d{4} ?\d{4} ?[\d]{0,2}")
        
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            iban_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": iban_positions}
```
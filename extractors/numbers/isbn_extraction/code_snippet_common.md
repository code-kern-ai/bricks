```python
import re
import spacy

# replace this list with a list containing your data
text = ["I wish to issue this book whose ISBN is 78-0-3563-82542-0.", "lso this one whose ISBN is 69-087-647-01."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "isbn",
}

def isbn_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    isbn_positions = []
    text_id = 0
    for entry in record["text"]:
        regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")
        
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            isbn_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": isbn_positions}
```
```python
import re
import spacy

# replace this list with a list containing your data
text = ["The IP addressing range is from 0.0.0.0 to 255.255.255.255."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "IP-address",
}

def ip_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    ip_positions = []
    text_id = 0
    for entry in record["text"]:
        regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
        
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            ip_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": ip_positions}
```
```python
import re
import spacy

# replace this list with a list containing your data
text = ["My E-Mail address is jane.doe@gmail.com", "Our support mail is support@awesome-co.com"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "label": "email",
}

def email_extraction(record: dict) -> dict:
    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")
    nlp = spacy.load("en_core_web_sm")

    email_positions = []
    text_id = 0
    for entry in record["your_text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            email_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return email_positions
```
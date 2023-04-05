```python
import re
import spacy
import phonenumbers

# replace this list with a list containing your data
text = ["So here's my number +442083661177. Call me maybe!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "phone_num",
}

def phone_number_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    phone_positions = []
    text_id = 0
    for entry in record["text"]:
        regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
        doc = nlp(entry)
        for match in regex.finditer(entry):
            parsed_num = phonenumbers.parse(match.group(0), None)
            if phonenumbers.is_valid_number(parsed_num):
                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
                phone_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": phone_positions}
```
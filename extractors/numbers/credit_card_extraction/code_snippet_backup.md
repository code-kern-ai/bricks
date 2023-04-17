```python
import re
import spacy 

# replace this list with a list containing your data
text = ["This is my card details please use it carefully 4569-4039-6101-4710.", "The card number is 1231 4551 3431 1009."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "credit card",
}

def credit_card_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    credit_card_positions = []
    text_id = 0
    for entry in record["text"]:
        regex = re.compile(
            r"(\d{4}[-\s]?){3}\d{3,4}"
        )
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            credit_card_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return credit_card_positions
```
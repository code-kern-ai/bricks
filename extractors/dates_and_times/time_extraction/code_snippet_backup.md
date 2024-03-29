```python
import re
import spacy

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "time"

# replace this list with a list containing your data
text = ["Right now it is 14:40:37.", "Three hours ago it was 11:40 am. Two hours and twenty mins from now it will be 5PM.",]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "time",
}

def time_extraction(record):
    regex = re.compile(
        r"\b(1[0-2]|[1-9])\s*[apAP][. ]*[mM]\.?|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?(?:(?:\s?[ap](?:\.m\.)?)|(?:\s?[AP](?:\.M\.)?)))|(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?"
    )
    nlp = spacy.load("en_core_web_sm")

    time_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            time_positions.append({f"text_{text_id}": [LABEL, span.start, span.end]})
        text_id += 1
    return {"extractions": time_positions}
```
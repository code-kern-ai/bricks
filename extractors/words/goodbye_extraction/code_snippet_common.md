```python
import re
import spacy

# replace this list with a list containing your data
text = ["I will leave for now since I have to cook dinner. Goodbye, and ciao to you as well!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "goodbye",
}

def goodbye_extraction(record: dict) -> dict:
    regex = re.compile(r"((?:((?i)good)(?:[ ])?)?((?i)bye)|(?i)Ciao|(?:((?i)see you)(?:[ ]?)((?i)tomorrow|later|soon)?))")
    nlp = spacy.load("en_core_web_sm")

    goodbye_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            goodbye_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": goodbye_positions}
```
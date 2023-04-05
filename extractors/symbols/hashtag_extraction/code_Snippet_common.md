```python
import re
import spacy

# replace this list with a list containing your data
text = ["In tech industry, #devrel is a very hot topic.", "Follow us on #mastodon!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "hashtag",
}

def hashtag_extraction(record):
    nlp = spacy.load("en_core_web_sm")
    regex = re.compile(r"#(\w*)")
    hashtag_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            hashtag_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]}) 
        text_id += 1
    return {"extractions": hashtag_positions}
```
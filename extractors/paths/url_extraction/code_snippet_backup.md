```python
import re
import spacy

# replace this list with a list containing your data
text = ["Check out https://kern.ai!"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "url",
}

def url_extraction(record):
    npl = spacy.load("en_core_web_sm")

    url_positions = []
    text_id = 0
    for entry in record["text"]:
        regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")
        doc = npl(entry)
        for match in regex_pattern.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            url_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]}) 
        text_id += 1
    return {"extractions" : url_positions}
```
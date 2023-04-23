```python
import spacy
import re

# replace this list with a list containing your data
text = ["My name is Jane.", "Look, it's John over there!"]
lookup_list = ["Jane", "John"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "lookup_list": lookup_list,
    "window": 4,
    "label": "person",  
}

def window_search_extraction(record):
    nlp = spacy.load("en_core_web_sm")

    windows_search_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for chunk in doc.noun_chunks:
            left_bound = max(chunk.sent.start, chunk.start - (record["window"] // 2) +1)
            right_bound = min(chunk.sent.end, chunk.end + (record["window"] // 2) + 1)
            window_doc = doc[left_bound: right_bound]
            if any([term in window_doc.text for term in record["lookup_list"]]):
                match = re.search(chunk.text, entry)
                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
                windows_search_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return {"extractions": windows_search_positions}
```
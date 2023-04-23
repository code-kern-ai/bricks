```python
import re
import spacy

# replace this list with a list containing your data
text = ["Check out https://kern.ai!", "Visit https://kern.ai for more information"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "url",
    "regex": r"https:\/\/[a-zA-Z0-9.\/]+"
}

def regex_extraction(record):

    def regex_search(pattern, string):
        prev_end = 0
        while True:
            match = re.search(pattern, string)
            if not match:
                break

            start_, end_ = match.span()
            yield start_ + prev_end, end_ + prev_end

            prev_end += end_
            string = string[end_:]
    nlp = spacy.load("en_core_web_sm")
        
    regex_extractions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for start, end in regex_search(record["regex"], entry):
            span = doc.char_span(start, end, alignment_mode="expand")
            regex_extractions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extractions": regex_extractions}
```
```python
import re
import spacy

# replace this list with a list containing your data
text = ["My favourite file is stored in: /usr/bin/myfavfiles/cats.png"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "path",
    "separator": "/"
}

def filepath_extraction(record):
    nlp = spacy.load("en_core_web_sm")
    sep = record["separator"]

    filepath_positions = []
    text_id = 0
    for entry in record["text"]:
        # Extracts the paths from the texts
        paths = [x for x in entry.split() if len(x.split(sep)) > 1]

        # We need to add an \ before separators to use them in regex
        regex_paths = [i.replace(sep, "\\" + sep) for i in paths]
        
        doc = nlp(entry)
        for path in regex_paths:
            pattern = rf"({path})"
            match = re.search(pattern, entry)

            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            
            filepath_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extractions" : filepath_positions}
```
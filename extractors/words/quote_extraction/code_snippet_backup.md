```python
import re
import spacy

# replace this list with a list containing your data
text = ['''"Hello, Nick," said Harry.
            "Hello, hello," said Nearly Headless Nick, starting and looking round. He wore a dashing, plumed hat on his long curly hair, and a tunic with a ruff, which concealed the fact that his neck was almost completely severed. He was pale as smoke, and Harry could see right through him to the dark sky and torrential rain outside.
            "You look troubled, young Potter," said Nick, folding a transparent letter as he spoke and tucking it inside his doublet.
            "So do you," said Harry.''']

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "quote",
}

def quote_extraction(record):
    regex = re.compile(r"\".*?\"|\'.*?\'")
    nlp = spacy.load("en_core_web_sm")

    quote_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            quote_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": quote_positions}
```
```python
# expects labelling task to have labels ["ADJ", "ADP", "ADV", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROP", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE"]
YOUR_ATTRIBUTE: str = "text" # only text attributes

def part_of_speech_extraction(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    doc = record[YOUR_ATTRIBUTE]

    for token in doc:
            pos = token.pos_
            if pos:
                yield pos, token.i, token.i+1
```
```python
# expects labelling task to have labels ["ADJ", "ADP", "ADV", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROP", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE"]
ATTRIBUTE: str = "text" # only text attributes

def part_of_speech_extraction(record):
    doc = record[ATTRIBUTE]
    for token in doc:
            pos = token.pos_
            if pos:
                yield pos, token.i, token.i+1
```
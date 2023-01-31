```python
# expects labelling task to have labels ["ADJ", "ADP", "ADV", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROP", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE"]
YOUR_ATTRIBUTE: str = "text" # only text attributes

def part_of_speech_extractor(record):
    """Yields POS tags using spaCy."""

    doc = record[YOUR_ATTRIBUTE]

    for token in doc:
            pos = token.pos_
            if pos:
                yield pos, token.i, token.i+1
```
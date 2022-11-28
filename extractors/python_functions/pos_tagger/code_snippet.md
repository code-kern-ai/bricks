```python
import spacy
import re

YOUR_ATTRIBUTE = "headline" # Choose any available attribute here

def pos_tagger_leo(record):
    '''Yields POS tags using spaCy.'''

    doc = record[YOUR_ATTRIBUTE]

    for token in doc:
        text = token.text
        pos = token.pos_

        start, end = token.i, token.i +1
        span = doc.char_span(start, end, alignment_mode="expand")

        yield pos, span.start, span.end
```
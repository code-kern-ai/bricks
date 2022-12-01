```python
YOUR_ATTRIBUTE: str = "text" # only text attributes

def pos_tagger(record):
    """Yields POS tags using spaCy."""

    doc = record[YOUR_ATTRIBUTE]

    for token in doc:
        pos = token.pos_

        start, end = token.i, token.i +1
        span = doc.char_span(start, end, alignment_mode="expand")

        yield pos, span.start, span.end
```
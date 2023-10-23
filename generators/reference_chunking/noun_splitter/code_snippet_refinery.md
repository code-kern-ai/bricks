```python
ATTRIBUTE: str = "text" # only text attributes

def noun_splitter(record):
    nouns_sents = set()
    for sent in record[ATTRIBUTE].sents:
        for token in sent:
            if token.pos_ == "NOUN" and len(token.text) > 1:
                nouns_sents.add(token.text)

    return list(nouns_sents)
```

```python
ATTRIBUTE: str = "text" # only text attributes

def noun_splitter(record):
    nouns_sents = []
    for sent in record[ATTRIBUTE].sents:
        nouns = [token.text for token in sent if token.pos_ == "NOUN" and len(token.text) > 1]
        if nouns:
            nouns_sents.extend([" ".join(nouns[i:i+1]) for i in range(0, len(nouns), 1)])
    return list(set(nouns_sents))
```
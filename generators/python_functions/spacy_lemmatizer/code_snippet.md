```python
YOUR_ATTRIBUTE: str = "text

def spacy_lemmatizer(record):
    return " ".join([token.lemma_ for token in record["headline"]])
```
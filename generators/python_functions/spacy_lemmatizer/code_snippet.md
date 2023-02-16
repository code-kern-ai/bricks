```python
YOUR_ATTRIBUTE: str = "text"

def spacy_lemmatizer(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    return " ".join([token.lemma_ for token in record[YOUR_ATTRIBUTE]])
```

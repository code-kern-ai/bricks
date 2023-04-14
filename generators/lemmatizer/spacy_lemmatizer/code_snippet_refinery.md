```python
ATTRIBUTE: str = "text"

def spacy_lemmatizer(record):
    final_text = ""
    for i, token in enumerate(record[ATTRIBUTE]):
        if i > 0:
            diff = token.idx - (record[ATTRIBUTE][i-1].idx + len(record[ATTRIBUTE][i-1]))
            if diff > 0:
                final_text+=" "*diff
        final_text+=token.lemma_
    return final_text
```

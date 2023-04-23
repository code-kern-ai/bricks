```python
import spacy

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def spacy_lemmatizer(record):
    nlp = spacy.load("en_core_web_sm")
    lemmatized_text = []
    for entry in record["text"]:
        doc = nlp(entry)
        lemmatized_text.append(" ".join([token.lemma_ for token in doc]))
    return {"lemmatizedTexts": lemmatized_text}
```

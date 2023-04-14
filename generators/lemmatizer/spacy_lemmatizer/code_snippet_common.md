```python
import spacy

def spacy_lemmatizer(text: str) -> str:
    """
    @param text: base text
    @return: All tokens in a text in their base form
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for text in texts:
        print(f"lemmatized text: \"{text}\" is \"{spacy_lemmatizer(text)}\"")

example_integration()
```

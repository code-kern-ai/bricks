```python
import spacy

def spacy_lemmatizer(text: str) -> str:
    """
    @param text: base text
    @return: All tokens in a text in their base form
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    final_text = ""
    for i, token in enumerate(doc):
        if i > 0:
            diff = token.idx - (doc[i-1].idx + len(doc[i-1]))
            if diff > 0:
                final_text+=" "*diff
        final_text+=token.lemma_
    return final_text
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]
    for text in texts:
        print(f"lemmatized text: \"{text}\" is \"{spacy_lemmatizer(text)}\"")

example_integration()
```

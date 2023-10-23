```python
import spacy 
from typing import List

loaded_models = {}
def load_spacy(spacy_model):
    if spacy_model not in loaded_models:  
        loaded_models[spacy_model] = spacy.load(spacy_model)
    return loaded_models[spacy_model]

def noun_splitter(text: str, spacy_model: str = "en_core_web_sm") -> List[str]:
    """
    @param text: The input text.
    @param spacy_model: The name of the spaCy model. Defaults to "en_core_web_sm".
    @ returns: A list of nouns.
    """
    nlp = load_spacy(spacy_model)
    doc = nlp(text)

    nouns_sents = set()
    for sent in doc.sents:
        for token in sent:
            if token.pos_ == "NOUN" and len(token.text) > 1:
                nouns_sents.add(token.text)
                
    return list(nouns_sents)


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 


def example_integration():
    texts = [
        "At many Barnes & Noble stores, the green-striped wallpaper and hunter-green walls have been scraped away.",
        "Many believe that this is the first time that Europeans arrived at the American continent.",
        "Porridge is delicious when made with love and care."
    ]

    for text in texts: 
        nouns = noun_splitter(text)
        print(f"Nouns in text '{text}' are -> {nouns}")

example_integration()
```
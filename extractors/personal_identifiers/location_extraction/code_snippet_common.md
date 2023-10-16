```python
import spacy
from typing import List, Tuple

loaded_models = {}
def load_spacy(spacy_model):
    if spacy_model not in loaded_models:  
        loaded_models[spacy_model] = spacy.load(spacy_model)
    return loaded_models[spacy_model]


def location_extraction(text: str, extraction_keyword: str, spacy_model: str = "en_core_web_sm") -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted names of persons  
    """
    nlp = load_spacy(spacy_model)
    doc = nlp(text)

    name_positions = []
    for ent in doc.ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            name_positions.append((extraction_keyword, ent.start, ent.end))
    return name_positions


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Tokyo is a place in Japan.", "My hometown is Cologne in Northrhine-Westphalia.", "She's from Berlin and likes EDM.", "Man I love pasta."]
    extraction_keyword = "location"
    for text in texts:
        found = location_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> {found}")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```

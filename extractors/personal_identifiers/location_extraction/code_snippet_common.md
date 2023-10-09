```python
import spacy
from typing import List, Tuple

def location_extraction(text: str, label: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param label: the label that is assigned to extracted words
    @return: positions of extracted names of persons  
    """
    nlp = spacy.load("en_core_web_sm")
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
    label = "location"
    for text in texts:
        found = location_extraction(text, label)
        if found:
            print(f"text: \"{text}\" has {label} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {label}")

example_integration()
```
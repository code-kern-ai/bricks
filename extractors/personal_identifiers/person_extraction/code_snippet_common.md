```python
import spacy
from typing import List, Tuple

def person_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted names of persons  
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    name_positions = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name_positions.append((extraction_keyword, ent.start, ent.end))
    return name_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My name is James Bond.", "Harry met Jane on a sunny afternoon.", "Say my name."]
    extraction_keyword = "name"
    for text in texts:
        found = person_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
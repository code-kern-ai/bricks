```python
from typing import List, Tuple
import spacy 

def work_of_art_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted work of arts
    """
    nlp = spacy.load("en_core_web_sm") # choose a larger model if no works of art are found
    doc = nlp(text)

    artwork_positions = []
    for entity in doc.ents:
        if entity.label_ == 'WORK_OF_ART':
            artwork_positions.append((extraction_keyword, entity.start, entity.end))

    return artwork_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Raiders of the lost arc is a great movie.", "Harry Potter is a great book.", "The Mona Lisa is a great work of art."]
    extraction_keyword = "work of art"
    for text in texts:
        found = work_of_art_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
```python
import spacy 
from typing import List, Tuple

def price_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted prices
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    price_positions = [] 
    for entity in doc.ents:
        if entity.label_ == "MONEY":
            price_positions.append((extraction_keyword, entity.start, entity.end))
    return price_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["A desktop with i7 processor costs 950 dollars in the US.", "I really need money."]
    extraction_keyword = "money"
    for text in texts:
        found = price_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
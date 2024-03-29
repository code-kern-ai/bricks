```python
import re
import spacy
from typing import List, Tuple

def percentage_extraction(text: str, extraction_keyword:str) -> List[Tuple[str, int, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted percentages
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"(-?\d+(?:[.,]\d*)?|-?[.,]\d+)\s*%")
    
    percentage_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        percentage_positions.append((extraction_keyword, span.start, span.end))
    return percentage_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["percentages 110% are found -.5% at 42,13% positions 1, 5 and 8", "Apple stock fell today."]
    extraction_keyword = "percentage"
    for text in texts:
        found = percentage_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()


```
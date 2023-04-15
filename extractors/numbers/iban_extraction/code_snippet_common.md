```python
import re
import spacy
from typing import List, Tuple

def iban_extraction(text:str, extraction_keyword:str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted IBAN numbers
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"[A-Z]{2}\d{2} ?\d{4} ?\d{4} ?\d{4} ?\d{4} ?[\d]{0,2}")
    iban_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        iban_positions.append((extraction_keyword, span.start, span.end))
    return iban_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My IBAN is DE89370400440532013000.", "I forgot my IBAN."]
    extraction_keyword = "iban"
    for text in texts:
        found = iban_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
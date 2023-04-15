```python
import re
import spacy
from typing import List, Tuple

def isbn_extraction(text: str, extraction_keyword:str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted book ISBN
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")
    
    isbn_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        isbn_positions.append((extraction_keyword, span.start, span.end))
    return isbn_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["I wish to issue this book whose ISBN is 78-0-3563-82542-0.", "lso this one whose ISBN is 69-087-647-01.", "The ISBN couldn't be found."]
    extraction_keyword = "isbn"
    for text in texts:
        found = isbn_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
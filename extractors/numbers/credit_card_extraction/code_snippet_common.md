```python
import re
import spacy 
from typing import List, Tuple

def credit_card_extraction(text: str, extraction_keyword:str) -> List[Tupel]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    credit_card_positions = []
    regex = re.compile(
        r"(\d{4}[-\s]?){3}\d{3,4}"
    )
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        credit_card_positions.append((extraction_keyword, span.start, span.end))
    return credit_card_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["This is my card details please use it carefully 4569-4039-6101-4710.", "The card number is 1231 4551 3431 1009.", "I don't have a credit card."]
    extraction_keyword = "credit card"
    for text in texts:
        found = credit_card_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
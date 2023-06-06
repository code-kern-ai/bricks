```python
import re
import spacy
from typing import List, Tuple

def bic_extraction(text:str, extraction_keyword:str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted BIC numbers
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r'\b[A-Z]{4,4}[A-Z]{2,2}[A-Z2-9][A-NP-Z0-9]([X]{3,3}|[A-WY-Z0-9]{1,1}[A-Z0-9]{2,2}|\s|\W|$)')
    bic_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        bic_positions.append((extraction_keyword, span.start, span.end))
    return bic_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My BIC is SCFBDE33XXX", "Here my BIC: COBADEBBXXX", "LBSODEB1BLN", "My IBAN DE89370400440532013000 and my BIC DGZFDEFFBER",
"GENODED1PA6", "My BIC 878653425X3", "I forgot my BIC.", "I am a false positive: AVOIDERS"]
    extraction_keyword = "BIC"
    for text in texts:
        found = bic_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
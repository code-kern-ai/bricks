```python
import re
import spacy 
import itertools
from typing import List, Tuple

def address_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted addresses
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex_1 = re.compile(r"(?:\d{1,5}(?:[A-Z ]+[ ]?)+(?:[A-Za-z-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Hill|Alley|Alle|City)[,](?:[ A-Za-z0-9,]+[ ]?)?)")
    regex_2 = re.compile(r"(?:(?:[A-Za-z-]?)+[ ](?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Str(?:\.)?|Hill|Alley|Alle|City)[ ]+\d{1,5},(?:[ A-Za-z0-9,]+[ ]?)?)")

    address_positions = []
    if regex_1.findall(text) or regex_2.findall(text):
        for match in itertools.chain(regex_1.finditer(text), regex_2.finditer(text)):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            address_positions.append((extraction_keyword, span.start, span.end))
    return address_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["The white house is located at 1600 Pennsylvania Ave NW · 20006 Washington", "I live at 35 Wood Lane, Pilsbury ME19 7DY, United Kingdom.", "I have also lived at 221BE Baker-callum Street, London VIC 3SX, United Kingdom.", "Where is the address?"]
    extraction_keyword = "address"
    for text in texts:
        found = address_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
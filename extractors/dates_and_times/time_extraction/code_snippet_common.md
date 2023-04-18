```python
from typing import List, Tuple
import re
import spacy

def time_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted times
    """
    regex = re.compile(
        r"\b(1[0-2]|[1-9])\s*[apAP][. ]*[mM]\.?|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?(?:(?:\s?[ap](?:\.m\.)?)|(?:\s?[AP](?:\.M\.)?)))|(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?"
    )
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    time_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        time_positions.append((extraction_keyword, span.start, span.end))
    return time_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Right now it is 14:40:37.", "Three hours ago it was 11:40 am.", "Two hours and twenty mins from now it will be 5PM.", "Time is relative."]
    extraction_keyword = "time"
    for text in texts:
        found = time_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
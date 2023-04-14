```python
import re
import spacy
from typing import List, Tuple

def digit_extraction(text: str, extraction_keyword: str, digit_length:int) -> List[Tuple[str, int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    num_string = "{"+f"{digit_length}"+"}"
    regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")
    
    digit_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        digit_positions.append((extraction_keyword, span.start, span.end))
    return digit_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My PIN is 1337.", "Sorry, I forgot my PIN."]
    extraction_keyword = "digit"
    digit_len = 4
    for text in texts:
        found = digit_extraction(text, extraction_keyword, digit_len)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
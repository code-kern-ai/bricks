```python
import re
import spacy
import phonenumbers
from typing import List, Tuple

def phone_number_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}")
        
    phone_positions = []
    for match in regex.finditer(text):
        parsed_num = phonenumbers.parse(match.group(0), None)
        if phonenumbers.is_valid_number(parsed_num):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            phone_positions.append((extraction_keyword, span.start, span.end))
    return phone_positions

# ↑ necessary bricks function '
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["So here's my number +442083661177. Call me maybe!", "Can I have your phone number?"]
    extraction_keyword = "phone number"
    for text in texts:
        found = phone_number_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
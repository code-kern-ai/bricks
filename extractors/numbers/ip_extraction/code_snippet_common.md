```python
import re
import spacy
from typing import List, Tuple

def ip_extraction(text:str, extraction_keyword:str) -> List[Tuple[str, int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    
    ip_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        ip_positions.append((extraction_keyword, span.start, span.end))
    return ip_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["The IP addressing range is from 0.0.0.0 to 255.255.255.255.", "No IP address found."]
    extraction_keyword = "ip address"
    for text in texts:
        found = ip_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
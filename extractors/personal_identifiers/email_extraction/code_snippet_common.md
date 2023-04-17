```python
import re
import spacy
from typing import List, Tuple

def email_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted emails
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")

    email_positions = []
    doc = nlp(text)
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        email_positions.append((extraction_keyword, span.start, span.end))
    return email_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My E-Mail address is jane.doe@gmail.com", "Our support mail is support@awesome-co.com"]
    extraction_keyword = "email"
    for text in texts:
        found = email_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
```python
import re
import spacy
from typing import List, Tuple

def url_extraction(text: str, extraction_keyword: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted URLs
    """
    npl = spacy.load("en_core_web_sm")
    doc = npl(text)

    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")  

    url_positions = []   
    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        url_positions.append((extraction_keyword, span.start, span.end)) 
    return url_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Check out https://kern.ai!", "Visit https://crowd.dev today!", "Can you send me the url?"]
    extraction_keyword = "url"
    for text in texts:
        found = url_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
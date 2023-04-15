```python
import re
import spacy
from typing import List, Tuple

def goodbye_extraction(text: str, extraction_keyword: str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: goodbye phrase positions
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"((?:((?i)good)(?:[ ])?)?((?i)bye)|(?i)Ciao|(?:((?i)see you)(?:[ ]?)((?i)tomorrow|later|soon)?))")

    goodbye_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        goodbye_positions.append((extraction_keyword, span.start, span.end))

    return goodbye_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["I will leave for now since I have to cook dinner. Goodbye, and ciao to you as well!"]
    extraction_keyword = "goodbye"
    for text in texts:
        found = goodbye_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
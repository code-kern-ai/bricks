```python
import re
import spacy
from typing import List, Tuple

def hashtag_extraction(text: str, extraction_keyword: str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: extracted hashtag positions
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    regex = re.compile(r"#(\w*)")

    hashtag_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        hashtag_positions.append((extraction_keyword, span.start, span.end)) 
    return hashtag_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["In tech industry, #devrel is a very hot topic.", "Follow us on #mastodon!"]
    extraction_keyword = "hashtag"
    for text in texts:
        found = hashtag_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
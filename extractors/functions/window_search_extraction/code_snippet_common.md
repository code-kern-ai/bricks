```python
from typing import List, Tuple
import spacy
import re

def window_search_extraction(text: str, extraction_keyword: str, window: int, lookup_list:list) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    windows_search_positions = []
    for chunk in doc.noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (window // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (window // 2) + 1)
        window_doc = doc[left_bound: right_bound]
        if any([term in window_doc.text for term in lookup_list]):
            match = re.search(chunk.text, text)
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            windows_search_positions.append((extraction_keyword, span.start, span.end))
    return windows_search_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My name is Jane.", "Look, it's John over there!", "A cute little puppy."]
    lookup_list = ["Jane", "John"]
    window = 4
    extraction_keyword = "person"
    for text in texts:
        found = window_search_extraction(text, extraction_keyword, window, lookup_list)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
```python
from typing import List, Tuple
import spacy
import re


def gazetteer_extraction(text:str, extraction_keyword:str, lookup_list:list) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @param lookup_list: a list of lookup values to search with
    @return: positions of extracted gazetteer positions
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    lookup_labels = []

    for chunk in doc.noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in lookup_list]):
            match = re.search(chunk.text, text)
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            lookup_labels.append((extraction_keyword, span.start, span.end))
    return lookup_labels

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My favourite dish is Pizza.", "I really like Pasta.", "New York is a great city."]
    lookup_list = ["Pizza", "Pasta"]
    extraction_keyword = "food"
    for text in texts:
        found = gazetteer_extraction(text, extraction_keyword, lookup_list)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
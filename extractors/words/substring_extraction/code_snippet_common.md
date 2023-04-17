```python
import spacy
from typing import List, Tuple

def substring_extraction(text:str, extraction_keyword:str, substring: str) -> List[Tuple[str, int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @param substring: the substring to be found in a text
    @return: found substrings 
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    start_index = text.find(substring)
    end_index = start_index + len(substring)

    if start_index != -1:
        span = doc.char_span(start_index, end_index, alignment_mode="expand")
        return (extraction_keyword, span.start, span.end)

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Italians eat a lot of pasta, often with tomatoes."]
    extraction_keyword = "substring"
    substring = "Italians eat a lot of pasta"
    for text in texts:
        found = substring_extraction(text, extraction_keyword, substring)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
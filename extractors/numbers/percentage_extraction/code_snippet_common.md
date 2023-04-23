```python
import re
import spacy
from typing import List, Tuple

def percentage_extraction(text: str, extraction_keyword: str, regex_pattern: str) -> List[Tuple[str, int]]:

    def regex_search(pattern, string):
        prev_end = 0
        while True:
            match = re.search(pattern, string)
            if not match:
                break

            start_, end_ = match.span()
            yield start_ + prev_end, end_ + prev_end

            prev_end += end_
            string = string[end_:]

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    percentage_positions = []  
    for start, end in regex_search(regex_pattern, text):
        span = doc.char_span(start, end, alignment_mode="expand")
        percentage_positions.append((extraction_keyword, span.start, span.end))
    return percentage_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["percentages 110% are found -.5% at 42,13% positions 1, 5 and 8", "Apple stock fell today."]
    regex_pattern = r"(-?\d+(?:[.,]\d*)?|-?[.,]\d+)%"
    extraction_keyword = "percentage"
    for text in texts:
        found = percentage_extraction(text, regex_pattern, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
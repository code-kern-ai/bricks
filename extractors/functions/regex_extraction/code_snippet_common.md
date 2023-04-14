```python
from typing import List, Tuple
import re
import spacy

def regex_extraction(text: str, extraction_keyword: str, regex: str) -> List[Tuple[str,int]]:
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

    regex_extractions = []
    for start, end in regex_search(regex, text):
        span = doc.char_span(start, end, alignment_mode="expand")
        regex_extractions.append((extraction_keyword, span.start, span.end))
    return regex_extractions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts =  ["Check out https://kern.ai!", "Visit https://kern.ai for more information", "I don't have a website."]
    extraction_keyword = "url"
    regex_pattern = r"https:\/\/[a-zA-Z0-9.\/]+"
    for text in texts:
        found = regex_extraction(text, extraction_keyword, regex_pattern)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
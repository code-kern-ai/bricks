```python
import re
import spacy
from typing import List, Tuple

def filepath_extraction(text: str, extraction_keyword: str, separator: str) -> List[Tuple[str, int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    paths = [x for x in text.split() if len(x.split(separator)) > 1]

    # We need to add an \ before separators to use them in regex
    regex_paths = [i.replace(separator, "\\" + separator) for i in paths]
    
    filepath_positions = []
    for path in regex_paths:
        pattern = rf"({path})"
        match = re.search(pattern, text)

        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        
        filepath_positions.append((extraction_keyword, span.start, span.end))
    return filepath_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["My favourite file is stored in: /usr/bin/myfavfiles/cats.png", "Linux, Mac and Windows use different separators"]
    extraction_keyword = "path"
    separator = "/"
    for text in texts:
        found = filepath_extraction(text, extraction_keyword, separator)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
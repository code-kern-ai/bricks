```python
from typing import List, Tuple
import re 
import spacy

def color_code_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
    rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
    hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
    hwb_regex = re.compile(r"hwb\([^\)]*\)")

    color_code_positions = []
    for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
        for match in regex.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            color_code_positions.append((extraction_keyword, span.start, span.end))
    return color_code_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["The color of the sky is #0000ff", "the code #000000 is black", "I like the color #ffffff"]
    extraction_keyword = "color"
    for text in texts:
        found = color_code_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
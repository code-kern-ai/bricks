```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "color"

def color_code_extraction(record):
    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
    rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
    hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
    hwb_regex = re.compile(r"hwb\([^\)]*\)")

    for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
        color_code_positions = []
        for match in regex.finditer(text):
            start, end = match.span()
            span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield LABEL, span.start, span.end 
```
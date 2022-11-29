```python
import re

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "color"

def my_tagger(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
    rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
    hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
    hwb_regex = re.compile(r"hwb\([^\)]*\)")

    for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
        for match in regex.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end)
            yield YOUR_LABEL, span.start, span.end 
```
```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "address"

def address_extraction(record): 
    regex_1 = re.compile(r"(?:\d{1,5}(?:[A-Z ]+[ ]?)+(?:[A-Za-z-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Hill|Alley|Alle|City)[,](?:[ A-Za-z0-9,]+[ ]?)?)")
    
    regex_2 = re.compile(r"(?:(?:[A-Za-z-]?)+[ ](?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Str(?:\.)?|Hill|Alley|Alle|City)[ ]+\d{1,5},(?:[ A-Za-z0-9,]+[ ]?)?)")

    text = record[ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string

    if regex_1.findall(text):
        for match in regex_1.finditer(text):
            start, end = match.span()
            span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield LABEL, span.start, span.end

    if regex_2.findall(text):
        for match in regex_2.finditer(text):
            start, end = match.span()
            span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield LABEL, span.start, span.end
```
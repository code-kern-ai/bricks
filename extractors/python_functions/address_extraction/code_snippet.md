```python
from typing import Dict
import re
import spacy

def location(text: str = None) -> Dict:
    if text is None:
        text = "I live at 35 Wood Lane, Pilsbury ME19 7DY, United Kingdom. But I have also lived at 221BE Baker-callum Street, London VIC 3SX, United Kingdom."
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    regex_1 = re.compile(r"(?:\d{1,5}(?:[A-Z ]+[ ]?)+(?:[A-Za-z-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Hill|Alley|Alle|City)[,](?:[ A-Za-z0-9,]+[ ]?)?)")
    regex_2 = re.compile(r"(?:(?:[A-Za-z-]?)+[ ](?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Str(?:\.)?|Hill|Alley|Alle|City)[ ]+\d{1,5},(?:[ A-Za-z0-9,]+[ ]?)?)")
    addresses = []

    if regex_1.findall(text):
        for match in regex_1.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end)
            addresses.append([span.start, span.end, span.text])
    if regex_2.findall(text):
        for match in regex_2.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end)
            addresses.append([span.start, span.end, span.text])

    return {"addresses": addresses}
```
```python
import re

def location(record): 
    regex_1 = re.compile(r"(?:\d{1,5}(?:[A-Z ]+[ ]?)+(?:[A-Za-z-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Hill|Alley|Alle|City)[,](?:[ A-Za-z0-9,]+[ ]?)?)")
    
    regex_2 = re.compile(r"(?:(?:[A-Za-z-]?)+[ ](?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Str(?:\.)?|Hill|Alley|Alle|City)[ ]+\d{1,5},(?:[ A-Za-z0-9,]+[ ]?)?)")

    if regex_1.findall(record["your-text"].text):
        for match in regex_1.finditer(record["your-text"].text):
            start, end = match.span()
            span = record["your-text"].char_span(start, end)
            yield "address", span.start, span.end

    if regex_2.findall(record["your-text"].text):
        for match in regex_2.finditer(record["your-text"].text):
            start, end = match.span()
            span = record["your-text"].char_span(start, end)
            yield "address", span.start, span.end
```
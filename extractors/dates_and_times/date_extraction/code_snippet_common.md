```python
from typing import List, Tuple
import re
import spacy

def date_extraction(text:str, extraction_keyword:str) -> List[Tuple[str,int]]:
    """
    @param text: the input text
    @param extraction_keyword: the label that is assigned to extracted words
    @return: positions of extracted dates
    """
    regex = re.compile(
        r"(?:[0-9]{1,2}|[0-9]{4}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    date_positions = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        date_positions.append((extraction_keyword, span.start, span.end))
    return date_positions

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["Today is 04.11.2022. Yesterday was 03/11/2022.", "Tomorrow is 05-11-2022.", "Day after tomorrow is 6 Nov 2022.", "What a nice day!"]
    extraction_keyword = "date"
    for text in texts:
        found = date_extraction(text, extraction_keyword)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```
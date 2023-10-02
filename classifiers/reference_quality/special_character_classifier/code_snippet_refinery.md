```python
import unicodedata
from typing import Set

ATTRIBUTE: str = "text" # only text attributes
ALLOWED_RANGES: Set[int] = set(range(0x0020, 0x007F)).union( # Basic Latin
    set(range(0x00A0, 0x00FF)), # Latin-1 Supplement
    set(range(0x0100, 0x017F)),  # Latin Extended-A
    set(range(0x0180, 0x024F)),  # Latin Extended-B
    set(range(0x2000, 0x206F)),  # General Punctuation
    set(range(0x20A0, 0x20CF)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
)  

def special_character_classifier(record):
    global ALLOWED_RANGES
    text = record[ATTRIBUTE].text    
    for char in text:
        if ord(char) not in ALLOWED_RANGES and unicodedata.category(char) != "Zs":
            return True
    return False
```
```python
import unicodedata
from typing import Optional, List, Tuple

ATTRIBUTE: str = "text" # only text attributes
ALLOWED_RANGES: List[int] = None # list of integers that represent Unicode code points
LABEL: str = "has_special_character"

def special_character_classifier(record):
    text = record[ATTRIBUTE].text    

    allowed = ALLOWED_RANGES
    if not allowed:
        allowed = default_allowed_values
    for char in text:
        if ord(char) not in allowed and unicodedata.category(char) != "Zs":
            return LABEL

default_allowed_values = set(range(32, 127)).union( # Basic Latin
    set(range(160, 255)), # Latin-1 Supplement
    set(range(256, 384)),  # Latin Extended-A
    set(range(384, 592)),  # Latin Extended-B
    set(range(8192, 8303)),  # General Punctuation
    set(range(8352, 8399)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
)
```
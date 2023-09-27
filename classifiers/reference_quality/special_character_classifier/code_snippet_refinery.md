```python
import unicodedata
from typing import List

ATTRIBUTE: str = "text" # only text attributes
ALLOWED_RANGES: List[str] = None

def special_character_classifier(record):
    global ALLOWED_RANGES
    text = record[ATTRIBUTE].text
    if ALLOWED_RANGES is None:
        ALLOWED_RANGES = [
            (0x0020, 0x007F),  # Basic Latin
            (0x00A0, 0x00FF),  # Latin-1 Supplement
            (0x0100, 0x017F),  # Latin Extended-A
            (0x0180, 0x024F),  # Latin Extended-B
            (0x2000, 0x206F),  # General Punctuation
            (0x20A0, 0x20CF),  # Currency Symbols
        ]

    # Allowed control characters
    allowed_controls = {"\n", "\t", "\r"}

    unusual_chars = {
        char
        for char in text
        if not any(start <= ord(char) <= end for start, end in ALLOWED_RANGES)
        and unicodedata.category(char) != "Zs"
        and char not in allowed_controls
    }
    return len(unusual_chars) > 0
```
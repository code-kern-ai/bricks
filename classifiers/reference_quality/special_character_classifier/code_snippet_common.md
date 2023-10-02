```python
import unicodedata
from typing import List,Optional, Set

DEFAULT_ALLOWED_RANGES = set(range(0x0020, 0x007F)).union( # Basic Latin
    set(range(0x00A0, 0x00FF)), # Latin-1 Supplement
    set(range(0x0100, 0x017F)),  # Latin Extended-A
    set(range(0x0180, 0x024F)),  # Latin Extended-B
    set(range(0x2000, 0x206F)),  # General Punctuation
    set(range(0x20A0, 0x20CF)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
    )  


def contains_special_characters(text: str, allowed_ranges: Optional[Set[int]] = None) -> bool:
    """
    @param text: Text to detect special characters in
    @param allowed_char_codes: Set of allowed char codes.
    @return: True if text contains unusual characters, False otherwise.
    """
    
    if allowed_ranges is None:
        allowed_ranges = DEFAULT_ALLOWED_RANGES
    
    for char in text:
        if ord(char) not in allowed_ranges and unicodedata.category(char) != "Zs":
            return True
    return False


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This contains a special char 你好.", "Such a clean text, wow!", "This is a greek letter: α", "Super funny 😀", "Rainbows are very nice."]
    for text in texts:
        print(f"\"{text}\" -> {special_character_classifier(text)}")

example_integration()
```
```python
import unicodedata
from typing import List, Tuple

DEFAULT_ALLOWED_RANGES = set(range(32, 127)).union( # Basic Latin
    set(range(160, 255)), # Latin-1 Supplement
    set(range(256, 384)),  # Latin Extended-A
    set(range(384, 592)),  # Latin Extended-B
    set(range(8192, 8303)),  # General Punctuation
    set(range(8352, 8399)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
)


def contains_special_characters(text: str, label_true: str, label_false: str, allowed_ranges: List[int] = None) -> str:
    """
    @param text: Text to detect special characters in
    @param allowed_char_codes: Set of allowed char codes.
    @return: label if text contains special character
    """
    
    if allowed_ranges is None:
        allowed_ranges = DEFAULT_ALLOWED_RANGES
    
    for char in text:
        if ord(char) not in allowed_ranges and unicodedata.category(char) != "Zs":
            return label_true
    return label_false


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This contains a special char 你好.", "Such a clean text, wow!", "This is a greek letter: α", "Super funny 😀", "Rainbows are very nice."]
    label_true = "has_special_character"
    label_false = "has_no_special_character"
    for text in texts:
        print(f"\"{text}\" -> {special_character_classifier(text, label_true, label_false)}")

example_integration()
```
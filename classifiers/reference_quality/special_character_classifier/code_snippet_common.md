```python
import unicodedata
from typing import List, Tuple

DEFAULT_ALLOWED_RANGE = set(range(32, 127)).union( # Basic Latin
    set(range(160, 255)), # Latin-1 Supplement
    set(range(256, 384)),  # Latin Extended-A
    set(range(384, 592)),  # Latin Extended-B
    set(range(8192, 8303)),  # General Punctuation
    set(range(8352, 8399)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
)


def special_character_classifier(text: str, allowed_range: List[int] = None) -> str:
    """
    @param text: Text to detect special characters in
    @param allowed_range: Set of allowed hexcodes for Unicode code range
    @return: boolean if text contains special characters
    """
    
    if allowed_range is None:
        allowed_range= DEFAULT_ALLOWED_RANGE
    
    for char in text:
        if ord(char) not in allowed_range and unicodedata.category(char) != "Zs":
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
import unicodedata
from typing import Optional, List, Tuple
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "Super funny haha 😀.",
    "allowedRanges": None
}

ALLOWED_RANGES = set(range(0x0020, 0x007F)).union( # Basic Latin
    set(range(0x00A0, 0x00FF)), # Latin-1 Supplement
    set(range(0x0100, 0x017F)),  # Latin Extended-A
    set(range(0x0180, 0x024F)),  # Latin Extended-B
    set(range(0x2000, 0x206F)),  # General Punctuation
    set(range(0x20A0, 0x20CF)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
    )  

class SpecialCharacterClassifierModel(BaseModel):
    text: str
    allowed_ranges: Optional[List[Tuple[int,int]]] = None

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def special_character_classifier(req: SpecialCharacterClassifierModel):
    """Checks if a string contains special characters"""
    text = req.text
    allowed_ranges = req.allowed_ranges
    if allowed_ranges is None:
        allowed_ranges = ALLOWED_RANGES

    for char in text:
        if ord(char) not in allowed_ranges and unicodedata.category(char) != "Zs":
            return {"contains_special_char": "true"}
    return {"contains_special_char": "false"}

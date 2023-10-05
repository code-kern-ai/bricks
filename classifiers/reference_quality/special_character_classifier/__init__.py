import unicodedata
from typing import Optional, List, Tuple
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "Super funny haha 😀.",
    "label_true": "has_special_character",
    "label_false": "has_no_special_character",
    "allowedRanges": None
}

ALLOWED_RANGES = set(range(32, 127)).union( # Basic Latin
    set(range(160, 255)), # Latin-1 Supplement
    set(range(256, 384)),  # Latin Extended-A
    set(range(384, 592)),  # Latin Extended-B
    set(range(8192, 8303)),  # General Punctuation
    set(range(8352, 8399)),  # Currency Symbols
    set([ord("\t"), ord("\n"), ord("\r")])# common stop chars
)

class SpecialCharacterClassifierModel(BaseModel):
    text: str
    label_true: str
    label_false: str
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
            return {"contains_special_char": req.label_true}
    return {"contains_special_char": req.label_false}

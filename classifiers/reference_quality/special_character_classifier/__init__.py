import unicodedata
from typing import List
from pydantic import BaseModel
from nltk.corpus import words, brown

INPUT_EXAMPLE = {
    "text": "uper funny haha 😀."
}


class SpecialCharacterClassifierModel(BaseModel):
    text: str
    allowed_ranges: List[str] = None

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def special_character_classifier(req: SpecialCharacterClassifierModel):
    """Checks if a string contains special characters"""
    text = req.text
    allowed_ranges = req.allowed_ranges
    if allowed_ranges is None:
        allowed_ranges = [
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
        if not any(start <= ord(char) <= end for start, end in allowed_ranges)
        and unicodedata.category(char) != "Zs"
        and char not in allowed_controls
    }
    return {"contains_special_char": len(unusual_chars) > 0}

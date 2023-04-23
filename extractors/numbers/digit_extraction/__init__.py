import re
from pydantic import BaseModel
from typing import Optional
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "My PIN is 1337.",
    "digitLength": 4,
    "spacyTokenizer": "en_core_web_sm"
}

class DigitExtractionModel(BaseModel):
    text: str
    digitLength: int
    spacyTokenizer: Optional[str]

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def digit_extraction(req: DigitExtractionModel):
    """Extracts digits of variable length."""
    text = req.text
    number = req.digitLength

    nlp = SpacySingleton.get_nlp()
    doc = nlp(text)

    num_string = "{"+f"{number}"+"}"
    regex = re.compile(rf"(?<![0-9])[0-9]{num_string}(?![0-9])")

    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        return {"Number": [span.start, span.end]}

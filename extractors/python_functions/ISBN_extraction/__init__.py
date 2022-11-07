from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class ISBNExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "I wish to have this book issued. It's ISBN number is 78-0-7657-37844-0.",
                "spacyTokenizer": "en_core_web_sm"
            }
        }

def isbn_extractor(request: ISBNExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")

    isbn = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        isbn.append([span.start, span.end, span.text])

    return {"isbn": isbn}

from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "I wish to issue this book whose ISBN is 78-0-3563-82542-0. And also this one whose ISBN is 69-087-647-01.",
    "spacyTokenizer": "en_core_web_sm",
}


class IsbnExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def isbn_extraction(request: IsbnExtractionModel):
    """Extracts the ISBN from a text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")

    isbn = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        isbn.append(["isbn", span.start, span.end])
    return {"isbn": isbn}

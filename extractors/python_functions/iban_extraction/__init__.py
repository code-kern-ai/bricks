from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "The IBANs are 22 characters long. The first two characters are the country code, the next two are the check digits, the next four are the bank code, and the rest is the account number.",
    "spacyTokenizer": "en_core_web_sm",
}


class IbanExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def iban_extraction(request: IbanExtractionModel):
    """Extracts IBAN from text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"[A-Z]{2}\d{2} ?\d{4} ?\d{4} ?\d{4} ?\d{4} ?[\d]{0,2}")

    isbn = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        isbn.append([span.start, span.end, span.text])
    return {"iban": isbn}

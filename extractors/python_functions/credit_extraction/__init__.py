from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "This is my card details please use it carefully 4569-4039-6101-4710.",
    "spacyTokenizer": "en_core_web_sm",
}


class CreditCardExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def credit_extraction(request: CreditCardExtractionModel):
    """Extracts the credit/debit card number from a text."""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"(\d{4}[-\s]?){3}\d{3,4}")

    credit = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        credit.append([span.start, span.end, span.text])

    return {"cardDetails": credit}

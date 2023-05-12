from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "My BIC number is COBADEBBXXX",
    "spacyTokenizer": "en_core_web_sm",
}


class BicExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def bic_extraction(request: BicExtractionModel):
    """Extracts BIC from text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r'[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z2-9][A-NP-Z0-9]([X]{3,3}|[A-WY-Z0-9]{1,1}[A-Z0-9]{2,2}|[A-WY-Z0-9]{0,0})')

    bic = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        bic.append(["BIC", span.start, span.end])
    return {"bic": bic}

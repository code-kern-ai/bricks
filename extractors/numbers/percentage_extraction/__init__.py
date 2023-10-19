
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "percentages 110% are found -.5% at 42,13% positions 1, 5 and 8",
    "spacyTokenizer": "en_core_web_sm",
}

class PercentageExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def percentage_extraction(request: PercentageExtractionModel):
    """Extracts the Percentages from a text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"(?:[\d-]{17}|[\d-]{13})")

    p = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        p.append([span.start, span.end, span.text])
    return {"percentages": p}

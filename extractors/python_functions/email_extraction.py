from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class EmailExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "If you have any questions, please contact johannes.hoetter@kern.ai.",
                "spacyTokenizer": "en_core_web_sm"
            }
        }

def email_extractor(request: EmailExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")

    emails = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        emails.append([span.start, span.end, span.text])

    return {"emails": emails}

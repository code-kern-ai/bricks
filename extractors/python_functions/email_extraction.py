from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class EmailExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema = {
            "example": {
                "text": "This text extract emails like yourname@gmail.com.",
                "spacy_tokenizer": "en_core_web_sm"
            }
        }

def email_extractor(request: EmailExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    regex = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")

    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"spans": spans}

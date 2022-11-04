from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class HashExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema = {
            "example": {
                "text": "In tech industry, #devrel is a very hot topic",
                "spacy_tokenizer": "en_core_web_sm",
            }
        }

def hash_extractor(request: HashExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    regex = re.compile(r"#(\w+)")
    regex.findall(text)

    spans = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        spans.append([span.start, span.end, span.text])

    return {"extracted hashtags": spans}

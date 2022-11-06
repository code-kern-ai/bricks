from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class HashExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_web_core_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "In tech industry, #devrel is a very hot topic",
                "spacyTokenizer": "en_core_web_sm",
            }
        }

def hash_extractor(request: HashExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"#(\w+)")
    regex.findall(text)

    hashtags = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        hashtags.append([span.start, span.end, span.text])

    return {"hashtags": hashtags}

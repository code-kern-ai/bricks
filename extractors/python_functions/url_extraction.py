from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class UrlExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "Check out https://kern.ai!",
                "spacy_tokenizer": "en_core_web_sm",
            }
        }

def fn_url_extraction(request: UrlExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")
    regex_pattern.findall(text)

    urls = []
    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        urls.append([span.start, span.end, span.text])

    return {"urls": urls}

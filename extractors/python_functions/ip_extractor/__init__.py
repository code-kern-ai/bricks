from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class IpExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_web_core_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "The IP addressing range is from 0.0.0.0 to 255.255.255.255",
                "spacyTokenizer": "en_core_web_sm",
            }
        }

def fn_ip_extractor(request: IpExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    regex.findall(text)

    ip_addresses = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        ip_addresses.append([span.start, span.end, span.text])

    return {"ip_addresses": ip_addresses}
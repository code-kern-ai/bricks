from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "The IP addressing range is from 0.0.0.0 to 255.255.255.255",
    "spacyTokenizer": "en_core_web_sm",
}


class IpExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_web_core_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def ip_extraction(request: IpExtractionModel):
    """Extracts IP addresses from text"""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    regex.findall(text)

    ip_addresses = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        ip_addresses.append(["ip_address", span.start, span.end])

    return {"ip_addresses": ip_addresses}

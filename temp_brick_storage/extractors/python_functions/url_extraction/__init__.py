from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "Check out https://kern.ai!",
    "spacyTokenizer": "en_core_web_sm",
}


class UrlExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def url_extraction(request: UrlExtractionModel):
    """Extracts urls from a given text."""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    regex_pattern = re.compile(r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+")
    regex_pattern.findall(text)

    urls = []
    for match in regex_pattern.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        urls.append(["url", span.start, span.end])

    return {"urls": urls}

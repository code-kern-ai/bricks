from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "In tech industry, #devrel is a very hot topic",
    "spacyTokenizer": "en_core_web_sm",
}


class HashtagExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_web_core_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def hashtag_extraction(request: HashtagExtractionModel):
    """Detects hashtags in a text and returns them in a list."""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    regex = re.compile(r"#(\w+)")
    regex.findall(text)

    hashtags = []
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end)
        hashtags.append(["hashtag", span.start, span.end])

    return {"hashtags": hashtags}

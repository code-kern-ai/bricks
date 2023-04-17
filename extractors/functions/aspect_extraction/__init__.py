from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
from textblob import TextBlob

INPUT_EXAMPLE = {
    "text": "It has a really great battery life, but I hate the window size...",
    "spacyTokenizer": "en_core_web_sm",
    "windowSize": 4,
    "sensitivity": 0.5,
}


class AspectExtractionModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"
    windowSize: int
    sensitivity: float

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def aspect_extraction(request: AspectExtractionModel):
    """Matches aspects in a text to positive or negative sentiment."""
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(request.text)
    matches = []

    for chunk in doc.noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (request.windowSize // 2) + 1)
        right_bound = min(chunk.sent.end, chunk.end + (request.windowSize // 2) + 1)
        window_doc = doc[left_bound:right_bound]
        sentiment = TextBlob(window_doc.text).polarity
        if sentiment < -(1 - request.sensitivity):
            matches.append(["negative", chunk.start, chunk.end])
        elif sentiment > (1 - request.sensitivity):
            matches.append(["positive", chunk.start, chunk.end])

    return {"aspects": matches}

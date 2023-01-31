from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "My favourite british tea is Yorkshire tea",
    "spacyTokenizer": "en_core_web_sm"
}

class PartOfSpeechExtractorModel(BaseModel):
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def part_of_speech_extractor(req: PartOfSpeechExtractorModel):
    """Yields POS tags using spaCy."""
    text = req.text

    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text)

    pos_tags = []
    for token in doc:
        pos = token.pos_

        start, end = token.i, token.i +1
        span = doc.char_span(start, end, alignment_mode="expand")

        pos_tags.append([pos, span.start, span.end])
        
    return {"POS tags": pos_tags}
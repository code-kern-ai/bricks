from typing import List
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "Max Mustermann decided to join Kern AI, where he wants to build great software.",
    "spacyTokenizer": "en_core_web_sm",
    "lookupValues": ["Max", "Leon", "Kai", "Aaron"],
    "yourLabel": "person",
}


class GazetteerExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"
    lookupValues: List[str]
    yourLabel: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def gazetteer_extraction(request: GazetteerExtractionModel):
    """Detects full entities in a text based on some hints."""
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(request.text)
    matches = []

    for chunk in doc.noun_chunks:
        if any(
            [chunk.text in trie or trie in chunk.text for trie in request.lookupValues]
        ):
            yield request.yourLabel, chunk.start, chunk.end
    return {f"{request.yourLabel}s": matches}

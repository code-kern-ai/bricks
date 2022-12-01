from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": 'The bestseller of last month is "Mystery of the Floridian Porter" by John Doe.',
    "spacyTokenizer": "en_core_web_sm",
}


class WorkOfArtExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def work_of_art_extraction(request: WorkOfArtExtractionModel):
    """Extracts the name of the book from a text."""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    found = []

    for entity in doc.ents:
        if entity.label_ == "WORK_OF_ART":
            found.append(["work of art", entity.start, entity.end])

    return {"works of art": found}

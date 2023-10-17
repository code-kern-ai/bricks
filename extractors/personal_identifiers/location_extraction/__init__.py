from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "Tokyo is a beautiful city, which is not located in Kansas, USA.",
    "spacyTokenizer": "en_core_web_sm",
}


class LocationExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def location_extraction(req: LocationExtractionModel):
    """ Uses SpaCy to extract locations from a text."""
    text = req.text
    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text)

    names = []
    for ent in doc.ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            names.append(["location", ent.start, ent.end])
    return {"locations": names}

from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "We are developers from Kern.ai",
    "spacyTokenizer": "en_core_web_sm",
}


class OrgExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def org_extraction(request: OrgExtractionModel):
    """Detects organizations in a given text."""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    organisations = []

    for entity in doc.ents:
        if entity.label_ == "ORG":
            organisations.append(["org", entity.start, entity.end])

    return {"organisations": organisations}

from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class OrganisationExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema = {
            "example": {
                "text": "We are developers from Kern.ai",
                "spacy_tokenizer": "en_core_web_sm",
            }
        }

def organisation_extraction(request: OrganisationExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    organisation = []

    for entity in doc.ents:
        if entity.label_ == 'ORG':
            organisation.append((entity.start, entity.end, entity))

    return {"extracted organisations": organisation}

from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class OrganisationExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "We are developers from Kern.ai",
                "spacy_tokenizer": "en_core_web_sm",
            }
        }

def organisation_extraction(request: OrganisationExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    organisations = []

    for entity in doc.ents:
        if entity.label_ == 'ORG':
            organisations.append((entity.start, entity.end, entity.text))

    return {"organisations": organisations}

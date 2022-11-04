from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class OrganisationExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] 

    class Config:
        schema = {
            "example": {
                "text": "We are developers from Kern.ai",
                "spacy_tokenizer": "en_core_web_lg",
            }
        }

def organisation_extraction(request: OrganisationExtractionModel):
    text = request.text
    doc = nlp(text)

    try:
        nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    except:
        print("Unable find tokenizer. Using en_core_web_lg instead.")
        nlp = SpacySingleton.get_nlp("en_core_web_lg")

    organisation = []

    for entity in doc.ents:
        if entity.label_ == 'ORG':
            organisation.append((entity.start, entity.end, entity))

    return {"organisation": organisation}

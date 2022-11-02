from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class CompanyExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: str[Optional] = "en_core_web_lg"

def company_ext(request: CompanyExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    company = []

    for entity in doc.ents:
        if entity.label_ == 'ORG':
            company.append((entity.start, entity.end, entity))

    return {"Company": company}

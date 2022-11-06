from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class PriceExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "A desktop with i7 processor costs 950 dollars in the US.",
                "spacy_tokenizer": "en_core_web_sm"
            }
        }

def price_extractor(request: PriceExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    prices = []
    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            prices.append((entity.start, entity.end, entity.text))

    return {"prices": prices}


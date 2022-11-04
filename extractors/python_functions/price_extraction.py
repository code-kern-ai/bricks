from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class PriceExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_lg"

    class Config:
        schema = {
            "example": {
                "text": "A desktop with i7 processor costs 800 euros in Germany. In the US, it costs 950 dollars.",
                "spacy_tokenizer": "en_core_web_lg"
            }
        }

def price_extractor(request: PriceExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    prices = []
    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            prices.append((entity.start, entity.end, entity))

    return {"extracted prices": prices}


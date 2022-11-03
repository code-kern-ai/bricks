from typing import Optional, Union
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

class PriceExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_lg"

def price_ext(request: PriceExtractionModel):
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)

    prices = []
    for entity in doc.ents:
        if entity.label_ == 'MONEY':
            prices.append((entity.start, entity.end, entity))

    return {"Prices": prices}

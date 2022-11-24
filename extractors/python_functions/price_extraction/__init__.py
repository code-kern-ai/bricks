from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "A desktop with i7 processor costs 950 dollars in the US.",
    "spacyTokenizer": "en_core_web_sm",
}


class PriceExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def price_extraction(request: PriceExtractionModel):
    """Extracts prices from a given text."""
    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    prices = []
    for entity in doc.ents:
        if entity.label_ == "MONEY":
            prices.append(["price", entity.start, entity.end])

    return {"prices": prices}

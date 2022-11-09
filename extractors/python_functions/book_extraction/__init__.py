from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": 'The bestseller of last month is "Mystery of the Floridian Porter" by John Doe.',
    "spacyTokenizer": "en_core_web_sm",
}


class BookExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def book_extraction(request: BookExtractionModel):
    """Extracts the name of the book from a text."""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    books = []

    for entity in doc.ents:
        if entity.label_ == "WORK_OF_ART":
            books.append(["book", entity.start, entity.end])

    return {"books": books}

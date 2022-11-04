from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class NameExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: str[Optional] = "en_core_web_lg"

    class Config:
        schema = {
            "example": {
                "text": "John Doe worked with Jane Doe and now they are together.",
                "spacy_tokenizer": "en_core_web_lg",
            }
        }

def name_extractor(request: NameExtractionModel):

    """
    Returns a dictionary of the extracted names from a given text.
    """

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    name = []

    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            name.append((entity.start, entity.end, entity))
    # "name" will contain all the occurrences of a particular name.
    # This is because spacy treats each word in a text as a unique vector.
    # So, two occurrences of "Div" does not mean "Div" == "Div"!
    names = {"Extracted names": name}

    return names

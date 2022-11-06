from typing import Optional
from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

class NameExtractionModel(BaseModel):
    text: str
    spacy_tokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {
            "example": {
                "text": "John Doe worked with Jane Doe and now they are together.",
                "spacy_tokenizer": "en_core_web_sm"
            }
        }

def name_extractor(request: NameExtractionModel):

    """
    Returns a dictionary of the extracted names from a given text.
    """

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacy_tokenizer)
    doc = nlp(text)
    names = []

    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            names.append((entity.start, entity.end, entity.text))
    # "name" will contain all the occurrences of a particular name.
    # This is because spacy treats each word in a text as a unique vector.
    # So, two occurrences of "Div" does not mean "Div" == "Div"!
    names = {"names": names}

    return names

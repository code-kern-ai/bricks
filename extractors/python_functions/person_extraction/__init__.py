from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "John Doe worked with Jane Doe and now they are together.",
    "spacyTokenizer": "en_core_web_sm",
}


class PersonExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def person_extraction(request: PersonExtractionModel):
    """
    Returns the occurrences of names of people in a dictionary.
    """

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    names = []

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            names.append(["person", entity.start, entity.end])
    # "name" will contain all the occurrences of a particular name.
    # This is because spacy treats each word in a text as a unique vector.
    # So, two occurrences of "Div" does not mean "Div" == "Div"!
    names = {"names": names}

    return names

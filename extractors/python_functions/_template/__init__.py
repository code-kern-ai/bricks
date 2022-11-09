from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "some text I want to use as an example",
    "spacyTokenizer": "en_core_web_sm",
    # if required, add more attributes here
}


# make sure the model name fits to the function name, as it is actually parsed
# i.e. my_tagger -> MyTaggerModel (capitalized and "Model" appended)
class MyTaggerModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"
    # if required, add more attributes here

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def my_tagger(request: MyTaggerModel):
    """my docstring to describe what the function does"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    # my function logic here
    results = []

    # append to the results triplets in the form of [label, start, end]

    # rename extractedEntities to whatever you want to call the output
    return {"extractedEntities": results}

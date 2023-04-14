from pydantic import BaseModel
from typing import List

INPUT_EXAMPLE = {
    "text": "The mail was sent from john@kern.ai, please contact him for further information.",
    "lookupValues": ["john@kern.ai", "jane@kern.ai"],
    "yourLabel": "in lookup",
}


class LookupListModel(BaseModel):
    text: str
    lookupValues: List[str]
    yourLabel: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def lookup_list(request: LookupListModel):
    """Checks if a given text contains any of the given lookup values."""

    text = request.text
    lookupValues = request.lookupValues
    yourLabel = request.yourLabel

    for lookupValue in lookupValues:
        if lookupValue.lower() in text.lower():
            return {yourLabel: True}

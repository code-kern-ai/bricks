from pydantic import BaseModel
from typing import List

class LookupListModel(BaseModel):
    text: str
    lookupValues: List[str]
    yourLabel: str

    class Config:
        schema_extra = {
            "example": {
                "text": "The mail was sent from johannes.hoetter@kern.ai, please contact him for further information.",
                "lookupValues": ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai"],
                "yourLabel": "ham"
            }
        }


def fn_lookup_list(request: LookupListModel):
    text = request.text
    lookupValues = request.lookupValues
    yourLabel = request.yourLabel
    
    for lookupValue in lookupValues:
        if lookupValue.lower() in text.lower():
            return {yourLabel: True}

from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "This is an english sentence.",
    "authKey": "key-here"
}

class MyClfModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def _template(request: MyClfModel):
    """Detects the language of a given text."""

    text = request.text

    # my function logic here
    result = None

    # rename classification to whatever you want to call the output
    return {"classification": result}

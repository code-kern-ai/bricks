from pydantic import BaseModel

INPUT_EXAMPLE = {"text": "This sentence should have 39 characters."}


class StringLenghtModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def string_lenght(request: StringLenghtModel):
    """Calculate the lenght of a text."""
    text = request.text
    lenght = len(text)
    return {"lenght": lenght}
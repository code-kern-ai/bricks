from pydantic import BaseModel
from textblob import TextBlob

INPUT_EXAMPLE = {"text": "This is too short!"}


class TextLengthModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def text_length(req: TextLengthModel):
    words = req.text.split()
    length = len(words)
    if length < 5:
        return {"text_length": "short"}
    elif length < 20:
        return {"text_length": "medium"}
    else:
        return {"text_length": "long"}

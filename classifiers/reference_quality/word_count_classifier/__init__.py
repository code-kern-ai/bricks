from pydantic import BaseModel

INPUT_EXAMPLE = {"text": "This is too short!"}


class WordCountClassifierModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def word_count_classifier(req: WordCountClassifierModel):
    """Checks the length of a string by counting the number of words in it"""
    words = req.text.split()
    length = len(words)
    if length < 5:
        return {"text_length": "short"}
    elif length < 20:
        return {"text_length": "medium"}
    else:
        return {"text_length": "long"}

from pydantic import BaseModel
from textblob import TextBlob

INPUT_EXAMPLE = {"text": "Wow, this is awesome!"}


class TextblobSentimentModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def setall(d, keys, value):
    for k in keys:
        d[k] = value


MAX_SCORE = 100
MIN_SCORE = 0

OUTCOMES = {}
setall(OUTCOMES, range(80, MAX_SCORE + 1), "subjective")
setall(OUTCOMES, range(60, 80), "rather subjective")
setall(OUTCOMES, range(40, 60), "neutral")
setall(OUTCOMES, range(20, 40), "rather objective")
setall(OUTCOMES, range(MIN_SCORE, 20), "objective")


def get_mapping_subjectivity(score):
    if score < MIN_SCORE:
        return OUTCOMES[MIN_SCORE]
    return OUTCOMES[int(score)]


def textblob_subjectivity(request: TextblobSentimentModel):
    """Calculate subjectivity of a text."""
    blob = TextBlob(request.text)

    return {"subjectivity": get_mapping_subjectivity(blob.sentiment.subjectivity * 100)}

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
MIN_SCORE = -100

OUTCOMES = {}
setall(OUTCOMES, range(40, MAX_SCORE + 1), "very positive")
setall(OUTCOMES, range(20, 40), "positive")
setall(OUTCOMES, range(-20, 20), "neutral")
setall(OUTCOMES, range(-40, -20), "negative")
setall(OUTCOMES, range(MIN_SCORE, -40), "very negative")


def get_mapping_sentiment(score):
    if score < MIN_SCORE:
        return OUTCOMES[MIN_SCORE]
    return OUTCOMES[int(score)]


def textblob_sentiment(request: TextblobSentimentModel):
    """Calculate sentiment of a text."""

    blob = TextBlob(request.text)

    return {"sentiment": get_mapping_sentiment(blob.sentiment.polarity * 100)}

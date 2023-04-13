from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

INPUT_EXAMPLE = {"text": "World peace announced by the United Nations."}


class VaderSentimentClassifierModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def vader_sentiment_classifier(req):
    """Get the sentiment of a text using the VADER algorithm."""
    analyzer = SentimentIntensityAnalyzer()
    text = req.text

    vs = analyzer.polarity_scores(text)
    if vs["compound"] >= 0.05:
        return {"sentiment": "positive"}
    elif vs["compound"] > -0.05:
        return {"sentiment": "neutral"}
    elif vs["compound"] <= -0.05:
        return {"sentiment": "negative"}

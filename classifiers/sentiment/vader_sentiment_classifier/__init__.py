from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

INPUT_EXAMPLE = {
    "text": "World peace announced by the United Nations.",
    "mode": "classification" # Choose "scores" to only get the sentiment scores as floats
}

class VaderSentimentClassifierModel(BaseModel):
    text: str
    mode: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def vader_sentiment_classifier(req):
    '''Get the sentiment of a text using the VADER algorithm.'''
    analyzer = SentimentIntensityAnalyzer()
    text = req.text

    vs = analyzer.polarity_scores(text)
    if req.mode == "classification":
        if vs["compound"] >= 0.05:
            return {"sentiment": "positive"}
        elif vs["compound"] > -0.05: 
            return {"sentiment": "neutral"}
        elif vs["compound"] <= -0.05:
            return {"sentiment": "negative"}
    elif req.mode == "scores": 
        return {"sentiment_scores": vs}
    else:
        return "Please choose either the 'classification' or 'scores' mode!"

from pydantic import BaseModel
from typing import Dict
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT_EXAMPLE = {
    "textOne": "The quick brown fox jumps over the lazy dog",
    "textTwo": "The quick yellow cat jumps over the lazy dog",
}

class ManhattanDistanceModel(BaseModel):
    textOne: str
    textTwo: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def manhattan_distance(request: ManhattanDistanceModel):
    """Calculates the Manhattan distance between two strings. Uses TF-IDF to vectorize the strings."""

    text_one = request.textOne
    text_two = request.textTwo

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([text_one.lower(), text_two.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    return {"manhattanDistance": sum(abs(val1-val2) for val1, val2 in zip(vect_one, vect_two))}
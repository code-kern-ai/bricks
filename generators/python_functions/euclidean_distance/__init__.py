import numpy as np 
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT_EXAMPLE = {
    "textOne": "Ten amazing facts about planet Mars.",
    "textTwo": "Ten amazing facts about the sun",
}

class EuclideanDistanceModel(BaseModel):
    textOne: str
    textTwo: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def euclidean_distance(req: EuclideanDistanceModel):
    """Calculates the euclidean distance between two text embedding vectors."""

    text_one = req.textOne
    text_two = req.textTwo

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([text_one.lower(), text_two.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Calculate the euclidean distance
    euc_distance = np.linalg.norm(vect_one - vect_two)

    return {"euclidean_distance": euc_distance}
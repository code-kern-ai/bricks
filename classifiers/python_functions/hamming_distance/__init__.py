import numpy as np
from pydantic import BaseModel
from scipy.spatial.distance import hamming
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT_EXAMPLE = {
    "textOne": "Grandpa is eating!", 
    "textTwo": "Let's eat, Grandpa!"
}

class HammingDistanceModel(BaseModel):
    textOne: str
    textTwo: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def hamming_distance(req: HammingDistanceModel):
    """Calculates the Hamming distance between two embeddings to find similar sentences."""

    text_one = req.textOne
    text_two = req.textTwo

    tfidf = TfidfVectorizer().fit_transform([text_one, text_two])

    dense = tfidf.toarray()
    vect_one, vect_two = np.squeeze(dense[0]), np.squeeze(dense[1])

    hamming_distance = hamming(vect_one, vect_two)
    return {"Hamming distance": hamming_distance}
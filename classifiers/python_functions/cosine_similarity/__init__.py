import numpy as np 
from numpy import dot
from numpy.linalg import norm
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT_EXAMPLE = {
    "textOne": "Ten amazing pasta recipes.",
    "textTwo": "Ten amazing steak recepes."
}

class CosineSimilarityModel(BaseModel):
    textOne: str
    textTwo: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def cosine_similarity(req: CosineSimilarityModel):
    '''Claculates the cosine similarity between to sentences.'''

    text_one = req.textOne
    text_two = req.textTwo

    # Transform sentences to a vector
    tfidf = TfidfVectorizer()
    vects = tfidf.fit_transform([text_one.lower(), text_two.lower()])
    vects = vects.todense()
    vect_one, vect_two = np.squeeze(np.asarray(vects[0])), np.squeeze(np.asarray(vects[1]))

    # Calculate the cosine similarity between the two vectors
    cos_sim = dot(vect_one, vect_two)/(norm(vect_one)*norm(vect_two))
    return {"cosine_similarity": cos_sim}
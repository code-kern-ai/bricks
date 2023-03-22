from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "Hello, I am talking about coding at Kern AI!"
}

class SpacyLemmatizerModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def spacy_lemmatizer(req: SpacyLemmatizerModel):
    """Converts words in a sentence to there base form."""
    text = req.text

    nlp = SpacySingleton.get_nlp("en_core_web_sm")
    doc = nlp(text)

    # Remove any line breakers as well
    lemmatized_text = " ".join([token.lemma_ for token in doc])

    return {"lemmatized_text": lemmatized_text}


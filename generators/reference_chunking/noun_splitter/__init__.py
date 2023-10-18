from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "My favorite noun is 'friend'.",
    "spacy_model": "en_core_web_sm"
}

class NounChunkerModel(BaseModel):
    text: str
    spacy_model: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def noun_splitter(req: NounChunkerModel):
    """Creates embedding chunks based on the nouns in a text"""
    nlp = SpacySingleton.get_nlp(req.spacy_model)
    doc = nlp(req.text)

    nouns_sents = []
    for sent in doc.sents:
        nouns = [token.text for token in sent if token.pos_ == "NOUN" and len(token.text) > 1]
        if nouns:
            nouns_sents.extend([" ".join(nouns[i:i+1]) for i in range(0, len(nouns), 1)])
    return {"nouns": list(set(nouns_sents))}


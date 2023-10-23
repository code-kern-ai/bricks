from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "text": "My favorite noun is 'friend'.",
    "spacy_model": "en_core_web_sm",
}


class NounSplitterModel(BaseModel):
    text: str
    spacy_model: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def noun_splitter(req: NounSplitterModel):
    """Creates embedding chunks based on the nouns in a text"""
    nlp = SpacySingleton.get_nlp(req.spacy_model)
    doc = nlp(req.text)

    nouns_sents = set()
    for sent in doc.sents:
        for token in sent:
            if token.pos_ == "NOUN" and len(token.text) > 1:
                nouns_sents.add(token.text)

    return {"nouns": list(nouns_sents)}

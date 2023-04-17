from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {"text": "Hello, I am talking about coding at Kern AI!"}


class SpacyLemmatizerModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def spacy_lemmatizer(req: SpacyLemmatizerModel):
    """Converts words in a sentence to there base form."""
    text = req.text

    nlp = SpacySingleton.get_nlp("en_core_web_sm")
    doc = nlp(text)
    final_text = ""
    for i, token in enumerate(doc):
        if i > 0:
            diff = token.idx - (doc[i - 1].idx + len(doc[i - 1]))
            if diff > 0:
                final_text += " " * diff
        final_text += token.lemma_
    return {"lemmatized_text": final_text}

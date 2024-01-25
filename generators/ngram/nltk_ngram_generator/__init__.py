from nltk.util import ngrams
from pydantic import BaseModel
from generators.util.spacy import SpacySingleton

INPUT_EXAMPLE = {"sentence": "Despite the unpredictable weather, the enthusiastic crowd gathered at the park for the annual summer festival, eagerly anticipating an evening filled with music, food, and vibrant celebrations.",
                "spacyTokenizer": "en_core_web_sm",
                "ngram_size": 2}


class NltkNgramGeneratorModel(BaseModel):
    sentence: str
    spacyTokenizer: str = "en_core_web_sm"
    ngram_size: int = 2

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def nltk_ngram_generator(req: NltkNgramGeneratorModel):
    """Generate word n-grams from the input sentence. Punctuation and stop words are preserved."""
    sentence = req.sentence
    ngram_size = req.ngram_size
    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    n_grams = list(ngrams(tokens, ngram_size))

    return {"n_grams": n_grams}

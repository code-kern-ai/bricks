from pydantic import BaseModel
from generators.util.spacy import SpacySingleton
from collections import Counter

INPUT_EXAMPLE = {
    "text": "APPL went down by 5% in the past two weeks. Shareholders are concerned over the continued recession since APPL and NASDAQ have been hit hard by this recession. Risks pertaining to short-selling are pouring in as APPL continues to depreciate. If the competitors come together and start short-selling, the stock can face calamity.",
    "spacyTokenizer": "en_core_web_sm",
    "n_words": 5
}


class MostFrequentWordsModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"
    n_words: int

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def most_frequent_words(request: MostFrequentWordsModel):
    """Generates the frequency of the words and shows top n words"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)

    words = [token.text for token in doc if not token.is_stop and not token.is_punct]

    return {"frequentWords": Counter(words).most_common(request.n_words)}

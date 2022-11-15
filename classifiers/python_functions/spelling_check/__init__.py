from pydantic import BaseModel
from nltk.corpus import words, brown

INPUT_EXAMPLE = {
    "text": "The sun is shinng brigt today."
}


class SpellingCheckModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def spelling_check(request: SpellingCheckModel):
    """Checks for spelling errors in a text."""

    words_corpus = words.words()
    brown_corpus = brown.words()
    word_list = words_corpus + brown_corpus
    text = request.text
    text_list_lower = text.replace(',', '').replace('.', '').lower().split()
    text_list_original = text.replace(',', '').replace('.', '').split()

    misspelled = []
    for i, _ in enumerate(text_list_lower):
        if text_list_lower[i] not in word_list and text_list_original[i] not in word_list:
            misspelled.append(text_list_original[i])

    return {
        "spellingErrors": len(misspelled),
    }

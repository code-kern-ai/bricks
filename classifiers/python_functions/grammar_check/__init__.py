from pydantic import BaseModel
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
nltk.download('words')
from nltk.corpus import words

INPUT_EXAMPLE = {
    "text": "This text have some gramatical errors."
}


class GrammarCheckModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def grammar_check(request: GrammarCheckModel):
    """Checks for spelling errors in a text."""

    correct_words = words.words()
    text = request.text
    text_list_lower = text.replace(',', '').replace('.', '').lower().split()
    text_list_original = text.replace(',', '').replace('.', '').split()

    misspelled = []
    for i, _ in enumerate(text_list_lower):
        if text_list_lower[i] not in correct_words and text_list_original[i] not in correct_words:
            misspelled.append(text_list_original[i])

    suggestions = []
    for word in misspelled:
        temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w) for w in correct_words if w[0] == word[0]]
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:3]])

    for i, _ in enumerate(text_list_original):
        for j, _ in enumerate(misspelled):
            if text_list_original[i] == misspelled[j]:
                text_list_original[i] = suggestions[j][0]

    text_corr = " ".join(text_list_original)

    return {
        "misspelledWords": misspelled,
        "suggestedCorrections": suggestions,
        "correctText": text_corr,
    }

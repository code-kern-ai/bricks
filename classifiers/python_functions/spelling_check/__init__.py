from pydantic import BaseModel
from collections import Counter
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words
from nltk.corpus import brown

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

    suggestions = []
    for word in misspelled:
        temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w) for w in word_list if w[0] == word[0]]
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:15]])

    for i, _ in enumerate(text_list_original):
        for j, _ in enumerate(misspelled):
            count = Counter(suggestions[j])
            if text_list_original[i] == misspelled[j]:
                text_list_original[i] = count.most_common(1)[0][0]

    text_corr = " ".join(text_list_original)

    sugg = []
    for word in suggestions:
        for i in word:
            if i not in sugg:
                sugg.append(i)

    return {
        "misspelledWords": misspelled,
        "suggestedCorrections": sugg[0:3],
        "correctText": text_corr,
    }

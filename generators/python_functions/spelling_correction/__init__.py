from pydantic import BaseModel
from collections import Counter
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words, brown

INPUT_EXAMPLE = {
    "text": "This text contaisn some speling errors.",
}


class SpellingCorrectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE,
        }


def spelling_correction(request: SpellingCorrectionModel):
    """Correct spelling mistakes in a text."""

    text = request.text
    words_corpus = words.words()
    brown_corpus = brown.words()
    word_list = words_corpus + brown_corpus
    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()

    misspelled = []
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            misspelled.append(text_original[i])

    suggestions = []
    for word in misspelled:
        temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w) for w in word_list if w[0] == word[0]]
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:15]])

    for i, _ in enumerate(text_lower):
        for j, _ in enumerate(misspelled):
            count = Counter(suggestions[j])
            if text_lower[i] == misspelled[j]:
                text_original[i] = count.most_common(1)[0][0]

    text_corr = " ".join(text_original)
    return {"text": text_corr}

```python
from typing import Dict, Any
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
nltk.download('words')
from nltk.corpus import words


def grammar_check(record: Dict[str, Any]):
    text = record["your_text"]
    correct_words = words.words()
    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    misspells = []
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in correct_words and text_original[i] not in correct_words:
            misspells.append(text_original[i])

    suggestions = []
    for word in misspells:
        temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w) for w in correct_words if w[0] == word[0]]
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:3]])

    for i, _ in enumerate(text_original):
        for j, _ in enumerate(misspells):
            if text_original[i] == misspells[j]:
                text_original[i] = suggestions[j][0]
    
    text_corrected = " ".join(text_original)
    
    return {"correctedText": text_corrected}

```
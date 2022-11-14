```python
from typing import Dict, Any
from collections import Counter
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
nltk.download('words', 'brown')
from nltk.corpus import words, brown


def spelling_check(record: Dict[str, Any]):
    text = record["your_text"]
    words_corpus = words.words()
    brown_corpus = brown.words()
    word_list = words_corpus + brown_corpus
    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    misspells = []
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            misspells.append(text_original[i])

    suggestions = []
    for word in misspells:
        temp = [(jaccard_distance(set(ngrams(word, 2)), set(ngrams(w, 2))), w) for w in word_list if w[0] == word[0]]
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:20]])
    
    count = Counter(suggestions[0])

    for i, _ in enumerate(text_original):
        for j, _ in enumerate(misspells):
            if text_original[i] == misspells[j]:
                text_original[i] = count.most_common(1)[0][0]
    
    text_corrected = " ".join(text_original)
    
    return {"correctedText": text_corrected}

```
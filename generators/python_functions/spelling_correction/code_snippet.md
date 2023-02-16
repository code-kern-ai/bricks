```python
from collections import Counter
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words, brown

#currently only english language is supported here
#reach out to us if this should be extended for other languages

YOUR_ATTRIBUTE: str = "text" # only text attributes

def spelling_correction(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    text = record[YOUR_ATTRIBUTE].text # SpaCy doc, hence we need to use .text to get the string.
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
        suggestions.append([i[1] for i in sorted(temp, key=lambda val:val[0])[0:15]])
        
    for i, _ in enumerate(text_lower):
        for j, _ in enumerate(misspells):
            count = Counter(suggestions[j])
            if text_original[i] == misspells[j]:
                text_original[i] = count.most_common(1)[0][0]
                
    text_corr = " ".join(text_original)
    return text_corr
```
```python
from nltk.corpus import words, brown

ATTRIBUTE: str = "text" # only text attributes
LABEL_MISTAKES: str = "contains mistakes"
LABEL_CORRECT: str = "no mistakes"

def spelling_check(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    words_corpus = words.words()
    brown_corpus = brown.words()
    word_list = set(words_corpus + brown_corpus)

    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    misspells = []
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            misspells.append(text_original[i])

    if len(misspells) > 0:
        return LABEL_MISTAKES
    else:
        return LABEL_CORRECT
```
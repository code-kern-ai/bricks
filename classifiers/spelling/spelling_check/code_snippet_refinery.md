```python
from nltk.corpus import words, brown

ATTRIBUTE: str = "text" # only text attributes
LABEL_MISTAKES: str = "contains mistakes"
LABEL_CORRECT: str = "no mistakes"

words_corpus = words.words()
brown_corpus = brown.words()
word_list = set(words_corpus + brown_corpus)

def spelling_check(record):
    text = record[ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            return LABEL_MISTAKES

    return LABEL_CORRECT
```
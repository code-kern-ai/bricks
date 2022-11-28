```python
import nltk
from nltk.corpus import words, brown

YOUR_ATTRIBUTE = "text"

def spelling_check(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

    words_corpus = words.words()
    brown_corpus = brown.words()

    word_list = words_corpus + brown_corpus
    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    misspells = []
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            misspells.append(text_original[i])

    return {"spellingErrors": len(misspells)}

```
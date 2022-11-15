```python
from typing import Dict, Any
import nltk
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

    return {"spellingErrors": len(misspells)}

```
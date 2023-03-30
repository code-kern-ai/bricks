```python
from nltk.corpus import words, brown

# replace this list with a list containing your data
text = ["This contins speling mistaks.", "Thats not how you wraite this.", "This should be a correct sentence."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "label_mistakes": "contains mistakes",
    "label_correct": "no mistakes",
}

def spelling_check(record: dict) -> dict:
    words_corpus = words.words()
    brown_corpus = brown.words()
    word_list = set(words_corpus + brown_corpus)

    mistakes = []
    for entry in record["your_text"]:
        text_lower = entry.replace(',', '').replace('.', '').lower().split()
        text_original = entry.replace(',', '').replace('.', '').split()
        
        misspells = []
        for i, _ in enumerate(text_lower):
            if text_lower[i] not in word_list and text_original[i] not in word_list:
                misspells.append(text_original[i])

        if len(misspells) > 0:
            mistakes.append(record["label_mistakes"])
        else:
            mistakes.append(record["label_correct"])
    return {"spellchecks": mistakes}
```
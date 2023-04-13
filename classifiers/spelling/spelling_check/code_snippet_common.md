```python
from nltk.corpus import words, brown

words_corpus = words.words()
brown_corpus = brown.words()
word_list = set(words_corpus + brown_corpus)
def spelling_check(text:str, return_label_has_mistakes:str, return_label_no_mistakes:str) -> str:
    """
    @param text: text to check
    @param return_label_has_mistakes: label to return if the text contains mistakes
    @param return_label_no_mistakes: label to return if the text does not contain mistakes
    @return: either return_label_has_mistakes or return_label_no_mistakes
    """
    text_lower = text.replace(',', '').replace('.', '').lower().split()
    text_original = text.replace(',', '').replace('.', '').split()
    
    for i, _ in enumerate(text_lower):
        if text_lower[i] not in word_list and text_original[i] not in word_list:
            return return_label_has_mistakes
      
    return return_label_no_mistakes

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ["This contins speling mistaks.", "Thats not how you wraite this.", "This should be a correct sentence."]
    label_no_mistakes = "no mistakes"
    label_has_mistakes = "mistakes"
    for text in texts:
        print(f"\"{text}\" has {spelling_check(text, label_has_mistakes, label_no_mistakes)}")

example_integration()
```
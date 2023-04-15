```python
from typing import List, Tuple
from collections import Counter
import spacy

def most_frequent_words(text:str, n_words:int = 5)->List[Tuple[str,int]]:
    """ Count most frequent words in a text, ignores stopwords and punctuation
    @param text: text we want to count words in
    @param n_words: amount of return entries in the list
    @return: list of most common words (Tuple of word and count)
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return Counter(words).most_common(n_words)
    
# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["APPL went down by 5% in the past two weeks. Shareholders are concerned over the continued recession since APPL and NASDAQ have been hit hard by this recession. Risks pertaining to short-selling are pouring in as APPL continues to depreciate. If the competitors come together and start short-selling, the stock can face calamity."]

    for text in texts:
        print(f"the most common words in \n\n{text}\n\nare:\n{most_frequent_words(text)}")
example_integration() 
```

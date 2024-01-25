```python
import spacy
from nltk.util import ngrams
from typing import List, Tuple

def nltk_ngram_generator(sentence: str, ngram_size: int = 2) -> List[Tuple[str, ...]]:
    """Generate word n-grams from the input sentence. Punctuation and stop words are preserved.
    @param sentence: The input sentence from which n-grams will be generated. 
    @param ngram_size: The size of each n-gram. Default: 2. This parameter specifies the number of consecutive words that will be included in each n-gram. For example, an ngram_size of 2 will produce bigrams. 
    @return: A list where each element is a tuple of strings (words), with each tuple representing an n-gram. The size of each tuple (i.e., the number of words it contains) corresponds to the 'ngram_size' specified.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    n_grams = list(ngrams(tokens, ngram_size))

    return n_grams
    
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    sentences = ["Despite the unpredictable weather, the enthusiastic crowd gathered at the park for the annual summer festival, eagerly anticipating an evening filled with music, food, and vibrant celebrations.", "The rapidly advancing technology sector offers exciting opportunities and significant challenges, sparking debates among experts and novices alike."]

    for i, sentence in enumerate(sentences):
        print(f"N_grams for sentence {i+1} are: {nltk_ngram_generator(sentence)}")

example_integration()
```

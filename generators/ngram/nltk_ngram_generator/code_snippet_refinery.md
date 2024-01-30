```python
from nltk.util import ngrams
ATTRIBUTE: str = "text" # only text fields
NGRAM_SIZE: int = 2

def nltk_ngram_generator(record):

    tokens = [token.text for token in record[ATTRIBUTE]]
    n_grams = list(ngrams(tokens, NGRAM_SIZE))
    n_grams_str = str(n_grams).strip('[]')

    return n_grams_str
```

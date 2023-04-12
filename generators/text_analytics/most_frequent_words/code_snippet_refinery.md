```python
from collections import Counter

ATTRIBUTE: str = "text"  # only text fields
N_WORDS: int = 5

def most_frequent_words(record):
    
    words = [token.text for token in record[ATTRIBUTE] if not token.is_stop and not token.is_punct]
    return str(Counter(words).most_common(N_WORDS)).strip("[]")
```

```python
from collections import Counter

YOUR_ATTRIBUTE: str = "text"  # only text fields
YOUR_N_WORDS: int = 5

def most_frequent_words(record):
    
    words = [token.text for token in record[YOUR_ATTRIBUTE] if not token.is_stop and not token.is_punct]
    return Counter(words).most_common(YOUR_N_WORDS)
```
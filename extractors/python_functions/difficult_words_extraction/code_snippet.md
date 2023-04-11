```python
from flashtext import KeywordProcessor

YOUR_ATTRIBUTE: str =  "text"
SYLLABLE_THRESHOLD: int = 2

def difficult_words_extraction(record):
    
    text = record[YOUR_ATTRIBUTE].text
    syllable_threshold = SYLLABLE_THRESHOLD
    difficult_words = textstat.difficult_words_list(text, syllable_threshold)
    
    return difficult_words
```
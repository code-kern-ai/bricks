```python
import textstat
import re

ATTRIBUTE: str =  "text" # only text attributes
SYLLABLE_THRESHOLD: int = 3
LABEL: str = "difficult_word"

def difficult_words_extraction(record):
    text = record[ATTRIBUTE].text
    syllable_threshold = SYLLABLE_THRESHOLD
    difficult_words = textstat.difficult_words_list(text, syllable_threshold)
    
    for word in difficult_words: 
        if word in text:
            start, end = re.search(rf"({word})", text).span() # get the position of the word in the text
            span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
            yield LABEL, span.start, span.end
```
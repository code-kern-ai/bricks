```python
from flashtext import KeywordProcessor
import re

YOUR_ATTRIBUTE: str =  "text"
SYLLABLE_THRESHOLD: int = 2

def difficult_words_extraction(record):
    text = record[YOUR_ATTRIBUTE].text
    syllable_threshold = SYLLABLE_THRESHOLD
    difficult_words = textstat.difficult_words_list(text, syllable_threshold)
    
    for word in difficult_words: 
        start, end = re.match(rf"({word})", text).span() # get the position of the word in the text
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield LABEL, span.start, span.end

```
```python
import textstat
from collections import Counter

ATTRIBUTE: str = "text" # only text attributes
TARGET_LANGUAGE: str = "en" # iso codes

def chunked_sentence_complexity(record):
    complexities = [textstat.flesch_reading_ease(sent.text) for sent in record[ATTRIBUTE].sents] 

    avg = int(round(sum(complexities) / len(complexities)))
    return get_mapping_complexity(avg)

def get_mapping_complexity(score):
    if score < 30:
        return "very difficult"
    if score < 50:
        return "difficult"
    if score < 60:
        return "fairly difficult"
    if score < 70:
        return "standard"
    if score < 80:
        return "fairly easy"
    if score < 90:
        return "easy"        
    return "very easy"

if TARGET_LANGUAGE is not None:
    textstat.set_lang(TARGET_LANGUAGE)
```
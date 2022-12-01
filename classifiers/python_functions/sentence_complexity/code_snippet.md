```python
import textstat
from typing import Dict

# Change these according to your attribute names
YOUR_ATTRIBUTE: str = "text"
TARGET_LANGUAGE: str = "en"

MAX_SCORE: int = 122
MIN_SCORE: int = 0

def fn_sentence_complexity(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string

def setall(d, keys, value):
    for k in keys:
        d[k] = value
    language = TARGET_LANGUAGE
    if language is not None:
        textstat.set_lang(language)
    
def get_mapping_complexity(score):
    if score < MIN_SCORE:
        return OUTCOMES[MIN_SCORE]
    return OUTCOMES[int(score)]

    sentence_complexity_score = textstat.flesch_reading_ease(text)
    sentence_complexity = get_mapping_complexity(sentence_complexity_score)
    return sentence_complexity

OUTCOMES: Dict = {}
setall(OUTCOMES, range(90, MAX_SCORE), "very easy")
setall(OUTCOMES, range(80, 90), "easy")
setall(OUTCOMES, range(70, 80), "fairly easy")
setall(OUTCOMES, range(60, 70), "standard")
setall(OUTCOMES, range(50, 60), "fairly difficult")
setall(OUTCOMES, range(30, 50), "difficult")
setall(OUTCOMES, range(MIN_SCORE, 30), "very difficult")
```
```python
#expects labeling task to have labels ["very easy", "easy" ,"fairly easy", "standard", "fairly difficult", "difficult", "very difficult"]

import textstat
from typing import Dict

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_TARGET_LANGUAGE: str = "en" # iso codes

YOUR_MAX_SCORE: int = 100
YOUR_MIN_SCORE: int = 0

def sentence_complexity(record):
    text = record[YOUR_ATTRIBUTE].text # SpaCy document, hence we need to call .text to get the string
    sentence_complexity_score = textstat.flesch_reading_ease(text)
    sentence_complexity = get_mapping_complexity(sentence_complexity_score)
    return sentence_complexity

def set_all(d, keys, value):
    for k in keys:
        d[k] = value
    
def get_mapping_complexity(score):
    if score < YOUR_MIN_SCORE:
        return outcomes[YOUR_MIN_SCORE]
    if score > YOUR_MAX_SCORE:
        return outcomes[YOUR_MAX_SCORE]
    return outcomes[int(score)]

if YOUR_TARGET_LANGUAGE is not None:
    textstat.set_lang(YOUR_TARGET_LANGUAGE)

outcomes: Dict = {}
set_all(outcomes, range(90, YOUR_MAX_SCORE + 1), "very easy")
set_all(outcomes, range(80, 90), "easy")
set_all(outcomes, range(70, 80), "fairly easy")
set_all(outcomes, range(60, 70), "standard")
set_all(outcomes, range(50, 60), "fairly difficult")
set_all(outcomes, range(30, 50), "difficult")
set_all(outcomes, range(YOUR_MIN_SCORE, 30), "very difficult")
```
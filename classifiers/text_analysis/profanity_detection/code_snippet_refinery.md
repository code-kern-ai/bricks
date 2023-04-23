```python
from better_profanity import profanity

ATTRIBUTE: str = "text" # only text attributes
LABEL_PROFANE: str = "profane"
LABEL_NOT_PROFANE: str = "not_profane"

def profanity_detection(record):
    # SpaCy document, hence we need to call .text on our record to get the string
    
    if profanity.contains_profanity(record[ATTRIBUTE].text):
        return LABEL_PROFANE
    return LABEL_NOT_PROFANE
```
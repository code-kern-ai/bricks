```python
from better_profanity import profanity

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL_PROFANE: str = "profane"
YOUR_LABEL_NOT_PROFANE: str = "not_profane"

def profanity_detection(record):
    # SpaCy document, hence we need to call .text on our record to get the string
    return YOUR_LABEL_PROFANE if profanity.contains_profanity(record[YOUR_ATTRIBUTE].text) else YOUR_LABEL_NOT_PROFANE 
```
```python
from better_profanity import profanity

YOUR_ATTRIBUTE = "body"

def profanity_detection(record):
    # SpaCy document, hence we need to call .text on our record to get the string
    return "Profane" if profanity.contains_profanity(record[YOUR_ATTRIBUTE].text) else "Not-profane" 
```
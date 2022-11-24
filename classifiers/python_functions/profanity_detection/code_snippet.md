```python
from better_profanity import profanity

YOUR_ATTRIBUTE = "body"

def profanity_detection(record):
    return "Profane" if profanity.contains_profanity(record[YOUR_ATTRIBUTE].text) else "Not-profane"
```
```python
ATTRIBUTE: str = "text" # only text attributes

def word_count_classifier(record):
    words = record[ATTRIBUTE].text.split()
    length = len(words)
    if length < 5:
        return "short"
    elif length < 20:
        return "medium"
    else:
        return "long"
```
```python
ATTRIBUTE: str = "text" # only text attributes

def text_length(text):
    words = text.split()
    length = len(words)
    if length < 5:
        return "short"
    elif length < 20:
        return "medium"
    else:
        return "long"
```
```python
ATTRIBUTE: str = "text" # only text attributes

def newline_splitter(record):
    splits = [t.strip() for t in record[ATTRIBUTE].text.split("\n")]
    return [val for val in splits if len(val) > 0]
```
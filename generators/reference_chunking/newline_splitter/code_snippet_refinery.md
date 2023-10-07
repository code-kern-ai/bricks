```python
ATTRIBUTE: str = "text" # only text attributes

def newline_splitter(record):
    splits = record[ATTRIBUTE].text.strip().split("\n")
    return [val for val in splits if len(val) > 0]
```
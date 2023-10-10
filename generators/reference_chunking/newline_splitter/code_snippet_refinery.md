```python
ATTRIBUTE: str = "text" # only text attributes

def newline_splitter(record):
    splits = record[ATTRIBUTE].text.split("\n")
    return [val.strip() for val in splits if len(val) > 0]
```
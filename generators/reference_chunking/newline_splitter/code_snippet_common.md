```python
from typing import List 

def newline_splitter(text: str) -> List[str]:
    splits = text.strip().split("\n")
    return [val for val in splits if len(val) > 0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["""
    This is a sentences.
    This too, but in another line
    """]
    for text in texts:
        print(f"The text {text} was split into {newline_splitter(text)}")

example_integration()
```
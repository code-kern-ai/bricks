```python
from typing import List 

def newline_splitter(text: str) -> List[str]:
    """
    @param text: The input string that needs to be split.
    @return:  A list of strings where each string is a non-empty line from the input.
    """
    splits = text.split("\n")
    return [val.strip() for val in splits if len(val) > 0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    texts = ["""
    This is a sentences.
    This too, but in another line
    """, "This is a sentence\nwith a newline literal!"]
    for text in texts:
        print(f"The text {text} was split into {newline_splitter(text)}")

example_integration()
```
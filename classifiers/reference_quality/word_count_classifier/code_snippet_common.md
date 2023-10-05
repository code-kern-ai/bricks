```python
def word_count_classifier(text: str) -> str:
    """
    @param text: text to check the length of.
    @return: either 'short', 'medium' or 'long' depending on the counted words.
    """
    words = text.split()
    length = len(words)
    if length < 5:
          return "short"
    elif length < 20:
          return "medium"
    else:
          return "long"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["This is short.", "This is a text with medium length.", "This is a longer text with many more words. There is even a second sentence with extra words. Splendid, what a joyful day!"]
    for text in texts:
        print(f"\"{text}\" is -> {word_count_classifier(text)}")

example_integration()
```
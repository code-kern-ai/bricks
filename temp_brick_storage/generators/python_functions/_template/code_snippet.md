```python
def my_generator(record): 
    return "label"
```
_Notes, remove them when you're finished_:
- The record is a dictionary, you can retrieve text e.g. as `record["text"].text`, as the record is already tokenized by spaCy.
- The function `return`s a single label
- What is written here will be copied to refinery; it must fit the interface of what refinery expects.
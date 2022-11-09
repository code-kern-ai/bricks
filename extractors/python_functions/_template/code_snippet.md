```python
def my_tagger(record): 
    yield "label", start, end
```

_Notes, remove them when you're finished_:
- The record is a dictionary, you can retrieve text e.g. as `record["text"].text`, as the record is already tokenized by spaCy.
- The function `yield`s tuples of the label and the start and end position of the label in the text.
- What is written here will be copied to refinery; it must fit the interface of what refinery expects.

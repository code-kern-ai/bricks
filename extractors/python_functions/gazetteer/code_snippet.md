```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list

def gazetter(record):
    YOUR_ATTRIBUTE = "details"
    YOUR_LABEL = "PERSON"
    LOOKUP_VALUES = ["Max"]
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in LOOKUP_VALUES]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
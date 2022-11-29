```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list
from typing import List

YOUR_ATTRIBUTE: str = "text"
YOUR_LABEL: str = "PERSON"
LOOKUP_VALUES: List[str] = ["Max"]

def gazetter(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in LOOKUP_VALUES]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
```python
import knowledge
from typing import List

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "PERSON"
LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
LOOKUP_VALUES: List[str] = ["Max"]

final_list = []
if LOOKUP_LISTS:
    for lookup_list in LOOKUP_LISTS:
        final_list += lookup_list
if LOOKUP_VALUES:
    final_list += LOOKUP_VALUES

def gazetteer_extraction(record):
    for chunk in record[ATTRIBUTE].noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in final_list]):
            yield LABEL, chunk.start, chunk.end
```
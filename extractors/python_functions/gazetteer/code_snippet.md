```python
from typing import List
import knowledge

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "PERSON"
YOUR_LOOKUP_LIST: str = knowledge.my_lookup_list #either lookup list or lookup values or both
YOUR_LOOKUP_VALUES: List[str] = ["Max"]

final_list = []
if YOUR_LOOKUP_LIST:
    final_list += YOUR_LOOKUP_LIST
if YOUR_LOOKUP_VALUES:
    final_list += YOUR_LOOKUP_VALUES

def gazetter(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in final_list]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
```python
import knowledge

YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LABEL: str = "PERSON"
YOUR_LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
YOUR_LOOKUP_VALUES: List[str] = ["Max"]

final_list = []
if YOUR_LOOKUP_LISTS:
    for lookup_list in YOUR_LOOKUP_LISTS:
        final_list += lookup_list
if YOUR_LOOKUP_VALUES:
    final_list += YOUR_LOOKUP_VALUES

def gazetteer_extraction(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        if any([chunk.text in trie or trie in chunk.text for trie in final_list]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
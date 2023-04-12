```python
import knowledge

WINDOW: int = 4 # choose any window size here
LABEL: str = "PERSON"
ATTRIBUTE: str = "text" # only text attributes
LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
LOOKUP_VALUES: List[str] = ["Max"]

final_list = []
if LOOKUP_LISTS:
    for lookup_list in LOOKUP_LISTS:
        final_list += lookup_list
if LOOKUP_VALUES:
    final_list += LOOKUP_VALUES

def window_search_extraction(record):
    for chunk in record[ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (WINDOW // 2) + 1)
        window_doc = record[ATTRIBUTE][left_bound: right_bound]
        if any([term in window_doc.text for term in final_list]):
            yield LABEL, chunk.start, chunk.end
```
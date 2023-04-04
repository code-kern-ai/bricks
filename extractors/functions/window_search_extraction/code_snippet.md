```python
import knowledge

YOUR_WINDOW: int = 4 # choose any window size here
YOUR_LABEL: str = "PERSON"
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
YOUR_LOOKUP_VALUES: List[str] = ["Max"]

final_list = []
if YOUR_LOOKUP_LISTS:
    for lookup_list in YOUR_LOOKUP_LISTS:
        final_list += lookup_list
if YOUR_LOOKUP_VALUES:
    final_list += YOUR_LOOKUP_VALUES

def window_search_extraction(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (YOUR_WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (YOUR_WINDOW // 2) + 1)
        window_doc = record[YOUR_ATTRIBUTE][left_bound: right_bound]
        if any([term in window_doc.text for term in final_list]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
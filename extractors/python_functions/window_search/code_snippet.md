```python
from typing import List

YOUR_WINDOW: int = 4 # choose any window size here
YOUR_LABEL: str = "PERSON"
YOUR_ATTRIBUTE: str = "text" # choose any available attribute here
LOOKUP_VALUES: List[str] = ["join"] # this could also be coming from a knowledge base via `import knowledge`

def window_cue_search(record):
    for chunk in record[YOUR_ATTRIBUTE].noun_chunks:
        left_bound = max(chunk.sent.start, chunk.start - (YOUR_WINDOW // 2) +1)
        right_bound = min(chunk.sent.end, chunk.end + (YOUR_WINDOW // 2) + 1)
        window_doc = record[YOUR_ATTRIBUTE][left_bound: right_bound]
        if any([term in window_doc.text for term in LOOKUP_VALUES]):
            yield YOUR_LABEL, chunk.start, chunk.end
```
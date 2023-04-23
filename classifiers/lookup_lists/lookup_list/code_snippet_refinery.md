```python
import knowledge
from typing import List

ATTRIBUTE: str = "text" # only text attributes

LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
LOOKUP_VALUES: List[str] = ["john@kern.ai", "jane@kern.ai"]
LABEL: str = "in lookup"


final_list = []
if LOOKUP_LISTS:
    for lookup_list in LOOKUP_LISTS:
        final_list += lookup_list
if LOOKUP_VALUES:
    final_list += LOOKUP_VALUES

def lkp_known_sender(record):
    for known_sender in final_list:
        if known_sender.lower() in record[ATTRIBUTE].text.lower(): # SpaCy document, hence we need to call .text to get the string
            return LABEL
```
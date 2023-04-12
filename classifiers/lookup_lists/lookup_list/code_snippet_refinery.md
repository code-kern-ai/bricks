```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list
import knowledge
from typing import List

ATTRIBUTE: str = "text"
LOOKUP_LIST: List[str] = knowledge.my_lookup_list # Change this to the name of your lookup list
LOOKUP_VALUES: List[str] = ["john@kern.ai", "jane@kern.ai"]
LABEL: str = "ham"

# If further values are specified, add them to the lookup list.
if LOOKUP_VALUES:
    for value in LOOKUP_VALUES:
        LOOKUP_LIST.append(value)

def lkp_known_sender(record):
    for known_sender in LOOKUP_LIST:
        if known_sender.lower() in record[ATTRIBUTE].text.lower(): # SpaCy document, hence we need to call .text to get the string
            return LABEL
```
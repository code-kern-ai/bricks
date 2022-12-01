```python
from typing import List
import knowledge

YOUR_ATTRIBUTE: str = "text" #only text attributes
YOUR_LABEL: str = "known sender"
YOUR_LOOKUP_LISTS: List[str] = [knowledge.my_lookup_list] #either lookup lists or lookup values or both
YOUR_LOOKUP_VALUES: List[str] = ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai"]

final_list = []
if YOUR_LOOKUP_LISTS:
    for lookup_list in YOUR_LOOKUP_LISTS:
        final_list += lookup_list
if YOUR_LOOKUP_VALUES:
    final_list += YOUR_LOOKUP_VALUES

def lkp_known_sender(record):
    for known_sender in final_list:
        if known_sender.lower() in record[YOUR_ATTRIBUTE].text.lower(): # SpaCy document, hence we need to call .text to get the string
            return YOUR_LABEL
```
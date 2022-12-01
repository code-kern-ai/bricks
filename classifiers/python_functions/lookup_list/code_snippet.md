```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list
from typing import List
import knowledge

YOUR_ATTRIBUTE: str = "text"
YOUR_LOOKUP_LIST: List[str] = knowledge.my_lookup_list
YOUR_LOOKUP_VALUES: List[str] = ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai"]
YOUR_LABEL: str = "ham"

final_list = []
if YOUR_LOOKUP_LIST:
    for lookup_list in YOUR_LOOKUP_LIST:
        final_list += lookup_list
if YOUR_LOOKUP_VALUES:
    final_list += YOUR_LOOKUP_VALUES

def lkp_known_sender(record):
    for known_sender in final_list:
        if known_sender.lower() in record[YOUR_ATTRIBUTE].text.lower(): # SpaCy document, hence we need to call .text to get the string
            return YOUR_LABEL
```
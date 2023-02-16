```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list
import knowledge

YOUR_ATTRIBUTE: str = "text"
YOUR_LOOKUP_LIST: List[str] = knowledge.my_lookup_list # Change this to the name of your lookup list
YOUR_LOOKUP_VALUES: List[str] = ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai"]
YOUR_LABEL: str = "ham"

# If further values are specified, add them to the lookup list.
if YOUR_LOOKUP_VALUES:
    for value in YOUR_LOOKUP_VALUES:
        YOUR_LOOKUP_LIST.append(value)

def lkp_known_sender(record):
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    for known_sender in YOUR_LOOKUP_LIST:
        if known_sender.lower() in record[YOUR_ATTRIBUTE].text.lower(): # SpaCy document, hence we need to call .text to get the string
            return YOUR_LABEL
```